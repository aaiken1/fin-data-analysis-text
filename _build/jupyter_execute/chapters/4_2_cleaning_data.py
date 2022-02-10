#!/usr/bin/env python
# coding: utf-8

# # Cleaning our data
# 
# Cleaning your data and dealing with dates. That's the life of anyone who deals with data, especially in finance. Most data sets are messy. This is especially true if you or your firm is the one collecting the data and not just purchasing something.
# 
# DataCamp has an article on (cleaning data in `pandas`)[https://www.datacamp.com/community/tutorials/data-preparation-with-pandas].
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

# In[2]:


uw['UWHomes_Tier2'] = uw["UWHomes_Tier2"].astype('float64')


# In[3]:


uw['RegionType'].value_counts()


# In[4]:


uw.isna().sum()


# In[5]:


uw.RegionName.unique()


# In[6]:


uw.RegionName.nunique()


# In[7]:


uw[uw['RegionType'] == 'MSA'].MSAName.nunique()


# In[8]:


uw[uw['RegionType'] == 'MSA']['MSAName'].nunique()


# We can bring back the stock data too, as that data has some missing values.

# In[9]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)


# Why are there missing values? Holidays and weekends, when trading doesn't take place.

# In[10]:


prices.isna().sum()


# We can drop these rows. We'll specify `axis=0`, or rows.

# In[11]:


prices = prices.dropna(axis=0)
prices.isna().sum()


# In[12]:


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

# In[13]:


import janitor
from janitor import clean_names


# In[14]:


prices = (
    pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)
    .remove_columns(['GLD'])
    .dropna()
    .rename_column('AAPL.O', 'AAPL')
    .rename_column('MSFT.O', 'MSFT')
)


# In[15]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = prices.clean_names()


# In[16]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = clean_names(prices)


# In[17]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices = prices.flag_nulls()


# In[18]:


prices.get_dupes()

