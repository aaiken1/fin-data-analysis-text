#!/usr/bin/env python
# coding: utf-8

# # Financial time series <a id='financial-time-series'></a>
# 
# Python and, in particular, `pandas` can easily deal with the most common type of financial data - **time series data**. We are going to look at the basics of using price and return data. This section follows Chapter 8 of our textbook and the fourth DataCamp assignment that discusses `pandas` time series.
# 
# Time series data means handling dates. There is a [DataCamp tutorial on datetime objects](https://www.datacamp.com/community/tutorials/python-datetime). 
# 
# We'll start with the usual sort of set-up and our familiar stock data. Our data is going to have a particular set-up in this section. Each column is going to represent both a security and something about that security. So, Apple's price. Or, Apple's return. This is a very common way to see financial data, but it is not the only way that this data can be organized.
# 
# 
# 
# ## Chapter Eight Highlights
# 
# | Topic         | Pages  |
# | :-------------------------------------------------------------------------------------- | :--------- | 
# | **Importing data and summary statistics**. We've seen most of this before. The new part is the looking at changes over time, which means **return calculations**.      | 205 - 215      | 
# | **Resampling**. Resampling is changing the periodicity of the data (i.e. going from daily to monthly to annual) | 215 - 217    | 
# | **Rolling statistics**. We often want to find moving averages and other statistics over rolling windows (e.g. one month of trading days). Our textbook gives us an example of technical analysis using rolling calculations. | 217 - 222     | 
# | **High-frequency data**. Tick-by-tick trade data. We won't deal too much with this. It's a whole topic by itself. | 228 - 230     | 
# 
# 

# ## Set-up and descriptives

# In[1]:


# Set-up

import numpy as np
import pandas as pd

# Date functionality
from datetime import datetime
from datetime import timedelta

import janitor
from janitor import clean_names

# all of matplotlib
import matplotlib as mpl 

# refer to the pyplot part of matplot lib more easily. Just use plt!
import matplotlib.pyplot as plt

# importing the style package
from matplotlib import style
from matplotlib.ticker import StrMethodFormatter

# generating random numbers
from numpy.random import normal, seed
from scipy.stats import norm

# seaborn
import seaborn as sns

# Keeps warnings from cluttering up our notebook. 
import warnings
warnings.filterwarnings('ignore')

# Some plot options that will apply to the whole workbook
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'


# Read in some eod prices
stocks = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True)  

stocks.dropna(inplace=True)  

stocks = clean_names(stocks)

stocks.info()


# We are using `pandas` DataFrames, which have many built-in ways to deal with time series data. We have made our **index** the date. This is important - having the date be our index opens up various date-related methods. 
# 
# Let's use `pandas` plot to make a quick figure of all of the prices over the time period in our data. Remember, `pandas` has its own plotting functions. They are very useful for quick plots like this. Because the date is our index, `pandas` knows to put that on the x-axis, right where we want it.

# In[2]:


stocks.plot(figsize=(10, 12), subplots=True);  


# We can use `.describe()` to look at our prices.

# In[3]:


stocks.describe().round(2) 


# We can use `.aggregate()` to create our own set of descriptives. 

# In[4]:


stocks.aggregate([min,  
                np.mean,  
                np.std,  
                np.median,  
                max]  
).round(2)


# ### Dates
# 
# The fourth Datacamp assignment covers some additional date basics. Two libraries are being used here: `datetime` and `pandas`. We can use `pandas` to objects and methods that help us deal with dates. Obviously, we need to handle a variety of time periods in finance.
# 
# We can define a `TimeStamp` and see that they are a particular object-type in Python. **All objects come with methods and attributes.** This is a generic idea from computer science called **object oriented programming**. 

# In[5]:


my_date = pd.Timestamp(datetime(2022, 2, 23))
print(type(my_date))
my_date


# Here's an example of an **attribute** for a `TimeStamp` object. You can also do `.month`, `.day`, `.dayofweek`, etc. 

# In[6]:


my_date.year


# We can add and subtract with dates using `timedelta`. Note that `datetime` no longer wants you to just add or subtract a number from a date.
# 
# There's both a `datetime` `timedelta` and a `pandas` `Timedelta`. You can read about the `pandas` version [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timedelta.html). 

# In[7]:


my_date + timedelta(days=7)


# Using the `pandas` version, just to highlight that different libraries have similar functionality. The `datetime` library and the `pandas` library are different things. But, they can do similar operations with time, even if the syntax varies a bit.

# In[8]:


my_date + pd.Timedelta(7, "d")


# `pandas` has a set of tools related to a **period** in time. You can define a [period](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Period.html), get attributes, and change its frequency. Changing the frequency means changing how `pandas` thinks about the period. Is this month? Is this a particular day?
# 
# Let's define a period as February 2022. 

# In[9]:


period = pd.Period('2022-02')
period


# We can then change that to a daily frequency. Note how, by default, `pandas` puts us at the end of the month. 

# In[10]:


period.asfreq('D')


# This can be really helpful when some Excel data comes in as, say "May-2019" and we want to get that to be an end of month date, like "5/31/19". The actual day is ambiguous when just dealing with month and year.
# 
# With the date as our index, we can pull certain dates and columns. Here's Apple's price on 2017-6-1. 

# In[11]:


stocks.loc['2017-6-1', 'aapl_o']


# Here's all of the columns, but just for a subset of dates.

# In[12]:


stocks.loc['2015-3':'2016-2',:]


# ## Calculating returns
# 
# We can start by just calculating the price change from day-to-day using `pandas` `diff()`. This function is described [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.diff.html). Notice how the first day in the data is now NaN, since you can't calculate a change without the previous day.
# 
# Since there's no `=`, I am not saving the data. Just showing you what the function does.

# In[13]:


stocks.diff().head() 


# Sometimes we want price changes. Other times we want `pandas` `pct_change()`. See [this for more](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pct_change.html). This function allows us to calculate price returns using the percent change. The default is to look back one period, or one day in this case. 

# In[14]:


stocks.pct_change().mul(100).round(3).head()  


# I'm multiplying by 100 just for the display of the data. 
# 
# The percent change is called a **linear return**. Or, **simple return**. This is different from **log returns**, or **compounded returns**. Both types of returns are correct and useful. They are just used for different things.
# 
# The formula for simple returns (R) is:
# 
# \begin{align}
# R_{t} = \frac{V_t}{V_{t-1}} - 1
# \end{align}
# 
# where R is the simple return based on the percent change and V is the cash flow, including price and dividends (if any). 
# 
# The formula for log returns (r) is:
# 
# \begin{align}
# r_{t} = ln(\frac{V_t}{V_{t-1}}) = ln(1 + R_{t})
# \end{align}
# 
# 
# See [this article](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1586656) for more on why this difference is important. In short, we need the mean of simple returns when doing portfolio optimization, as these returns work with a weighted average. Simple returns **aggregate across assets**. Log returns, however, **aggregate across time**. In other words, the cumulative return using log returns is the sum of individual log returns over the time period. You definitely can't do that with simple returns!
# 
# Here's a [brief video](https://www.youtube.com/watch?v=PtoUlt3V0CI) that describes the same thing using Excel.
# 
# Finally, [this chapter](https://faculty.washington.edu/ezivot/econ424/returnCalculations.pdf) has everything you've ever want to know about return calculations. See pgs. 16 and 17 for log returns.
# 
# We can calculate log returns using `np.log` and `.shift()` from `pandas`. Let's look at what `.shift()` does. Compare the following:

# In[15]:


stocks


# In[16]:


stocks.shift(1)


# `stocks.shift(1)` has moved the previous price up one row. You can do a also do `stocks.shift(-1)`, which pulls prices from the next period to the previous one.

# In[17]:


stocks.shift(-1)


# So, by dividing `stocks` by `stocks.shift(1)`, we are dividing today's price by yesterday's price. Note how we are dividing one DataFrame by another, in a sense. This is an example of **vectorization**. No need to loop through all of the columns and rows.

# In[18]:


rets_log = np.log(stocks / stocks.shift(1))  
rets_log


# We can then use the fact that you can sum up log returns over time to get **cumulative**, or **total** log returns. First, you can use the `.cumsum()` function from `pandas` to transform our daily returns into a cumulative sum. In other words, each period is now the sum of all returns in the previous periods.

# In[19]:


rets_log.cumsum()


# If you take the cumulative sum of log returns (R) at any point and do e^R, then you get the value of $1 invested at the beginning. We can use `.apply()` to "apply" the exponential function *e* to each value in the DataFrame. If you want to convert back to the cumulative simple return instead, you can do e^R - 1. 

# In[20]:


rets_log.cumsum().apply(np.exp)


# In[21]:


print(np.exp(1.800839))


# You can then plot the cumulative returns. Notice how we use the `.` to keep sending the DataFrame through to the next step. Take the raw data, do something to it, do something else to that result, and then plot it.

# In[22]:


rets_log.cumsum().apply(np.exp).plot(figsize=(10, 6));  


# We can also create return series using **simple returns**. We calculate percent returns, add 1 to each to get (1+R), and then **chain returns together** using `.cumprod()`. We subtract one at the end from the total.
# 
# In other words,
# 
# \begin{align}
# Total Return = (1 + R_{1})*(1 + R_{2})*(1 + R_{3})*(1 + R_{4})... - 1
# \end{align}
# 

# In[23]:


rets_simple = stocks.pct_change() # period return
rets_simple = rets_simple.add(1)
rets_simple.head()


# In[24]:


rets_simple_cumulative = rets_simple.cumprod().sub(1)
rets_simple_cumulative


# ## Normalizing price series
# 
# You often see charts where all of the assets start at a price of 1 or 100. You can then compare their growth over time. We can easily do this using `pandas`. 
# 
# We can divide all of the prices by the first price in the series, creating **prices relative to that starting point**.
# 
# We can pull the first price for one stock using `.iloc`. 

# In[25]:


stocks.aapl_o.iloc[0]


# We can also pull all of the first prices.

# In[26]:


stocks.iloc[0]


# We can use `.div()` to divide every item in a column by the first item in that column. This is yet another example of vectorization making our lives easier. As the DataCamp assignment notes, `.div()` and other math functions automatically align series and DataFrame columns. So, each price in the first column gets divided by the first price in the first column, etc.

# In[27]:


normalized = stocks.div(stocks.iloc[0]).mul(100)
normalized.plot()


# ## Resampling
# 
# Resampling is when you change the time period that you're looking at. So, you can go from daily to weekly to monthly, etc. This is called **downsampling** and involves aggregating your data.
# 
# You can also do the opposite and go from, say, monthly to daily. The new dates created in your data will be set as NaN. This is called **upsampling** and involves filling in missing data.
# 
# Let's start with `.asfreq` and some basic fill methods. I am going to "create" some quarterly data first for us to work with. I'll discuss how I do this in a minute. 

# In[28]:


stocks_quarterly = stocks.resample('1q', label='right').last()
stocks_quarterly.head()


# Alright, we have some quarterly stock price data now. But, what I want to make this monthly data? Well, I don't have the actual monthly prices in this data set, but I can still **upsample** the data and go from quarterly to monthly.

# In[29]:


stocks_monthly = stocks_quarterly.asfreq('M')
stocks_monthly.head()


# We now have new dates and missing values. We could fill in these missing values like we want. `.asfreq()' has different methods. I'll fill with the previous value, so that April and May get a March value, etc. This is called a **forward fill**. 

# In[30]:


stocks_monthly = stocks_quarterly.asfreq('M', method='ffill')
stocks_monthly.head()


# `pandas` also has a method called `.resample`. This is **a lot** like a `.groupby()`, but dealing with time.
# 
# The code `stocks.resample('1w', label='right')` creates what `pandas` calls a `DatetimeIndexResampler` object. Basically, we are creating "bins" based on the time period we specify. I start with one week and then do one month. The argument `label='right'` tells `.resample()` which bin edge to label the bucket with. So, the first edge (i.e. the first date)
# or the last edge (i.e. the last date). The option *right* means the last edge. For example, the bin will get labeled with the last day of the week. Or the last day of the month. The method `.last()` picks the last member of each time bin. So, we'll get get end-of-week prices or end-of-month prices.
# 
# You can find the documentation [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html). The fourth DataCamp assignment also goes over the details.

# In[31]:


stocks.resample('1w', label='right').last().head()  


# In[32]:


stocks.resample('1m', label='right').last().head()  


# In[33]:


rets_log.cumsum().apply(np.exp).resample('1m', label='right').last(
                          ).plot(figsize=(10, 6));  


# ## Rolling statistics

# Rolling statistics are your usual sorts of statistics, like a mean or standard deviation, but calculated with **rolling time windows**. So, the average price over the past month. Or, the standard deviation of returns of the past year. The value gets updated as you move forward in time - this is the rolling part.
# 
# Let's set a 20 day window and calculate some rolling statistics. There's one you might not know, a kind of moving average called an [exponentially weighted moving average](https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/exponentially-weighted-moving-average-ewma/) (ewma). 

# In[34]:


window = 20  

stocks['aapl_min'] = stocks['aapl_o'].rolling(window=window).min()  
stocks['aapl_mean'] = stocks['aapl_o'].rolling(window=window).mean()  
stocks['aapl_std'] = stocks['aapl_o'].rolling(window=window).std()  
stocks['aapl_max'] = stocks['aapl_o'].rolling(window=window).max()  
stocks['aapl_ewma'] = stocks['aapl_o'].ewm(halflife=0.5, min_periods=window).mean()  


# Let's make a plot using `pandas` `plot`. I'll select four variables and then pick just the last 200 observations using `.iloc`. Notice I don't need to include the index value. This is a line graph, so `.plot()` knows that you want this on the x-axis. I like how `.plot()` automatically styles the x-axis for us too.

# In[35]:


stocks[['aapl_min', 'aapl_mean', 'aapl_max', 'aapl_o']].iloc[-200:].plot(style=['g--', 'r--', 'g--', 'b'], lw=0.8, figsize=(10, 6), title = 'Apple Price with 20-Day Rolling Window Statistics');  


# Now, I'll make the same graph using `matplotlib`. Again, I don't include the index value, as, by default, `matplotlib` will put it on the x-axis. I'm going to put four different line plots on the same axis. I am again selecting just the last 200 rows using `.iloc()`.

# In[36]:


fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(1, 1, 1)

ax.plot(stocks.aapl_min.iloc[-200:], 'g--', lw=0.8)
ax.plot(stocks.aapl_mean.iloc[-200:], 'r--', lw=0.8)
ax.plot(stocks.aapl_max.iloc[-200:], 'g--', lw=0.8)
ax.plot(stocks.aapl_o.iloc[-200:], 'b', lw=0.8)

ax.set_xlabel('Date')
ax.set_ylabel('Apple Price')
ax.set_title('Apple Price with 20-Day Rolling Window Statistics');


# Which way should you make your plots? Basically up to you! There are less verbose ways to do it that the `matplotlib` method I used above. I kind of like seeing each line like that, as it helps me read and understand what's going on. 
# 
# You could also select just the data you want, save it to a new DataFrame, and then plot.

# In[37]:


stocks_last200 = stocks.iloc[-200:]

fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(1, 1, 1)

ax.plot(stocks_last200.aapl_min, 'g--', lw=0.8)
ax.plot(stocks_last200.aapl_mean, 'r--', lw=0.8)
ax.plot(stocks_last200.aapl_max, 'g--', lw=0.8)
ax.plot(stocks_last200.aapl_o, 'b', lw=0.8)

ax.set_xlabel('Date')
ax.set_ylabel('Apple Price')
ax.set_title('Apple Price with 20-Day Rolling Window Statistics');


# ### Simple trend indicator

# One of the best known "anomalies" in finance is that stocks that have been doing better perform better in the future, and vice-versa. This general set of anomalies are called **momentum and trend**. Here's a [summary of momentum and why it might exist](https://www.aqr.com/Insights/Research/White-Papers/Explanations-for-the-Momentum-Premium). The hedge fund Two Sigma has a brief explanation of how [trend and momentum](https://www.venn.twosigma.com/vennsights/momentum-and-trend-following) are different. And a more [academic explanation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463). 
# 
# We can calculate basic moving averages that might capture the spirit of **trend**. We want stocks that are outperforming their longer history in the short-term. We can measure this with two different **simple moving averages** (sma). 

# In[38]:


stocks['aapl_sma_42'] = stocks['aapl_o'].rolling(window=60).mean()
stocks['aapl_sma_252'] = stocks['aapl_o'].rolling(window=252).mean()  

stocks[['aapl_o', 'aapl_sma_42', 'aapl_sma_252']].plot(figsize=(10, 6));  


# Let's create an indicator (1/0) variable that is 1 if the two-month moving average is above the one-year moving average. This would be example of a simple **short-term trend** strategy. You buy the stock if it is doing better now than it has in over the past year. You do not own the stock otherwise.
# 
# I will then graph the moving averages, the price, and the indicator, called **take_position**, on the same graph. I'm going to do something a bit different, but you'll see it in our text. I will use `pandas` `.plot()` to make the graph, but save this to an **axes object**. I can then refer to the **ax** object when styling. This kind of mixes two ways that we've seen plot and figure creation!
# 
# Notice the creation of a secondary y-axis for the indicator variable.

# In[39]:


stocks['take_position'] = np.where(stocks['aapl_sma_42'] > stocks['aapl_sma_252'], 1, -1)  

ax = stocks[['aapl_o', 'aapl_sma_42', 'aapl_sma_252', 'take_position']].plot(figsize=(10, 6), secondary_y='take_position')
ax.get_legend().set_bbox_to_anchor((0.25, 0.85));


# What do you think? Did this strategy work for trading Apple during the 2010s? We'll look more at **backtesting strategies** and all of the issues that arise later on.

# ## Correlation and regression
# 
# We'll look at some simple correlation and linear regression calculations. We'll do more with regression later on.
# 
# Let's look at the relationship between the S&P 500 and the Apple. I'll bring the stocks data again, but just keep these two time series. I won't bother cleaning the names. `pyjanitor` replaces the . in front of `.SPX` with an underscore and `plot()` doesn't like that when making the legend.

# In[40]:


# Read in some eod prices
stocks2 = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True)  

stocks2.dropna(inplace=True)  

stocks2 = stocks2[['.SPX', 'AAPL.O']]


# In[41]:


stocks2.plot(subplots=True, figsize=(10, 6));


# In[42]:


rets2 = np.log(stocks2 / stocks2.shift(1)) 

rets2.dropna(inplace=True)


# In[43]:


pd.plotting.scatter_matrix(rets2,
                           alpha=0.2,  
                           diagonal='hist',  
                           hist_kwds={'bins': 35},  
                           figsize=(10, 6));


# We can run a simple linear regression using `np.polyfit` from the `numpy` library. Other libraries have more sophisticated tools. We'll set `deg=1` since this is a linear regression (i.e. degree of 1). 

# In[44]:


reg = np.polyfit(rets2['.SPX'], rets2['AAPL.O'], deg=1)  
reg


# Apple has a beta of 0.957 (note the scientific notation in the output). The intercept (or alpha) is the next number and is based on daily returns. 

# In[45]:


rets2.corr()  


# ## Generating random returns
# 
# We are going to look more at distributions and what are called Monte Carlo methods when we get to risk management, simulations, and option pricing. But, for now, let's look at a simple case of generating some random returns that "look" like actual stock returns.
# 
# Let's create 1000 random numbers from a normal distribution with a mean of 0 and a standard deviation of 0.01 (1%). This means that we "pull" these numbers out of that distribution. We can then plot them (using `seaborn`, for fun) and include a normal distribution that fits the distribution of random numbers. 

# In[46]:


seed(1986)
random_returns = normal(loc=0, scale=0.01, size=1000)
sns.distplot(random_returns, fit=norm, kde=False)


# Looks like a bell curve to me. Let's take that set of 1000 random numbers and turn them into a `pd.Series`. We can then treat them like actual returns and create a cumulative return series, like above.

# In[47]:


return_series = pd.Series(random_returns)
random_prices = return_series.add(1).cumprod().sub(1)
random_prices.mul(100).plot();


# And there you go! Some fake returns. Stocks returns aren't actually normally distributed like this, at least over short windows. Simulations and Monte Carlo methods are used a lot in wealth management to figure out the probability that a client will meet their retirement goals.
