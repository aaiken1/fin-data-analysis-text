#!/usr/bin/env python
# coding: utf-8

# # Cleaning our data
# 
# Cleaning your data and dealing with dates. That's the life of anyone who deals with data, especially in finance. Most data sets are messy. This is especially true if you or your firm is the one collecting the data and not just purchasing something.
# 
# DataCamp has an article on [cleaning data in `pandas`](https://www.datacamp.com/community/tutorials/data-preparation-with-pandas).
# 
# ## Getting set up
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
# We can bring back the stock data too, as that data has some missing values.

# In[11]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)


# Why are there missing values? Holidays and weekends, when trading doesn't take place.

# In[12]:


prices.isna().sum()


# We can drop these rows. We'll specify `axis=0`, or rows.

# In[13]:


prices = prices.dropna(axis=0)
prices.isna().sum()


# In[14]:


prices.head(15)


# ## Pyjanitor
# 
# We are going to look at a fun package that is based on something from the [R](https://www.r-project.org) statistical programming language, called [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/). 
# 
# To use this package, you'll need to type the following in the terminal (Mac) or command prompt (Windows)
# 
# ```
# conda install -c conda-forge pyjanitor
# ```
# 
# There are even [finance specific tools](https://pyjanitor-devs.github.io/pyjanitor/api/finance/).

# In[15]:


import janitor
from janitor import clean_names


# `pyjanitor` lets us have an interesting workflow. We can read in our data set, remove columns, drop missings, and rename columns, all in one series of steps.

# In[16]:


prices = (
    pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)
    .remove_columns(['GLD'])
    .dropna()
    .rename_column('AAPL.O', 'AAPL')
    .rename_column('MSFT.O', 'MSFT')
)


# There are also some built-in, general functions. `clean_names()` does what it says. For example, it sets all characters in a variable name to lower case.

# In[17]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = prices.clean_names()


# Again, a variety of syntaxes to do the same thing.

# In[18]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = clean_names(prices)


# The method `flag_nulls` creates a new variable that will have a 1 if any of the variables specified are missing. In this case, I didn't specify anything, so it will look across all of the variables. If any variable is `NaN`, then that row gets a 1. Notice the **any**.

# In[19]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = prices.flag_nulls()


# Finally, simple way to see if we have any rows of duplicate data. This will happen surprisingly (and unfortunately) often when we start merging data together. 

# In[20]:


prices.get_dupes()

