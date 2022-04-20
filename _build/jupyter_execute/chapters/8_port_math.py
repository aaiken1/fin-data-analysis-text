#!/usr/bin/env python
# coding: utf-8

# # Essential portfolio math
# 
# This brief chapter will cover the type of statistics that we often see when looking at **portfolios**. Much of this material is covered in various DataCamp exercises. Parts of the material, such as skewness and kurtosis, are also covered in **Chapter 13 of our textbook**. 
# 
# This material will have us thinking about **portfolio construction**.
# 
# What is **portfolio construction**? Choosing and sizing the various trades (or, assets, more generally) to achieve a good trade-off between risk and expected return.
# 
# 1. Diversification
# 2. Position limits and risk limits: At the level of securities, asset classes, and overall portfolio. 
# 3. Larger bets on higher conviction trade.
# 4. Size bets in terms of risk
# 5. Correlations matter: For a long position, correlation with other longs is bad, corr. with shorts is good. Powerful to go long/short within each industry, diversify across industries. Can use ETFs and futures to “hedge” out sector and market exposure.
# 6. Resize positions according to forward-looking risk and conviction
# 
# We'll start by bringing in some **monthly hedge fund return data**. We'll calculate some portfolio returns, using assumed weights. We'll then move on to portfolio-level **variance and standard deviation**. We'll see how to **annualize returns and volatility**. We'll look at other risk measures, like **skewness** and **kurtosis**. We'll see **Sharpe** and **Sortino** ratios. Finally, we'll make a graph showing the **drawdown**, or worse loss, of our portfolio.
# 
# These ideas will get us thinking about portfolios, trading strategies, risk management, and portfolio optimization. We'll go into more detail in later chapters.
# 
# The formulas are **must knows** for finance folks! For example, you need these on CFA Level 1.
# 

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import janitor
from janitor import clean_names

# This brings in all of matplotlib
import matplotlib as mpl 

# This lets us refer to the pyplot part of matplot lib more easily. Just use plt!
import matplotlib.pyplot as plt

hf = pd.read_excel('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/hf_rets.xlsx',
                  index_col=0, parse_dates=True)  

hf = hf.clean_names()

hf.describe()


# There's a lot there, so let's just keep four different columns. These columns represent the average monthly return for that hedge fund type. I'm keeping long/short equity, equity market neutral, global macro, managed futures.
# 
# Long/short equity funds do what the name says -- they go long and short stocks, generally keeping their market beta less than one. But not that different from traditional mutual funds.
# 
# Equity market neutral might aim for a beta of zero, but usually have more exposure than that. They are trying to get rid of their risk exposures and just earn alpha from security mispricings. Easier said than done.
# 
# Global macro funds make trades based on broad market trends, currencies, and other markets affected by macro events, like inflation or economic growth. They don't buy or sell individual stocks and often use futures contracts to get their exposures. 
# 
# Finally, managed futures are similar, but tend to follow trend-following strategies. They buy stuff that's been going up and sell stuff that's been going down. Some investors use them as diversifiers in their portfolios.
# 
# You'll see more on these ideas in the factor model notes.

# In[2]:


rets = hf.iloc[:,[5, 6, 8, 9]]
rets


# I used `.iloc` to keep the columns I wanted. Easier to use a column number reference than type out these long names.

# ## Geometric vs. arithmetic averages
# 
# In order to think about portfolio returns, we also need to understand the relationship between an arithmetic average and the geometric average, and when to use one vs. another.
# 
# This article, [by the financial planner Michael Kitches](https://www.kitces.com/blog/volatility-drag-variance-drain-mean-arithmetic-vs-geometric-average-investment-returns/), is a great explanation of why the difference matters and how **volatility drag** affects your total return. From his summary:
# 
# > In the investment world, it’s common to discuss average rates of return, both in a backward-looking fashion (e.g., to report investment results), and in a more forward-looking manner (e.g., to project the average growth rate of investments for funding future goals in retirement planning software). However, the reality is that because returns are linked to each other – the return in one year increases or decreases the available wealth to compound in the subsequent year – it’s not sufficient to simply determine an “average” return by adding up all the historical returns and dividing by how many there are.
# 
# > Instead of this traditional “arithmetic mean” approach to calculating an average, in the case of investment returns, the proper way to calculate average returns is with a geometric mean, that takes into account the compounding effects of a series of volatile returns over time. Which is important, because in practice the geometric average return is never as high as its arithmetic mean counterpart, due to the fact that volatility always produces some level of “volatility drag”, which can be estimated by subtracting ½ of the investment’s variance (standard deviation squared) from its arithmetic return.
# 
# > Fortunately, the reality is that most investment returns, as commonly discussed by financial advisors, are already reported as geometric returns, typically stated as either a Compound Average Growth Rate (CAGR), an annualized return, or some similar label. Which means, intended or not, most financial advisors already project future wealth values in a retirement plan using the (proper) geometric return assumption.
# 
# > However, the variance drain on a sequence of volatile returns still matters when financial advisors use Monte Carlo analysis, which by design actually projects sequences of random volatile returns (based on the probability that they will occur) to determine the outcome of particular retirement strategies. Because the fact that volatility drag is already part of a Monte Carlo analysis means that the return assumption plugged into a Monte Carlo projection should actually be the (higher) arithmetic return, and not the investment’s long-term compound average growth rate. Otherwise, the impact of volatility drag is effectively counted twice, which can understate long-term returns and overstate the actual risk of the prospective retirement plan!
# 
# We can put that reasoning into a simple, but important formula.
# 
# \begin{align}
# \text{Compound Return}_i = E[R_p] - \frac{1}{2}\sigma^2_p
# \end{align}
# 
# where $E[R_i]$ is the arithmetic mean of the portfolio (i.e. the expected return) and $\sigma^2_p$ is the variance of the portfolio. Note that this math works for single assets, too. It isn't portfolio specific.
# 
# ```{hint}
# This is yet another formula that appears on the CFA and CFP exams.
# ```
# 
# Believe it or not, just figuring out how to calculate returns in order to create projections (e.g. for a client portfolio) is a controversial, non-trivial task. Two of the authors of your FIN 4120 investments textbook suggest that you should forecast the value of a portfolio using an average [between the arithmetic and geometric](https://www.tandfonline.com/doi/abs/10.2469/faj.v59.n6.2574?src=recsys).

# ## Portfolio-level returns
# 
# Let's define an array of weights. We'll put 25% of our money into each style category. This isn't actually an investable strategy, since you can't invest in the average hedge fund!

# In[3]:


wgts = np.array([0.25, 0.25, 0.25, 0.25])


# We can find the monthly means for each strategy. I'll multiply each by 100, name the column, and then turn the series into a DataFrame. You need the table to be a DataFrame in order to style it. I then use a **dictionary** to change the row names. Remember, a Python dictionary matches one item to another. I finally style the number format.

# In[4]:


monthly_rets_avg = rets.mean().mul(100)

monthly_rets_avg = monthly_rets_avg.rename('Monthly Return')

monthly_rets_avg = monthly_rets_avg.to_frame()

monthly_rets_avg = monthly_rets_avg.rename({'ln_sh_eq_hedge_fund_usd':'L/S Equity','eq_mkt_ntr_hedge_fund_usd':'Equity Market Neutral','global_mac_hedge_fund_usd':'Global Macro','mngd_fut_hedge_fund_usd':'Managed Futures'}, axis='rows')

monthly_rets_avg = monthly_rets_avg.style.format('{:.3f}%').set_caption('Hedge Fund Style Returns') 

monthly_rets_avg


# The **method chaining** to writing the code step-by-step to make the table works too. I find this easier to read. Note that I'm **not** saving the table as a DataFrame anywhere, though I could. I do one action and then the output gets passed on to the next action.

# In[5]:


(
    rets.mean()
    .mul(100)
    .rename('Monthly Return')
    .to_frame()
    .rename({'ln_sh_eq_hedge_fund_usd':'L/S Equity','eq_mkt_ntr_hedge_fund_usd':'Equity Market Neutral','global_mac_hedge_fund_usd':'Global Macro','mngd_fut_hedge_fund_usd':'Managed Futures'}, axis='rows')
    .style
        .format('{:.3f}%')
        .set_caption('Hedge Fund Style Returns')   
)


# We can also see what our equally-weighted portfolio would have done per month over that time period. I'll remake the monthly average returns, since you can't use it for math now that it's been styled.

# In[6]:


monthly_rets_avg = rets.mean()
hf_port_ret = np.sum(monthly_rets_avg * wgts)
hf_port_ret


# Let's weight each month's returns by our weights so that we can then calculate monthly portfolio returns.

# In[7]:


weighted_returns = (wgts * rets)


# I'm calculating monthly returns by summing up across each row. That's the `axis=1` argument. I'm then naming this series *port_ret*.

# In[8]:


port_ret = weighted_returns.sum(axis=1).rename('port_ret')


# I'll join my portfolio returns to the monthly fund returns. There should be the same number of portfolio returns as individual hedge fund returns.

# In[9]:


rets_with_port = rets.join(port_ret)


# And, I can calculate cumulative returns and then graph them. As we've seen using a function like `.cumprod()` like this is an example of **broadcasting** and **vectorization**. I am adding 1 to every monthly return and then applying the `.cumprod()` function to each observation. Take a look at the result to see what happened. 
# 
# I'll also rename the columns a slightly different way. Notice that I'm using `inplace=True` and have the column names inside of a **dictionary**. 

# In[10]:


monthly_cum_rets = (1+rets_with_port).cumprod()
monthly_cum_rets.rename(columns={'ln_sh_eq_hedge_fund_usd':'L/S Equity', 'eq_mkt_ntr_hedge_fund_usd':'Equity Market Neutral', 'global_mac_hedge_fund_usd':'Global Macro', 'mngd_fut_hedge_fund_usd':'Managed Futures', 'port_ret':'EW Port Ret' }, inplace=True)


# In[11]:


monthly_cum_rets.plot();


# Yikes! Check out the orange line - equity market neutral funds aren't necessarily very market neutral!

# ## Risk measures at the portfolio-level
# 
# As you know from your investments class, the variance of a portfolio is **not** the average variance of the assets in the portfolio. We need to take into account the effects of **diversification**. For example, here's the formula for the variance of a portfolio with two assets. We need weights, variances, and the covariance between the two.
# 
# \begin{align}
# \sigma^2_p = w^2_1 \sigma^2_1 + w^2_2 \sigma^2_2 + 2 w_1 w_2 \sigma^2_{1,2}
# \end{align}
# 
# That last sigma, $\sigma^2_{1,2}$, is the **covariance** between the two assets. 
# 
# This formula generalizes for **any number of assets**. 
# 
# \begin{align}
# \sigma^2_p = w^T \Sigma w
# \end{align}
# 
# where $w$ is a **vector** containing all of our portfolio weights and sigma is the variance-covariance matrix for our assets. The "T" means the matrix operation **transpose**. This is necessary for the matrix multiplication. 
# 
# Let's use Python to find the variance-covariance matrix. There are variances along with diagonal of the matrix and covariance terms **between assets** in the off-diagonals. Note that upper-right and lower-left of the matrix are identical. This is because the covariance between Asset 1 and Asset 2 is the same as the covariance between Asset 2 and Asset 1. 

# In[12]:


cov_matrix = rets.cov()
cov_matrix


# We can also find the correlation matrix. Correlation ($\rho$) is the **covariance between two assets divided by the standard deviation of each asset multiplied together**: $\rho_{1,2} = \frac{\sigma_{1,2}}{\sigma_1 \sigma_2}$

# In[13]:


corr_matrix = rets.corr()
corr_matrix


# The correlation among these general strategies is pretty low! That's good for portfolio formation. In fact, strategies like managed futures are often considered a diversifier in a traditional equity and bond portfolio. 
# 
# Let's use our general formula, our weights, and the cov matrix to find **portfolio variance**. We'll use `np.dot()` from `numpy` to do the dot product. This is like **mmult** in Excel. The `.T` transposes, or flips, the vector of returns so that we can multiply. 

# In[14]:


port_variance = np.dot(wgts.T, np.dot(cov_matrix, wgts))
port_variance


# Here's a [refresher on matrix multiplication](https://www.mathsisfun.com/algebra/matrix-multiplying.html) in case you need it.

# Portfolio standard deviation is, of course, just the square root of variance. We can use `np.sqrt()`. 

# In[15]:


port_stddev = np.sqrt(np.dot(wgts.T, np.dot(cov_matrix, wgts)))
print(str(np.round(port_stddev, 3) * 100) + '%')


# ## Skewness and kurtosis
# 
# We'll look more at the distribution of asset returns when we get to a more formal treatment of risk management. But, for now, we need to know that asset returns, like stocks, and even portfolio returns, like those of a hedge fund, are not typically normally distributed. They "lean", or have **skewness**. That skewness can be either positive or negative, depending on the strategy. They also have **kurtosis**, or "fat tails". This means that there are more extreme returns than you would expect if they followed a normal distribution.
# 
# It is easy to find both in Python.

# In[16]:


rets_with_port.skew()


# It's easier to see what skewness and kurtosis mean with pictures.
# 
# ```{figure} ../images/08-skew.png
# ---
# name: 08-skew.png
# align: center
# ---
# Some strategies, like selling options, have negative skewness. You make a small profit much of the time -- until you don't. Other investments have positive skewness. You'll lose money much of the time, but occasionally get a large payoff. Some volatility-protection strategies look like this. Source: DataCamp.
# ```

# In[17]:


rets_with_port.kurt()


# ```{figure} ../images/08-kurt.png
# ---
# name: 08-kurt.png
# align: center
# ---
# Many investment strategies have more "rare events" or larger gains and losses than you would expect if returns followed the normal distribution. Source: DataCamp.
# ```

# ## Annualizing and adjusting for risk
# 
# There are many ways to report returns. We've seen discrete vs. log returns. There are returns for specific period, like a day or a month. We can then take that specific period return and **annualize** it. This takes a return over a shorter time frame and asks what are return would be if we earned that return over a year.
# 
# We can also annualize a multi-year return and ask what annual return would have gotten us the same multi-year return.
# 
# Both of these ideas are really the same thing mathematically and take into account **compounding**. They let us compare returns that are different time periods. Fund managers that fall under the SEC '40 Act are required to report calculations like this.
# 
# There are also many ways to **adjust for risk**. Why do we need to adjust for risk? Simply put, you can go to a casino and put all of your money on black, get lucky, and double your "investment". But I don't want you managing my money! Your risk-adjusted return is zero. 
# 
# The same thing is true for trading securities, like stocks, bonds, options, and crypto. You can buy a penny stock, or a Dog coin, or a deep out-of-the-money call option and make a lot of money. And that money is real - you can spend it! But, we need ways to disentangle return, risk, and luck if we're going to assign skill to someone's good forture. 
# 
# Let's combine these two ideas, getting our return and risk measures in the same time units and taking risk into account, to calculate to basic risk-adjustment measures: the **Sharpe Ratio** and the **Sortino Ratio**.
# 
# We'll look at **factor models** in another chapter. This is a more comprehensive way to adjust our returns for the risks that we're taking in order to see if we have skill. 
# 
# Let's use the monthly portfolio returns that I created above to find our measures of risk/return trade-off. I will first annualize my monthly return. I will then annualize my monthly standard deviation, or volatility as we say in finance. I am "cheating" a bit on my volatility annualization. These are discrete returns. Multiplying by the square root of the number of your time periods in a year (12, because we have montly returns) really only works if you have log returns.
# 
# See the DataCamp assignment and your Principles of Finance notes for more on these calculations.

# In[18]:


risk_free = 0.02
 
port_ret = rets_with_port.port_ret
port_ret.describe()


# In[19]:


annualized_return=((1 + port_ret.mean())**(12))-1
annualized_vol = port_ret.std()*np.sqrt(12)


# Note that `**` denotes exponent, while `*` is multiplication in Python. 
# 
# We can then calculate the **Sharpe Ratio**, which is the ratio of returns above the risk-free rate to the volatility (i.e. the risk) in the portfolio.

# In[20]:


sharpe_ratio = (annualized_return - risk_free) / annualized_vol
sharpe_ratio


# We have a Sharpe near 1. That's pretty high! Hedge fund strategies often take risks that are not well-defined by standard deviation. For example, if a strategy has a lot of negative skewness, then we would expect to occasionally have large losses. Volatility doesn't capture that type of risk.
# 
# Returns that are "too smooth" can also create artificially low Sharpe Ratios. For example, if a strategy holds illiquid securities that are not marked-to-market (or priced) consistently, then the reported returns won't affect the actual volatility of the positions if they were priced, say, daily. For example, many venture capital and private equity strategies only mark, or change the prices of their investments, quarterly. A mutual fund is going to see their positions market daily. ETFs trade throughout the day. Private equity strategies look less volatile than they really are and, so, have higher Sharpe ratios than they do in reality. 

# We can also calculate the **Sortino Ratio**. This looks very similar to the Sharpe Ratio, expect that we only calculate the standard deviation using returns below some target, or threshold. So, we are interesting in volatility during bad times, not just overall volatility. We often use a target of 0 to look at negative returns, but you can choose something else if that's appropriate.
# 
# Note that I am masking with `.loc` to get just the negative returns from the *port_ret* Series.

# In[21]:


target_return = 0

negative_returns = port_ret.loc[port_ret < target_return]

down_stdev = negative_returns.std()*np.sqrt(12)

sortino_ratio = (annualized_return - risk_free)/down_stdev

sortino_ratio


# ## Drawdowns
# 
# We might also be interested in draw-downs, or what the bad times look like, how long they last, and how long it takes to get our money back.
# 
# We will calculate the cumulative portfolio return, the previous maximum cumulative return (often called a **high water mark**), and the percentage below the high water mark at any point. 
# 
# I print my index, just to show you that *date* is the index of the *port_drawdown* DataFrame. So, my x-axis in my plots can just be `port_drawdown.index`. 
# 
# I am using `matplotlib` and `plt.plot` to make two stacked line charts. I find this to be the easiest way, even if it is more verbose. You can really see what you're doing in each step.

# In[22]:


port_ret_cum = (1+port_ret).cumprod()
previous_peaks = port_ret_cum.cummax()
drawdowns = (port_ret_cum - previous_peaks)/previous_peaks

port_drawdown = pd.DataFrame({'Cumulative Return': port_ret_cum, 'Previous Peak': previous_peaks, 'Drawdown': drawdowns})

print(port_drawdown.index)


# Let's make the graph. You'll see that the Great Financial Crisis was the high water mark, at least in this data.

# In[23]:


plt.figure(figsize=(10, 6))

plt.subplot(211)
plt.plot(port_drawdown.index, port_drawdown['Cumulative Return'], lw=1.5, label='Cumulative Portfolio Returns')
plt.plot(port_drawdown.index, port_drawdown['Previous Peak'], lw=1.5, label='Previous High Water Mark')
plt.legend(loc=0)
plt.ylabel('Cumulative Returns')
plt.title('Hedge Fund Portfolio Drawdowns')

plt.subplot(212)
plt.plot(port_drawdown.index, port_drawdown['Drawdown'], lw=1.5, label='Drawdown')
plt.legend(loc=0)
plt.xlabel('Date')
plt.ylabel('Return');

