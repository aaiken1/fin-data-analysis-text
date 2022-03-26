#!/usr/bin/env python
# coding: utf-8

# # Portfolio optimization
# 
# Portfolio optimization is an important part of many quantitative strategies. You take some inputs related to risk and return and you try to find the portfolio with the desired characteristics. Those characteristics might be something like the best risk-reward trade-off, often given with a Sharpe Ratio. Or, you might be trying to find a portfolio with a particular expected return and the lowest possible risk to get that return. 
# 
# We'll start with the example of portfolio optimization using `scipy.optimize`, very similar to the code found in Chapter 13 of our textbook. This is very much like using **Solver in Excel**. You are having Python numerically solve an optimization problem with some set of constraints or limits on the answer. This means that Python will try to guess values until it gets really, really close to the "best" possible solution.
# 
# We are also going to see some interesting Python. We'll use **tuples**, a basic (primitive) data type in Python. We have **for** loops. We'll **define our own functions**. We'll even use something called a **lambda function**. 
# 
# Finally, we'll use the `PyPortfolioOpt` [package](https://pypi.org/project/pyportfolioopt/), which is also discussed in the DataCamp assignments. This lets us avoid some of the more math-like aspects of using `scipy.optimize` and have a library do the work for us using more familiar finance terms. Still, I think it is really important to understand at least a little bit about the optimization process itself. These tools are used in all sorts of applications.
# 

# ## Getting started
# Let's bring in our usual set of prices, pick four assets, calculate **discrete** returns, and plot a histogram of those returns.
# 
# We are going to use **discrete** (or simple, or arithmetic) returns instead of **log** returns, because we are doing **portfolio optimization**. In short, the return of a portfolio is the weighted average of the mean discrete returns. This is not true for mean log returns.

# In[1]:


# Read in some eod prices
import numpy as np
import pandas as pd

from pylab import mpl, plt

import scipy.optimize as sco

raw = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True).dropna() 

symbols = ['AAPL.O', 'MSFT.O', 'SPY', 'GLD'] #two stocks and two ETFs

noa = len(symbols) #noa = number of assets

data = raw[symbols]

rets = data.pct_change().dropna()

rets.hist(bins=40, figsize=(10, 8));


# We can the average daily return of each of these four sets of discrete returns and annualize them. You can annualize daily log returns by multiplying by 252, the number of trading days in a year. You can not do this with discrete returns, or $\frac{P_t}{P_{t-1}} - 1$. Instead, you **compound them and do $(1+dailyaverage)^{252} - 1$.

# In[2]:


(1+rets.mean())**252-1


# In[3]:


ann_rets = (1+rets.mean())**252-1


# Same thing with variance and covariance. We are going to take a short-cut and annualize the daily variances and covariances by multiplying by 252. You would annualize standard deviation by multiplying by $\sqrt{252}$. Technically, you should only do this with log returns.

# In[4]:


rets.cov() * 252


# When you form a portfolio, you of course need to know how much of your portfolio is in each asset. Let's pick some **random weights** to start. We'll do that by choosing random numbers between 0 and 1. How many random numbers? The variable *noa* has the number of assets stored in it, so we'll pick four. Then, we'll divide each random number by the sum of the four numbers. This "trick" let's us go from four numbers between 0 and 1 to four numbers that will add up to 1. Just like portfolio weights!
# 
# Note the `/=`. This divides every item in *weights* by the sum of the weights and then saves the result back to *weights*.

# In[5]:


weights = np.random.random(noa)
weights /= np.sum(weights)


# In[6]:


weights.sum()


# Good! They add up to 1. Or, well, basically 1. Remember, computers try their best to store exact numbers, but there's only so much precision that you can get. 

# In[7]:


np.sum(ann_rets * weights)


# We can also find portfolio variance using the random weights. Again, we're annualizing variances and covariances.

# In[8]:


np.dot(weights.T, np.dot(rets.cov() * 252, weights))


# Finally, we take the square root of variance to get standard deviation. 

# In[9]:


np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))


# Ok, all of this was with random weights. Can we do any better than that, if we assume that our expected returns and variance co-variance matrix represent our best guess about how these assets will behave in the future? Note that his is a really big assumption. The past might not tells us much about the future.

# ## Plotting the efficient frontier
# 
# The efficient frontier represents the relationship between risk and return. Each point on the curve is the best return that you can get for a given level of risk. Or, equivalently, each point is the lowest risk that you can take for a particular expected return. We would expect to see a positive relationship between risk and return. 
# 
# ```{figure} ../images/09-cal.png
# ---
# name: 09-cal.png
# align: center
# ---
# The Capital Allocation Line, or CAL. The mean-variance frontier is the highest return you can get for a given level of risk. The CAL is all possible combinations have the highest Sharpe Ratio portfolio (the tangency portfolio) and the risk-free asset. If all investors have the same beliefs about all underlying assets, then they will all hold the same market portfolio, just in different quantities, depending on their risk preferences. Source: Asset Management by Andrew Ang
# ```
# 
# What if we picked a bunch of random portfolios, found their risk and return, and then plotted each on a scatter plot? We should see the efficient frontier "emerge" as we essentially throw darts, since some risk-return combinations are not possible for a given set of assets. There's only so much return you can get for a given level of risk. 
# 
# To do this, let's define two functions. One just takes weights and finds the portfolio return using the mean returns. The other finds the volatility of the portfolio using the weights passed to it. Note that both are just the formulas used above, but now in a function that we've defined. 
# 
# How do you **read the format of a user defined function**? You use `def` to define the function name. Inside of `()`, you put the items that are getting passed, or given to, the function. In this case, whatever we give the function will be called *weights* inside of the function. What's inside the function. You must end the first line with a `:`. Then, you need to **indent everything that happens when the function is used**. In this case, that's just one line. The function will **return** whatever is on the line with **return**. In this case, the portfolio return and volatility. 

# In[10]:


def port_ret(weights):
    return np.sum(ann_rets * weights)


# In[11]:


def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))


# Here's the main part. We are going to use those two functions above to write some cleaner code. We start by creating two empty arrays, *prets* and *pvols*. We'll then put a bunch of different portfolio mean returns and volatilities into these arrays. How are we going to get these different portfolio risk and return characteristics? Let's create a bunch of random portfolios with random asset weights. In fact, let's create 2500 random portfolios and see what each combination of risk and return looks like when we plot it. The shape should look familiar!

# In[12]:


prets = []
pvols = []
for p in range (2500):  
    weights = np.random.random(noa)  
    weights /= np.sum(weights)  
    prets.append(port_ret(weights))  
    pvols.append(port_vol(weights))  
prets = np.array(prets)
pvols = np.array(pvols)


# The **for** statement will have the value *p* go from 0 to 2499 (i.e. 2500 times). For each of these times through the loop, we calculate our random weights and the portfolio returns and volatility for these weights, using the same expected returns and volatility for the assets each time through. Only the weights are changing. We then **append**, or stack, the return and volatility values on top of each other, creating two **lists** with 2500 numbers in them. But, we don't want a list. We want an **array** of numbers. The last two lines convert the lists into `numpy` arrays which we can graph.
# 
# Let's graph them. We'll make a **scatter plot** with volatility on the x-axis and returns on the y-axis. The `c=` option adds a third dimension to the graph, where we pick a color for each dot based on another value. That value is the return for that dot divided by the volatility of that dot. In other words, darker red means bigger return over risk ratio, or larger **Sharpe Ratio**. Notice how the dark red is along the edge of the curve? This is the **efficient frontier**! 

# In[13]:


plt.figure(figsize=(10, 6))
plt.scatter(pvols, prets, c=prets / pvols,
            marker='o', cmap='coolwarm')
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio');


# We've just generated the **efficient frontier** from a simulation. No "formulas", per se. Just make 2500 random portfolios and at least some of them are going to be good!
# 
# Each portfolio on the **envelope**, the edge of the shape we see above, is on the efficient frontier. Each of these portfolios has the highest return for a given level of risk (or the lowest risk for a given return). 
# 
# We'll draw the efficient frontier below. 

# ## Optimizing
# 
# Let's use an **optimizer** actually find the portfolio with the best Sharpe Ratio. This will be, for a given risk-free rate, the single portfolio with the best risk-reward trade-off. 
# 
# We'll also find the portfolio with the lower volatility (risk). This portfolio is sometimes called the **minimum variance portfolio**.
# 
# We will assume in this example that the risk-free rate is zero. We are not subtracting the risk-free rate from the portfolio return in the numerator. Note that as you change the risk-free rate, then you get different maximum Sharpe Ratio portfolios. What you're doing, graphically, is **tracing** out the efficient frontier, finding different porfolios that are on the envelope. 

# We'll start by defining a new function. This is our **Sharpe Ratio**. The optimization process that we're going to use wants to find the **minimum** of something. So, we'll make the Sharpe Ratio negative. This will then be the equivalent of finding the **maximum. 

# In[14]:


def min_func_sharpe(weights):  
    return -port_ret(weights) / port_vol(weights)  


# That's the function that we are going to **minimize**. We are going to have Python find the weights that make that function as small as possible. Again, since the function has a negative sign in front, this is like finding the maximum. 
# 
# Portfolio optimization always has a **constraint** where your weights must add up to one. To add this constraint, we are now going to set up a **dictionary** that our optimizer is going to be able to understand. The dictionary will say that we are going to give the optimizer something that is type `eq`, or an equation, and that the equation is the sum of all of our weights minus 1. The optimizer is going to know that we want this to be set equal to zero when solving for weights. In other words, all of our weights must add up to one - we are forcing the optimizer to to this.
# 
# By the way, see the `lambda x:`? This is a **lambda**, or anonymous, function. These let us quickly and easily define a simple function. In this case, we have a function that is going to take an argument *x* and then do something with it. We are adding up all of the elements of *x* and then subtracting one. When we use this function, *x* will be our weights.

# In[15]:


cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})  
type(cons)


# We can now put some bounds on our weights. Weights, in this case, need to be between 0 and 1. This isn't always the case! For example, short-selling means having weights less than 0. Leverage means weights greater than 1, potentially. To do this, we'll create a **tuple** that has the set (0,1) for each asset in our portfolio, four in this case. This will tell the optimizer to keep each asset weight between 0 and 1.

# In[16]:


bnds = tuple((0, 1) for x in range(noa))  
bnds


# We'll start by giving the optimizer an equally-weighted portfolio. It will change these weights to find the ones that minimize that negative Sharpe Ratio.

# In[17]:


eweights = np.array(noa * [1. / noa,])  
eweights  


# Here's the negative Sharpe Ratio with the equal-weights. So, the "real" Sharpe is 0.8436.

# In[18]:


min_func_sharpe(eweights)


# Finally, let's use the optimizer! We are going to use `sco.minimize` from the library `SciPy`, which we have brought in above. This function is like **Solver in Excel**. It is going to find the minimum value of some function by changing a set of variables in the function, subject to some constraints. The first argument is the function to minimize. The second argument is the initial guess. Then, we give it the method to use to find the minimum value. We're using something called Sequential Least Squares Programming (SLSQP) here. Not important for us. We then give the optimizer our bounds for the variables and the constraints.
# 
# You can read more about this function in the `SciPy` manual (here)[https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html]. 

# In[19]:


opts = sco.minimize(min_func_sharpe, eweights,
                    method='SLSQP', bounds=bnds,
                    constraints=cons) 
type(opts)


# We've saved the results in this OptimizeResult **object**. This object contains information about our optimization, including the optimal values it found. It calls these *x* - they are our weights that give us the minimum negative (i.e. maximum) Sharpe Ratio.

# In[20]:


opts


# Let's pull out just the weights from the object and round to three decimal palces.

# In[21]:


opts['x'].round(3)  


# Here's the portfolio return with those weights.

# In[22]:


port_ret(opts['x']).round(3)  


# And the portfolio volatility with those weights.

# In[23]:


port_vol(opts['x']).round(3)  


# And, the Sharpe Ratio with those weights.

# In[24]:


port_ret(opts['x']) / port_vol(opts['x'])  


# We can do the same things and find the set of weights that **minimize portfolio variance**. 

# In[25]:


optv = sco.minimize(port_vol, eweights,
                    method='SLSQP', bounds=bnds,
                    constraints=cons)  


# In[26]:


optv


# In[27]:


optv['x'].round(3)


# Nothing in our first asset, Apple. Since we are just minimizing variance, we don't care about Apple's nice return over this period. 

# In[28]:


port_vol(optv['x']).round(3)


# In[29]:


port_ret(optv['x']).round(3)


# In[30]:


port_ret(optv['x']) / port_vol(optv['x'])


# ## Efficient Frontier

# Let's now trace out the actual **efficient frontier**. We are going to follow an "algorithm", so to speak. Here are the steps:
# 
# 1) Pick a target return.
# 2) Find the portfolio that gives you the minimum portfolio standard deviation (volatility) for that target return.
# 3) Repeat this process for a large number of target returns.

# These steps will find a bunch of different portfolios, all that live on the envelope of the set containing all of the possible portfolios. These are the portfolios on the efficient frontier. 
# 
# To do this, we now need two constraints. First, we want our portfolio return to be equal to some target return, *tret*. Second, we again have our weights must sum to one constraint.
# 
# Both of these constraints can live inside of the *cons* tuple. This **tuple** contains two **dictionaries**. Kind of confusing, but we just need to understand the syntax for writing out different constraints.

# In[31]:


cons = ({'type': 'eq', 'fun': lambda x:  port_ret(x) - tret},
        {'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})  
type(cons)


# Our bounds again, same as before.

# In[32]:


bnds = tuple((0, 1) for x in weights)


# Let's create an **array** of values from 0.05 to 0.20. This represents a minimum of a 5% return and a maximum of a 20% return. We'll do 50 evenly-spaced values. Each one of these represents one target return. We are going to find and store the minimum volatility that gives us each return.

# In[33]:


trets = np.linspace(0.05, 0.2, 50)
print(type(trets))
trets


# And here's the optimization process. We start with an empty array that will eventually contain 50 different volatilities (standard deviations). Then, we loop through each target return in *trets*. Each one gets stored in *tret* and used in the For loop. The optimizer uses that target return as part of the constraint function that we included. We are then storing the value of the minimized portfolio volatility function in *tvols*. Note that we are not storing the weights for each portfolio. We only care about the minimum volatilities for each return.

# In[34]:


get_ipython().run_cell_magic('time', '', "tvols = []\nfor tret in trets:\n    res = sco.minimize(port_vol, eweights, method='SLSQP',\n                       bounds=bnds, constraints=cons)  \n    tvols.append(res['fun'])\ntvols = np.array(tvols)")


# And now we can plot our efficient frontier. The efficient frontier is each **target return, minimum volatility pair**. That blue line is the frontier and is being added by the first `plt.plot` statement. The second `plt.plot` adds the yellow star at the max Sharpe Ratio portfolio. The third `plt.plot` adds the red star at the global minimum variance portfolio. Notice how both of these are pulling the weights, *x*, out of their respective Optimizer objects. 

# In[35]:


plt.figure(figsize=(10, 6))
plt.scatter(pvols, prets, c=prets / pvols,
            marker='.', alpha=0.8, cmap='coolwarm')
plt.plot(tvols, trets, 'b', lw=4.0)
plt.plot(port_vol(opts['x']), port_ret(opts['x']),
         'y*', markersize=15.0)
plt.plot(port_vol(optv['x']), port_ret(optv['x']),
         'r*', markersize=15.0)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio');


# ## PyPortfolioOpt
# 
# To get started, you'll need to type `pip install PyPortfolioOpt` in your Terminal below. This will install the package, since it doesn't come with Anaconda. We can then bring in what we need.
# 
# You can read all about the `PyPortfolioOpt` package [here](https://pypi.org/project/pyportfolioopt/).

# In[36]:


from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


# We can find expected returns and the sample variance-covariance matrix using functions from `PyPortfolioOpt`. Notice that these functions want prices, not returns. So, I'm using the DataFrame *data*, not *ret*. 
# 

# In[37]:


mu = expected_returns.mean_historical_return(data)
mu


# In[38]:


S = risk_models.sample_cov(data)
S


# Let's find our max Sharpe portfolio.

# In[39]:


# Optimize for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
raw_weights = ef.max_sharpe(risk_free_rate = 0.025)
cleaned_weights = ef.clean_weights()
print(cleaned_weights)
ef.portfolio_performance(verbose=True, risk_free_rate = 0.025)


# In[40]:


ef = EfficientFrontier(mu, S, weight_bounds=(-0.2, 0.5))
raw_weights = ef.max_sharpe(risk_free_rate = 0.025)
cleaned_weights = ef.clean_weights()
print(cleaned_weights)
ef.portfolio_performance(verbose=True, risk_free_rate = 0.025)

