#!/usr/bin/env python
# coding: utf-8

# # Merging and reshaping data
# 
# This brief section follows along with the last part of Chapter 5 of out textbook. There are two main topics. First, we want to learn about **merging** or **joining** data sets. Think of this like [xlookup](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929) in Excel, or, more generally, SQL queries. In fact, you can do [SQL in Python](https://www.datacamp.com/community/tutorials/mysql-python), if you're familiar with it. We will also see **concatenating**, or **stacking** data. Finally, we will see how to **reshape our data**. We'll see **wide** and **long** data. 
# 
# ```{margin} The Keys to Our Data
# What variables (e.g. security ID and a date) uniquely identify our data? What variables are common across data sets? 
# ```
# 
# I'll work through a few common examples below using stock data. You can find more examples in the textbook.
# 
# Here are some [visualizations](https://jalammar.github.io/visualizing-pandas-pivoting-and-reshaping/) for what these different functions do.

# In[1]:


# Set-up

import numpy as np
import pandas as pd

import matplotlib as mpl 

import matplotlib.pyplot as plt

aapl = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/aapl.csv')
xom = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/xom.csv')

aapl.set_index('date')
xom.set_index('date')

aapl.info()


# ## Appending data sets
# 
# Appending, or concatenation, or stacking data. This is when you simply put one data set on top of another. However, you need to be careful! Do the data sets share the same variables? How are index values handled?
# 
# There are two ways of doing this. You can use `.append()` or `pd.concat()` from `pandas`.

# In[2]:


ap1 = aapl.append(xom, sort=False)
ap1


# See how there are 1513 rows, but the index for XOM only goes to 755? We didn't ignore the index, so the original index comes over. The first observation of both DataFrames starts at 0. There are 756 AAPL observations and 755 XOM. 
# 
# Let's ignore the index now.

# In[3]:


aapl.append(xom, ignore_index=True, sort=False)


# Here we ignored the index, so the new index goes from 0 to 1512. What should you do? I would ignore the index and reset it in this situation. Once this data is stacked, we have **long** or **narrow** data, where each observation is uniquely identified by the date and a security ID. We have three security IDs in this data: PERMNO, TICKER, and CUSIP. In this particular situation, they should all three work. The PERMNO is the only one that is guaranteed to not change over time. Stocks change tickers. Tickers get reused. Same with CUSIPs. 
# 
# `pd.concat` does the same thing, but with slightly different syntax. I like the way it looks a bit better.

# In[4]:


pd.concat((aapl, xom), sort=False)  


# In[5]:


pd.concat((aapl, xom), ignore_index=True, sort=False)  


# Stacking data sets usually occurs when you're doing fancier looping, which creates some set of data or results for different subgroups (e.g. different years). You then can stack the subgroups on top of each other to get a finished, complete data set. 

# ## Reshaping data sets
# 
# We are going to see two types of data, generally speaking: **wide** data and **long**, or narrow data. 
# 
# In general, **wide data** has a separate column for each variable (e.g. returns, volume, etc.). Each row is then an observation for a security particular unit or firm.
# 
# In finance, it can get more complicated, as wide data might have a date column and then columns like *aapl_ret*, *msft_volume*, etc. Notice how the firm identifiers are mixed with the variable type?
# 
# **Long data** would have columns like *firm*, *variable*, and *value*. Then, each firm would appear on multiple rows, instead of a single row, and the variable column would have multiple values like return, volume, etc. Finally, the specific value for that variable would be in the value column. 
# 
# You can also add an extra dimension for time and add a *date* column. Then, you would multiple variables per firm on specific dates.
# 
# **Long data** is sometimes called **tidy data**. It is, generally speaking, easier to summarize and deal with. Every variable value (e.g. a return) has a key paired with it (e.g. firm ID and date).
# 
# Here's another [explanation of these methods](https://www.geeksforgeeks.org/reshape-a-pandas-dataframe-using-stackunstack-and-melt-method/).
# 
# Let's start with **going from long to wide**. We will use `pd.pivot` to do this.

# In[6]:


wide = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/aapl.csv')


# ## Joining data sets
# 
# You will need to join, or **merge** data sets all of the time. Data sets have **identifiers**, or **keys**. Python calls these the data's **index**. For us, this could be a stock ticker, a PERMNO, or a CUSIP. Finance data sets also have dates typically. If we have several different data sets, we can merge them together using keys.
# 
# To do this, we need to understand the **shape** of our data, discussed above. We usually are merging long data sets, because the keys, like dates and identifiers, are in separate columns. In **wide data**, keys and variables are mixed.
# 
# 
# ```{figure} ../images/04-joins.png
# ---
# name: 04-joins.png
# align: center
# class: with-border
# ---
# Visualization for the four main ways to merge, or join, data.
# ```

# 
