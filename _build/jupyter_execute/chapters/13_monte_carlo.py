#!/usr/bin/env python
# coding: utf-8

# # Monte Carlo and portfolios
# 
# We saw how to simulate the price of an asset back when we looked at the price of [Bitcoin](chapters/7_nasdaq_api.html#btc-sim) and using the Nasdaq API. We are going to take a more complete look here at **simulating correlated assets within a portfolio**. These methods can be used for measuring portfolio risk, for simulating client portfolios in a [financial planning setting](https://www.kitces.com/blog/volatility-drag-variance-drain-mean-arithmetic-vs-geometric-average-investment-returns/), or [pricing complex options](https://en.wikipedia.org/wiki/Monte_Carlo_methods_for_option_pricing) like [Asian options](https://en.wikipedia.org/wiki/Asian_option). 
# 
# I am basing a lot of my code and discussion on this [blog post](https://medium.com/codex/simulate-multi-asset-baskets-with-correlated-price-paths-using-python-472cbec4e379). 
# 
# This material is related to the [Heston model](https://www.codearmo.com/python-tutorial/heston-model-simulation-python) for simulating the prices of correlated assets. The volatility of the assets are linked together. In the Heston model, the volatility of an asset today is also related to past volatility. We'll do more on this when we get to [GARCH models](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity). 
# 
# We'll also use **pandas data-reader** to bring in some stock prices from Yahoo! finance. You'll need to run `pip install pandas-datareader` in the terminal. You can read more about it [here](https://pydata.github.io/pandas-datareader/remote_data.html).
# 
# The textbook goes into more detail than we need, but this is the type of material that you'd cover in a first-semester mathematical finance course in a Masters program.
# 
# ## Chapter 12 Highlights
# 
# | Topic         | Pages  |
# | :-------------------------------------------------------------------------------------- | :--------- | 
# | **Basic Price Simulation**. Simulations with just a single asset. Our author uses these techniques for basic option pricing later on.     | 352 - 365      | 
# | **Stochastic Volatility**. Heston volatility model and Cholesky decomposition for correlated assets.    | 365 - 368    | 

# ## How correlation affects our simulations
# 
# However, when we start to form portfolios, we are going to care about the correlations across assets. We've already seen this when looking at portfolio math. When simulating the Bitcoin prices, we took random numbers from the standard normal distribution and then scaled them by our estimate for the volatility of BTC. This allowed us to capture the randomness of the returns.
# 
# However, when dealing with more than one asset, we can't do that, since the assets are **not independent** from one another. If Apple goes up, Google is more likely to have gone up as well. The two stocks are **correlated**. How can we account for this in our simulation? We will create **correlated random shocks** ($W$), where the random movement of one asset depends on another assets movement.
# 
# Let's try a simulation to see what's going on. I'll draw two random variables from the standard normal distribution, N(0,1). The random part of the return for Asset 1, $W_1$, is simply the random draw, $x_1$. However, the random part of the return for Asset 2 $W_2$, is correlated with whatever $x_1$ ends up being. Mathematically, this dependent random movement is given as:
# 
# \begin{align}
# W_2 = \rho x_1 + (1 - \sqrt{\rho^2}) x_2
# \end{align}
# 
# I'll set the correlation, $\rho$, to be -0.80. These two assets are negatively correlated, so they should move in opposite directions. We'll set each asset to have the same mean return and same volatility. I'll set the starting price of each of these assets to 1.
# 
# We'll bring in our usual packages and try this out. This code should look a lot like the Bitcoin code, except that I now have two assets. I am only doing one simulation for each asset, so two total simulations.
# 

# In[1]:


import datetime
import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


T = 251 # How long is our simulation? Let's do 252 days (0 to 251)
N = 251 # number of time points in the prediction time horizon, making this the same as T means that we will simulate daily returns 

rho = -0.80 # Correlation between our two assets. Change me to get different patterns!
mu = 0.05/252 # Mean return (log). Using daily. 
sigma = 0.12/np.sqrt(252)  # Volatility of returns (standard deviation). Using daily. 

S_0 = 1 # Starting price

dt = T/N # One day price movements
dW = np.zeros([2, N]) # Set up random shocks with zeroes for now

# Sample two random variables from the standard normal distribution standard normal distribution. Two rows of 251 values from N(0,1).
X = np.random.normal(scale = np.sqrt(dt), size=(2, N))

# Generate correlated random shock, W. 
dW[0] = X[0] # Same as first row in X
dW[1] = rho * X[0] + (1 - np.sqrt(rho**2)) * X[1] # Dependent on both sets of random values. How dependent? Correlation determines.

#Cumulative sum of random shocks for our assets.
W = np.cumsum(dW, axis=1) 

time_step = np.linspace(dt, T, N)
time_steps = np.broadcast_to(time_step, (2, N))

S_t = S_0 * np.exp((mu - 0.5 * sigma ** 2) * time_steps + sigma * W)

S_t = np.insert(S_t, 0, S_0, axis=1)


# Let's plot the two sets of cumulative returns to see if they make sense.

# In[3]:


sims = pd.DataFrame(np.transpose(S_t))

# plotting
ax = sims.plot(alpha=0.2, legend=False)

ax.set_title('Simulated Asset Returns with Correlation of -0.80', fontsize=12);


# You can really see the negative correlation!
# 
# Let's move to some real data now. I am using `pandas data-reader` to bring in adjusted closing prices for five stocks. I then calculate discrete returns and check my descriptives.

# In[4]:


start_date = datetime.datetime(2019, 1, 1)
end_date = datetime.datetime(2020, 1, 1)
ticker_list = ["AAPL", "F", "FB", "AMZN", "XOM"]

stock_data = pdr.DataReader(ticker_list, "yahoo", start_date, end_date)

prices = stock_data['Adj Close']

rets = prices.pct_change().dropna()


# In[5]:


rets


# In[6]:


rets.describe()


# Seems legit! The average daily returns are all positive, but around zero. The worst daily return is an Apple return of -9.96%. Each stock has a count of 251 daily returns over the course of the year.
# 
# OK, now it's time to set up our simulation. We will do 50 different future portfolio paths. We'll simulate 252 days worth of prices. We'll use these prices to find returns.
# 
# We are simulating random numbers. But, computers cant *really* generate truly random numbers. We can set a **seed** value that will always generate the same set of random values. 
# 
# `mu` has our arithmetic average returns. 
# 
# We then find our usual variance-covariance matrix using `.cov()`.

# In[7]:


np.random.seed(1986)

T = 252 # How long is our simulation? Let's do 252 days.
N = 252 # number of time points in the prediction time horizon, making this the same as T means that we will simulate daily returns 
N_SIM = 50  # How many simulations to run?
dt = T/N # daily steps
noa = 5 # Number of assets

weights = np.array(noa * [1. / noa,])  # EW portfolio based on number of assets. You can change this array to have any weights you want.

mu = rets.mean()
cov = rets.cov()
sigma = rets.std()
corr = rets.corr()

# initial matrix
port_returns_all = np.full((T-1, N_SIM), 0.) # One less return than price


# We can look at the actual correlations among our assets to get a sense of what we are using to form portfolios.

# In[8]:


corr


# Let's start with a simple case. We'll simulate one series of returns for each of our assets, but include **correlated shocks**. We'll get returns by actually simulating prices and then calculating returns.
# 
# The first line picks out he latest prices for each stock. This is where we will start. You could start each stock at \$1 and get the same return result, since it's the change that matters.
# 
# The second line is our **math magic**. This takes our variance-covariance matrix and does something called the **Cholesky Decomposition**. The variance-covariance matrix contains the information for how our assets move together (i.e. covariance). This method will allow us to use the **correlation among our assets** when simulating the random price paths. We want correlated assets to move together. You can read more about these methods [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4066115). 
# 
# `A` is a $5\times5$ matrix, just like the variance-covariance matrix, but the upper triangular part is all zeroes, while the lower triangular part still contains the dependencies among our assets. 
# 
# `S` is 252 days of "empty" prices for our 5 assets. We'll fill these in with simulated prices. We make the first price in the array equal to the latest price.
# 
# Then, we have a `for` loop that simulates prices for each asset across all 252 days.
# 
# We first calculate the **drift**, or deterministic component, of the return. This is based on the mean and standard deviation of the returns. `dt` is just 1 day in this case.
# 
# We then pull 5 random variables, one for each asset, from the standard normal distribution. We'll call these 5 numbers `Z`. 
# 
# If you multiply `A` and `Z`, then you get correlated standard normal variables, instead of five sets of random variables with no relationships among them.
# 
# The last line in the `for` loop is again how we simulate prices. I have done the drift (deterministic) and diffusion (random) terms separately to make it easier to see what's going on. With this type of simulation, the stock price today is the stock price yesterday times $\exp(\text{drift} + \text{diffusion})$. This is **continuous compounding**. 
# 
# I take these prices and calculate returns again. But, these are now one set of simulated returns.
# 
# Finally, I take the returns and multiply them by our chosen weights to get a single set of **portfolio returns**.

# In[9]:


S_0 = prices.iloc[-1]
A = np.linalg.cholesky(cov)
S = np.zeros([noa, N])
S[:, 0] = S_0

for i in range(1, N):    
    drift = (mu - 0.5 * sigma**2) * dt # dt = 1. This is the deterministic part of the daily return. It's the same every day.
    Z = np.random.normal(0., 1., noa) # Putting as period after a number in Python makes division work correctly when dealing with integers. Not sure we even need it here.
    diffusion = np.matmul(A, Z) * np.sqrt(dt) # dt = 1. This is the random part. 
    S[:, i] = S[:, i-1]*np.exp(drift + diffusion) # S_t = S_t-1 * e^(r). Continuous compounding. 

R = pd.DataFrame(S.T).pct_change().dropna() # Create returns from those simulated prices.

port_rets = np.cumprod(np.inner(weights, R) + 1) # Weights x returns, cumulative product to get cumulative portfolio returns.


# ```{hint}
# I recommend running each line separately and then looking at the resulting variabl/array. This is how you can figure out what's going on in the simulation.
# ```
# 
# Let's check the correlations and descriptives for these simulated returns. 

# In[10]:


R.corr()


# In[11]:


R.describe()


# They seem to make sense! The simulated correlations, in particular, are close to the empirical correlations. 

# Finally, let's add **one more element to this loop**. We can find 50 different portfolio returns by wrapping the code above in another `for` loop.
# 
# Remember, the **indentation** matters! It tells us how the loops are **nested**. 
# 

# In[12]:


S_0 = prices.iloc[-1]
A = np.linalg.cholesky(cov)
S = np.zeros([noa, N])
S[:, 0] = S_0

for t in range(0, N_SIM):
    for i in range(1, N):    
        drift = (mu - 0.5 * sigma**2) * dt 
        Z = np.random.normal(0., 1., noa) 
        diffusion = np.matmul(A, Z) * np.sqrt(dt) 
        S[:, i] = S[:, i-1]*np.exp(drift + diffusion) 

        R = pd.DataFrame(S.T).pct_change().dropna()

        port_rets = np.cumprod(np.inner(weights, R) + 1)
    port_returns_all[:, t] = port_rets


# I don't claim that this is elegant code. I'm sure there's a better way to do this via vectorization, without loops. I'll figure it out!
# 
# Let's graph these 50 different portfolio paths to see what our future may hold.

# In[13]:


port_returns_all = pd.DataFrame(port_returns_all)

plt.plot(port_returns_all)
plt.ylabel('Portfolio Returns')
plt.xlabel('Days')
plt.title('Simulated Portfolio Returns in 30 days')


# That's a large spread of possible cumulative portfolio returns over the year! This type of simulation is potentially useful for financial planners, and let's you "answer" questions like, "What's the probability that my portfolio falls below a particular level over the next decade?". You can also use price paths like this to price certain options, where the value of the option depends on the paths that a basket of stocks took. 
