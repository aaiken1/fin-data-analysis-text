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
# 
# We can select a column and change the variable type using `.astype()`.

# In[2]:


uw['UWHomes_Tier2'] = uw['UWHomes_Tier2'].astype('float64')


# This code is actually taking the column, changing its type, and saving it to the DataFrame with the same column name. Note that we could changed the name of the column.

# ## Counting, missings, and dupes
# 
# When you first bring in some data, you often want to do some simple checks. How many observations do you have? Are you missing anything? Are their duplicate observations? How do we define duplicate observations?
# 
# You can't do any data analysis until you **understand the structure of your data**. What do you have? Why do you have it? How do you want to use it? 
# 
# Let's start with **counts**. We can count the number of times a **category** appears in a variable. Note that this is only useful for variables that have an sense of category. You would do this for any of the home count or dollar value variables, for example.
# 
# We can select a **categorical variable**, like *RegionType* and then use `.value_counts()` from `pandas`. 

# In[3]:


uw['RegionType'].value_counts()


# We should look for **missing values** for each variable. `isna()` returns a `TRUE` or `FALSE` for each value, depending on whether or not it is `NaN`, or missing. We can then take those 1/0, true or false, values and add them up with `sum()`. 

# In[4]:


uw.isna().sum()


# You can see the logic in how these functions work. We take our DataFrame uw and we send it to `isna()`. This actually creates another DataFrame, that we then pass to `sum()`. Check it out.

# In[5]:


uw.isna()


# The same sort of logic applies to the method `unique()`. This one gives an `array` of each unique value in a column or set of columns. This will save an array of unique values that appear in the *RegionName* column.

# In[6]:


unique_regions = uw.RegionName.unique()


# I'm using the `.ColumnName` construction to pull the variable. 
# 
# We can count the number of unique values for a variable.

# In[7]:


uw.RegionName.nunique()


# We can filter on one variable and count another. We're looking for unexpected things, just trying to get a sense for what we have.

# In[8]:


uw[uw['RegionType'] == 'MSA'].MSAName.nunique()


# This syntax works too! We are pulling the column name out using a **list** defined by the column names inside of `[]`.

# In[9]:


uw[uw['RegionType'] == 'MSA']['MSAName'].nunique()


# We have 95 unique MSA is our data. Seems reasonable. MSAs are like city-regions.

# Finally, we can just drop any rows with missing values using `.dropna()` from `pandas`. If we don't specify a column, then it will drop a row if **ANY** value is missing. I don't actually want to drop missings here, so I'm not going to save my work with a `uw = `.
# 
# You can read more [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html). 

# In[10]:


uw.dropna(axis = 0)


# We now have 1071 rows, since *MSAName* had so many missing values. But - that was OK given how this data are constructed. You'll see another example with stock data below.
# 
# Now, I'll just drop observations if *AllHomes_Tier1* is missing.

# In[11]:


uw.dropna(subset = ['AllHomes_Tier1'], axis = 0)


# Nothing gets dropped, since there were no missing values. 

# Unique and missing values are important. So is the idea of **duplicates**. Does a row (an observation) contain the same values as another row? That could be all of the values across all of the variables, or just a particular column (e.g. ticker), or a set of columns (e.g. ticker and date).
# 
# We can see if our data has any duplicates by using `.duplicated()` from `pandas`.
# 
# You can read more [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html). 
# 
# I'm going to **filter** my data to only include `RegionType='Zip'` and then look for duplicate Zip codes. The Zip codes are found in *RegionName*. I'll save this to a new DataFrame called *dupes*. The argument `keep='first` will keep the first duplicate, if any. 
# 
# I am then going to **mask** my subset of the uw data. So, I filter to get just Zip codes. Then, I **mask** on the *dupes* DataFrame. This DataFrame is just an array of True/False values. By **masking**, I'm telling Python to only keep values that are True. There are no True values, so no duplicate Zips and the resulting DataFrame is empty. 
# 

# In[12]:


dupes = uw[uw['RegionType'] == 'Zip'].duplicated(subset=['RegionName'], keep='first')

uw[uw['RegionType'] == 'Zip'][dupes]


# 
# We can use `drop_duplicates()` to look at our data and drop rows that are duplicate observations. We use the `subset=` argument to tell it what columns to look at for duplicates. We can leave out this argument if we want to look across all columns. 
# 
# The argument `keep=` will tell it which duplicate to keep in the data (e.g. the first one or the last one).
# 
# You can read more about the syntax [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html).

# In[13]:


uw.drop_duplicates()


# In[14]:


uw.drop_duplicates(subset=['RegionName', 'StateName'], keep='last')


# You want to keep track of the number of observations (rows) when you're dropping duplicates. In this case, we go from 2,610 rows to 2,571. 

# ## Sorting our data
# 
# Another basic task that we often face is **sorting our data**. You can sort numeric or string data, by variable using `.sort_values()` from `pandas`.
# 
# The `ascending=` argument can be True or False and tells us how to sort. You can pass it a list of how to sort if you're sorting on multiple variables. 
# 
# I'l sort the data by *RegionType* first. Then, I'll sort the data by *RegionType*, *RegionName*, and *AllHomes_Tier1*
# 
# You can read more [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html).

# In[15]:


uw.sort_values(by = 'RegionType', ascending = True)


# In[16]:


uw.sort_values(by = ['RegionType', 'RegionName', 'AllHomes_Tier1'], ascending = [True, True, False])


# ## Renaming columns
# 
# While cleaning our data, we might want to rename our columns, or variables. You can do this automatically with something like `pyjanitor` (see below). You can also do it when importing the data using `.read_csv` from `pandas`, if you know that you'll want to change the name. 
# 
# It is also easy enough to do using `.rename` from `pandas`. You give it a mapping of old name to new name. I'll rename *MSAName* for fun.
# 
# Note the `inplace=True` argument. You'll see this a lot for `pandas` methods. This makes it so that we don't have to do a `uw = uw.rename()`. Instead, we save over the old DataFrame with the new one with the new column name.
# 
# You can read more [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html).

# In[17]:


uw.rename(columns = {'MSAName':'msaname'}, inplace = True)


# ## Dropping columns
# 
# We can also simply drop a column of data. You could do this via data subsets (e.g. `.iloc`), but this method lets you use `.drop()` to specify the name of the column. It's a little clearer doing things this way.
# 
# The `axis=1` option means that you are dropping the column named. I've picked a column at random to drop. Notice that I'm saving my work back to the *uw* DataFrame.

# In[18]:


uw = uw.drop('UWHomes_TotalValue_Tier3', axis=1)


# ## Missing data example
# 
# Finally, let's try some more complicated code. I found this example [here](https://towardsdatascience.com/a-better-eda-with-pandas-profiling-e842a00e1136).
# 
# First, we will create a DataFrame that has the total number of missing values for each variable. We can sort the data using `sort_values()`. The `ascending=False` option will have the variable with the largest number of missings at the top.

# In[19]:


total = uw.isna().sum().sort_values(ascending=False)


# By the way, you'll also see a `isnull()` method that does the same thing as `isna()`. 
# 
# Next, let's create a DataFrame that that has the percentage of values that are missing for each variable. This is neat one - we are creating a DataFrame of values (total number missing) for the numerator and another DataFrame of values (total number) for the denominator. Then, we are dividing two DataFrames, giving us another DataFrame of the resulting division. We then sort.

# In[20]:


percent = (uw.isnull().sum()/uw.isnull().count()).sort_values(ascending = False)


# We can use a new function called `concat` from `pandas` that combines data, either as rows (stacking) or columns (combining). We'll combine columns, with means concatenating along axis=1. We'll name both columns. We can do this because each DataFrame has the same index created by `pandas`, all of our variable names. So, there's a one-to-one correspondence between the two DataFrames.

# In[21]:


missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Missing Percent'])


# Let's take the percents and multiply all of them by 100, just to make them look like percents. And to show you, again, that you can.

# In[22]:


missing_data['Missing Percent'] = missing_data['Missing Percent'] * 100


# For the last step, we can filter and just get the variable names where more than 10% of our data are missing.

# In[23]:


missing_data[missing_data['Missing Percent'] > 10]


# 
# ## Back to stocks
# 
# We can bring back the stock data too, as that data has some missing values.

# In[24]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True)


# Why are there missing values? Holidays and weekends, when trading doesn't take place.

# In[25]:


prices.isna().sum()


# We can drop these rows. We'll specify `axis=0`, or rows.

# In[26]:


prices = prices.dropna(axis=0)
prices.isna().sum()


# In[27]:


prices.head(15)


# ## Pyjanitor
# 
# We are going to look at a fun package that is based on something from the [R](https://www.r-project.org) statistical programming language, called [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/#installation). 
# 
# To use this package, you'll need to type the following in the terminal (Mac) or cmd terminal (Windows).
# 
# ```
# pip install pyjanitor
# ```
# 
# This will install `pyjanitor` using `pip`. Again, **if you're using Windows, make sure that your terminal is cmd and not Powershell**. `pip` works in Powershell, but you have to change a system setting first.You'll need to restart VS Code once you've installed it.
# 
# If you're using Google Colab, there's currently a bug in pyjanitor that requires you to install a previous version. You can do this in a Jupyter cell. Note that you need to use `!pip` when using a terminal command inside of a Jupyter notebook. 
# 
# ```
# !pip install pyjanitor==0.23.1
# ```
# 
# There are even [finance specific tools](https://pyjanitor-devs.github.io/pyjanitor/api/finance/).
# 
# We can bring in `janitor` and treat it as part of `pandas` using the `import` function.

# In[28]:


import janitor


# `pyjanitor` lets us have an interesting workflow. We can read in our data set, remove columns, drop missings, and rename columns, all in one series of steps.

# In[29]:


prices = (
    pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True)
    .remove_columns(['GLD'])
    .dropna()
    .rename_column('AAPL.O', 'AAPL')
    .rename_column('MSFT.O', 'MSFT')
)


# There are also some built-in, general functions. `clean_names()` does what it says. For example, it sets all characters in a variable name to lower case.

# In[30]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True)

prices = prices.clean_names()


# Note the syntax - you start with the DataFrame and then apply the function to it.
# 
# You might see another syntax, though. You can import the functions directly and then include the DataFrame as an argument to that function. Both ways are detailed in the [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/#installation) instructions.

# In[31]:


from janitor import clean_names, remove_empty
 
prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True)

prices = clean_names(prices) # See the difference?


# The method `flag_nulls` creates a new variable that will have a 1 if any of the variables specified are missing. In this case, I didn't specify anything, so it will look across all of the variables. If any variable is `NaN`, then that row gets a 1. Notice the **any**.

# In[32]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True)

prices.flag_nulls()


# Finally, simple way to see if we have any rows of duplicate data. This will happen surprisingly (and unfortunately) often when we start merging data together. 

# In[33]:


prices.get_dupes()

