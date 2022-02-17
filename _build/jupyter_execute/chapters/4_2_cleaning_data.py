#!/usr/bin/env python
# coding: utf-8

# # Cleaning our data
# 
# Cleaning your data and dealing with dates. That's the life of anyone who deals with data, especially in finance. Most data sets are messy. This is especially true if you or your firm is the one collecting the data and not just purchasing something.
# 
# DataCamp has an article on [cleaning data in `pandas`](https://www.datacamp.com/community/tutorials/data-preparation-with-pandas).
# 
# [Chapter 7](https://wesmckinney.com/book/data-cleaning.html) of *Python for Data Analysis* for more data cleaning tips.
# 
# ## Underwater exploration
# 
# We'll start by bringing in our Zillow data again.
# 

# In[1]:


import numpy as np
import pandas as pd

uw = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/zestimatesAndCutoffs_byGeo_uw_2017-10-10_forDataPage.csv')
uw.info()


# Once of the most important steps in data cleaning is just looking at what we have. What are the variables? What are their types? How many unique values of each variable do we have? Any missings? Do we see anything unexpected?
# 
# This [page](https://datagy.io/pandas-unique/) has a nice summary.

# In[2]:


uw['UWHomes_Tier2'] = uw["UWHomes_Tier2"].astype('float64')


# We can count the number of times a category appears in a variable. Note that this is only useful for variables that have an sense of category. You would do this for any of the home count or dollar value variables, for example.

# In[3]:


uw['RegionType'].value_counts()


# We should look for missing values for each variable. `isna()` returns a `TRUE` or `FALSE` for each value, depending on whether or not it is `NaN`, or missing. We can then take those 1/0, true or false, values and add them up with `sum()`. 

# In[4]:


uw.isna().sum()


# You can see the logic in how these functions work. We take our DataFrame uw and we send it to `isna()`. This actually creates another DataFrame, that we then pass to `sum()`. Check it out.

# In[5]:


uw.isna()


# The same sort of logic applies to the method `unique()`. This one gives an `array` of each unique value in a column or set of columns.

# In[6]:


uw.RegionName.unique()


# And, to look across multiple columns, we could use `drop_duplicates()'. This will find the unique values for set of variables given it.

# In[7]:


uw[['RegionName','StateName']].drop_duplicates()


# We can count the number of unique values for a variable.

# In[8]:


uw.RegionName.nunique()


# We can filter on one variable and count another. We're looking for unexpected things, just trying to get a sense for what we have.

# In[9]:


uw[uw['RegionType'] == 'MSA'].MSAName.nunique()


# This syntax works too!

# In[10]:


uw[uw['RegionType'] == 'MSA']['MSAName'].nunique()


# We have 95 unique MSA is our data. Seems reasonable. MSAs are like city-regions.
# 
# Finally, let's try some more complicated code. I found this example [here](https://towardsdatascience.com/a-better-eda-with-pandas-profiling-e842a00e1136).
# 
# First, we will create a DataFrame that has the total number of missing values for each variable. We can sort the data using `sort_values()`. The `ascending=False` option will have the variable with the largest number of missings at the top.
# 

# In[11]:


total = uw.isna().sum().sort_values(ascending=False)


# By the way, you'll also see a `isnull()` method that does the same thing as `isna()`. 
# 
# Next, let's create a DataFrame that that has the percentage of values that are missing for each variable. This is neat one - we are creating a DataFrame of values (total number missing) for the numerator and another DataFrame of values (total number) for the denominator. Then, we are dividing two DataFrames, giving us another DataFrame of the resulting division. We then sort.

# In[12]:


percent = (uw.isnull().sum()/uw.isnull().count()).sort_values(ascending=False)


# We can use a new function called `concat` from `pandas` that combines data, either as rows (stacking) or columns (combining). We'll combine columns, with means concatenating along axis=1. We'll name both columns. We can do this because each DataFrame has the same index created by `pandas`, all of our variable names. So, there's a one-to-one correspondence between the two DataFrames.

# In[13]:


missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Missing Percent'])


# Let's take the percents and multiply all of them by 100, just to make them look like percents. And to show you, again, that you can.

# In[14]:


missing_data['Missing Percent'] = missing_data['Missing Percent'] * 100


# For the last step, we can filter and just get the variable names where more than 10% of our data are missing.

# In[15]:


missing_data[missing_data['Missing Percent'] > 10]


# 
# ## Back to stocks
# 
# We can bring back the stock data too, as that data has some missing values.

# In[16]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)


# Why are there missing values? Holidays and weekends, when trading doesn't take place.

# In[17]:


prices.isna().sum()


# We can drop these rows. We'll specify `axis=0`, or rows.

# In[18]:


prices = prices.dropna(axis=0)
prices.isna().sum()


# In[19]:


prices.head(15)


# ## Pyjanitor
# 
# We are going to look at a fun package that is based on something from the [R](https://www.r-project.org) statistical programming language, called [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/). 
# 
# To use this package, you'll need to type the following in the terminal (Mac) or command prompt (Windows).
# 
# ```
# conda install -c conda-forge pyjanitor
# ```
# This will install `pyjanitor` using Ananconda. So, it should show up when you select the Anaconda distribution of Python. You'll need to restart VS Code once you've installed it.
# 
# There are even [finance specific tools](https://pyjanitor-devs.github.io/pyjanitor/api/finance/).

# In[20]:


import janitor
from janitor import clean_names


# `pyjanitor` lets us have an interesting workflow. We can read in our data set, remove columns, drop missings, and rename columns, all in one series of steps.

# In[21]:


prices = (
    pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)
    .remove_columns(['GLD'])
    .dropna()
    .rename_column('AAPL.O', 'AAPL')
    .rename_column('MSFT.O', 'MSFT')
)


# There are also some built-in, general functions. `clean_names()` does what it says. For example, it sets all characters in a variable name to lower case.

# In[22]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = prices.clean_names()


# Again, a variety of syntaxes to do the same thing.

# In[23]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = clean_names(prices)


# The method `flag_nulls` creates a new variable that will have a 1 if any of the variables specified are missing. In this case, I didn't specify anything, so it will look across all of the variables. If any variable is `NaN`, then that row gets a 1. Notice the **any**.

# In[24]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = prices.flag_nulls()


# Finally, simple way to see if we have any rows of duplicate data. This will happen surprisingly (and unfortunately) often when we start merging data together. 

# In[25]:


prices.get_dupes()

