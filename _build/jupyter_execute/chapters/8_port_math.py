#!/usr/bin/env python
# coding: utf-8

# # Essential portfolio math
# 
# This brief chapter will cover the type of statistics that we often see when looking at **portfolios**. Much of this material is covered in various DataCamp exercises. Pieces, such as skewness and kurtosis, are also covered in **Chapter 13 of our textbook**. 
# 
# This material will have us thinking about **portfolio construction**.
# 
# What is **portfolio construction**? Choosing and sizing the various trades to achieve a good trade-off between risk and expected return.
# 
# 1. Diversification
# 2. Position limits and risk limits: 
#   - At the level of securities, asset classes, and overall portfolio. 
# 3. Larger bets on higher conviction trade.
# 4. Size bets in terms of risk
# 5. Correlations matter
#   - For a long position, correlation with other longs is bad, corr. with shorts is good
#   - Powerful to go long/short within each industry, diversify across industries
#   - Can use ETFs and futures to “hedge” out sector and market exposure
# 6. Resize positions according to forward-looking risk and conviction
# 
# We'll start by bringing in some **monthly hedge fund return data**. We'll calculate some portfolio returns, using assumed weights. We'll then move on to portfolio-level **variance and standard deviation**. We'll see how to **annualize returns and volatility**. We'll look at other risk measures, like **skewness** and **kurtosis**. We'll see **Sharpe** and **Sortino** ratios. Finally, we'll make a graph for the max drawdown of our strategy.
# 
# These ideas will get us thinking about portfolios, trading strategies, risk management, and portfolio optimization.
# 
# The formulas are **must knows** for finance folks! For example, you need these on CFA Level 1.
# 

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import janitor
from janitor import clean_names

hf = pd.read_excel('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/hf_rets.xlsx',
                  index_col=0, parse_dates=True)  

hf = hf.clean_names()

hf.describe()


# There's a lot there, so let's just keep four different columns. These columns represent the average monthly return for that hedge fund type. I'm keeping long/short equity, equity market neutral, global macro, managed futures.
# 
# Long/short equity funds do what that says - they go long and short stocks, generally keeping their market beta less than one. Equity market neutral might aim for a beta of zero, but usually have more exposure than that. They are trying to get rid of their risk exposures and just earn alpha from security mispricings. Global macro funds make trades based on broad market trends, currencies, and other markets affected by macro events, like inflation or economic growth. They don't buy or sell individual securities and often use futures contracts to get their exposures. Finally, managed futures are similar, but tend to follow trend-following strategies. 
# 
# You'll see more on these ideas in the factor model notes.

# In[2]:


rets = hf.iloc[:,[5, 6, 8, 9]]
rets


# ## Portfolio-level returns
# 
# Let's define an array of weights. We'll put 25% of our money into each style category. This isn't actually an investable strategy, since you can't invest in the average long/short equity fund!

# In[3]:


wgts = np.array([0.25, 0.25, 0.25, 0.25])


# We can find the monthly means for each strategy.

# In[4]:


monthy_rets_avg = rets.mean()
monthy_rets_avg


# We can also see what our equally-weighted portfolio would have done per month over that time period.

# In[5]:


hf_port_ret = np.sum(monthy_rets_avg*wgts)
hf_port_ret


# Let's weight each month's returns by our weights so that we can then calculate monthly portfolio returns.

# In[6]:


weighted_returns = (wgts * rets)


# I'm calculating monthly returns by summing up across each row. That's the `axis=1` argument. I'm then naming this series *port_ret*.

# In[7]:


port_ret = weighted_returns.sum(axis=1).rename('port_ret')


# I'll join my portfolio returns to the monthly fund returns. There should be the same number of portfolio returns as individual hedge fund returns.

# In[8]:


rets_with_port = rets.join(port_ret)


# And, I can calculate cumulative returns and then graph them. 

# In[9]:


monthly_cum_rets=(1+rets_with_port).cumprod()


# In[10]:


monthly_cum_rets.plot()
 


# Yikes! Check out the orange line - equity market neutral funds aren't necessarily very market neutral!

# ## Risk measures at the portfolio-level
# 
# As you know from your investments class, the variance of a portfolio is **not** the average variance of the assets in the portfolio. We need to take into account the effects of **diversification**. For example, here's the formula for the variance of a portfolio with two assets. We need weights, variances, and the covariance between the two.
# 
# \begin{align}
# \sigma^2_p = w^2_1 \sigma^2_1 + w^2_2 \sigma^2_2 + 2 w_1 w_2 \sigma^2_{1,2}
# \end{align}
# 
# $\sigma^2_{1,2}$ is the **covariance** between the two assets. 
# 
# This formula generalizes for **any number of assets**. 
# 
# \begin{align}
# \sigma^2_p = w^T \Sigma w
# \end{align}
# 
# where $w$ is a **vector** containing all of our portfolio weights and $\Sigma$ is the variance-covariance matrix for our assets. The "T" means the matrix operation **transpose**. This is necessary for the matrix multiplication. 
# 
# Let's use Python to find the variance-covariance matrix. There are variances along with diagonal of the matrix and covariance terms **between assets** in the off-diagonals. Note that upper-right and lower-left of the matrix are identical. This is because the covariance between Asset 1 and Asset 2 is the same as the covariance between Asset 2 and Asset 1. 

# In[11]:


cov_matrix = rets.cov()
cov_matrix


# Let's use our general formula, our weights, and the cov matrix to find **portfolio variance**. We'll use `np.dot()` from `numpy` to do the dot product. This is like **mmult** in Excel. The `.T` transposes, or flips, the vector of returns so that we can multiply. 

# In[12]:


port_variance = np.dot(wgts.T, np.dot(cov_matrix, wgts))
port_variance


# Here's a [refresher on matrix multiplication](https://www.mathsisfun.com/algebra/matrix-multiplying.html) in case you need it.

# Portfolio standard deviation is, of course, just the square root of variance. We can use `np.sqrt()`. 

# In[13]:


port_stddev = np.sqrt(np.dot(wgts.T, np.dot(cov_matrix, wgts)))
print(str(np.round(port_stddev, 3) * 100) + '%')


# ## Skewness and kurtosis
# 
# We'll look more at the distribution of asset returns when we get to a more formal treatment of risk management. But, for now, we need to know that asset returns, like stocks, and even portfolio returns, like those of a hedge fund, are not typically normally distributed. They "lean", or have **skewness**. That skewness can be either positive or negative, depending on the strategy. They also have **kurtosis**, or "fat tails". This means that there are more extreme returns than you would expect if they followed a normal distribution.
# 
# It is easy to find both in Python.

# In[14]:


rets_with_port.skew()


# In[15]:


rets_with_port.kurt()

