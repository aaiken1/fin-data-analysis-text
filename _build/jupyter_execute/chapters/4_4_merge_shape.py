#!/usr/bin/env python
# coding: utf-8

# # Merging and reshaping data
# 
# We are going to cover two main topics in this brief section. First, we want to learn about **merging** or **joining** data sets. Think of this like [xlookup](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929) in Excel, or, more generally, SQL queries. In fact, you can do [SQL in Python](https://www.datacamp.com/community/tutorials/mysql-python), if you're familiar with it. We will also see **concatenating**, or **stacking** data. We will see how to **reshape our data**. We'll see **wide** and **long** data. We'll end with using **multi-level indices** to shape our data.
# 
# ```{margin} The Keys to Our Data
# What variables (e.g. security ID and a date) uniquely identify our data? What variables are common across data sets? 
# ```
# 
# I'll work through a few common examples below using stock data.
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

aapl = aapl.set_index('date')
xom = xom.set_index('date')

aapl.info()


# Our usual set-up is above. Notice that I'm setting the index of each DataFrame using `.set_index()`, instead of doing it inside of the `.read_csv()`. Either way works.
# 
# By setting *date* as my index, it will disappear from the variable list. 

# In[2]:


xom.info()


# We can check and make sure that *date* really is the index. I'll use the *xom* DataFrame.

# In[3]:


xom.index


# ## Concatenating data sets
# 
# Appending, or concatenation, or stacking data. This is when you simply put one data set on top of another. However, you need to be careful! Do the data sets share the same variables? How are index values handled?
# 
# You can use `.concat()` from `pandas`. Notice that our two datasets don't have exactly the same number of rows. Older code might use `.append()` from `pandas`.

# In[4]:


pd.concat((aapl, xom), sort=False)  


# See how there are 1513 rows, but the index for XOM only goes to 755? We didn't ignore the index, so the original index comes over. The first observation of both DataFrames starts at 0. There are 756 AAPL observations and 755 XOM. 
# 
# Let's ignore the index now.

# In[5]:


pd.concat((aapl, xom), ignore_index=True, sort=False)  


# Here we ignored the index, so the new index goes from 0 to 1512. What should you do? I would ignore the index and reset it in this situation. Once this data is stacked, we have **long** or **narrow** data, where each observation is uniquely identified by the date and a security ID. We have three security IDs in this data: PERMNO, TICKER, and CUSIP. In this particular situation, they should all three work. The PERMNO is the only one that is guaranteed to not change over time. Stocks change tickers. Tickers get reused. Same with CUSIPs. 
# 
# Stacking data sets usually occurs when you're doing fancier looping, which creates some set of data or results for different subgroups (e.g. different years). You then can stack the subgroups on top of each other to get a finished, complete data set. 

# ## Reshaping data sets
# 
# We are going to see two types of data, generally speaking: **wide** data and **long**, or narrow data. We will be **melting** our data (going from wide to long) or **pivoting** our data (going from long to wide). 
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
# Let's start with **going from wide to long**. We will use `pd.melt` to do this.

# In[6]:


wide = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/wide_example.csv')
wide


# This data has four firms, all on a single date. There are actually three IDs here: PERMNO, COMNAM, and CUSIP. PERMNO is the permanent security ID assigned by [CRSP](https://crsp.org). COMNAM is obviously the firm name. [CUSIP](https://www.cusip.com/index.html) is a security-level ID, so multiple securities (e.g. bonds) from the same firm will have different CUSIPs, though the first six digits of the CUSIP will ID the firm. When you look up fund holdings with the SEC, you'll get a CUSIP for each security held by the mutual fund, hedge fund, etc.
# 
# There are then four variables for each security: price (*PRC*), return (*RET*), the price at the open (*OPENPRC*), and the number of trades on the NASDAQ exchange (*NUMTRD*) Exxon doesn't trade on the NASDAQ, so that variable is missing, or NaN. 
# 
# We can use `pd.melt` to take this wide data and make it long. Long data will have a firm identifier (or several), a date, a column that contains the **names** of the different variables (e.g. PRC, RET), and a column for the **values** of the variables. I will keep *PERMNO* as my ID, keep *PRC* and *RET*, name my variable column *vars* and my value column *values*. I'll save this to a new DataFrame called *long*.

# In[7]:


long = pd.melt(wide, id_vars = ['PERMNO'], value_vars = ['PRC', 'RET'], var_name = 'vars', value_name = 'values')
long


# You don't have to explicitly specify everything that I did. Here, I melt and just tell it to create a *PERMNO* ID column. Keep everything else. You can really see the long part now. 

# In[8]:


pd.melt(wide, id_vars = ['PERMNO'])


# You can also have two different identifying variables. This is helpful if you have **panel** data, with multiple firm observations across different dates. This is obviously very common in finance.

# In[9]:


long2 = pd.melt(wide, id_vars = ['PERMNO', 'date'], value_vars = ['PRC', 'RET'], var_name = 'vars', value_name = 'values')
long2


# We can put our long data back to wide using `pd.pivot`. You need to tell it the column that has the values, the column that has the variable names, and the column to create your index (ID).

# In[10]:


wide2 = pd.pivot(long, values = 'values', columns = 'vars', index = 'PERMNO')
wide2


# We can use the long data that kept the date to create wide data with multiple indices: the firm ID and the date. This will again be very helpful when we deal with multiple firms over multiple time periods. The firm ID and the date will uniquely identify each observation. 

# In[11]:


wide3 = pd.pivot(long2, values = 'values', columns = 'vars', index = ['PERMNO', 'date'])
wide3


# ## Joining data sets
# 
# You will need to join, or **merge** data sets all of the time. Data sets have **identifiers**, or **keys**. Python calls these the data's **index**. For us, this could be a stock ticker, a PERMNO, or a CUSIP. Finance data sets also have dates typically. If we have several different data sets, we can merge them together using keys.
# 
# To do this, we need to understand the **shape** of our data, discussed above. 
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
# We will use `pd.join` to do this. I'm going to bring in two sets of data from CRSP. Each data set has the same three securities, XOM, AAPL, and TLT, over the same time period (Jan 2019 - Dec 2021). But, they have some different variables.

# In[12]:


crsp1 = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/crsp_022722.csv')
crsp2 = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/crsp_030622.csv')


# We can look at each DataFrame and see what they have.

# In[13]:


crsp1


# In[14]:


crsp2


# We can see that they each have the same IDs (e.g. *PERMNO*) and *date*. The *crsp2* DataFrame has an additional variable, *RETX*, or returns without dividends, that I want to merge in. I'm going to simplify the *crsp2* DataFrame and only keep three variables: *PERMNO*, *date*, and *retx*. I will then merge using *PERMNO* and *date* as my **keys**. These two variables uniquely identify each row. 
# 
# I will do an **inner join**. This will only keep *PERMNO*-*date* observations that are in **both** data sets. An **outer join** would keep all observations, including those that are in one dataset, but not the other. This might be helpful if you had PERMNOs in one data set, but not the other, and you wanted to keep all of your data.
# 
# For this particular data, there should be a 1:1 correspondence between the observations. 

# In[15]:


crsp2_clean = crsp2[['PERMNO', 'date', 'RETX']]
merged = crsp1.merge(crsp2_clean, how = 'inner', on = ['PERMNO', 'date'] )
merged


# You can see the *RETX* variable at the end of the merged DataFrame. 
# 
# What happens if you don't clean up with *crsp2* data first?

# In[16]:


merged = crsp1.merge(crsp2, how = 'inner', on = ['PERMNO', 'date'] )
merged


# Do you see the `_x` and `_y` suffixes? `pd.merge` adds that when you have two variables with the same name in both data sets that **you are not using as key values**. The variables that you merge on, the key values, truly get merged together, and so you only get one column for *PERMNO* and one column for *date*, in this example. But, *TICKER* is in both data sets and is not a key value. So, when you merge the data, you're going to have two columns names *TICKER*. The `_x` means that the variable is from the *left* (first) data set and the `_y` means that the variable is from the *right* (second) data set. 
# 
# You can read more about `pd.merge` [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html). Bad merges that lose observations are a common problem. 
# 
# You have to understand your data structure before trying to combine DataFrames together. 

# ## Multiple Levels
# 
# So far, we've only defined data with one index value, like a date or a stock ticker. But - look at the return data above. There is both a stock and a date. When data has an ID and a time dimension, we call that **panel data**. For example, stock-level or firm-level data through time. `pandas` can help us deal with this type of data as well.
# 
# You can read more about **MultiIndex** data on the `pandas` [help page](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#).
# 
# This type of data is also called **hierarchical**. Let's use the *crsp2* DataFrame to see what's going on.

# In[17]:


crsp2


# We have *PERMNO*, our ID, and *date*. Together, these each define a unique observation. 
# 
# We can see that *crsp2* doesn't have an index that we've defined. It is just the default number.

# In[18]:


crsp2.index


# I'll now set **two indices** for the CRSP data and save this as a **new DataFrame** called *crsp3*. I'm using the `pandas` `.set_index()` function and 
# passing the name of the columns in the list.
# 
# I then sort the data using `.sort_index()`. This does what it says - it sorts by *date* and then *PERMNO*.

# In[19]:


crsp3 = crsp2.set_index(['date', 'PERMNO'])

crsp3.sort_index()

crsp3


# You can see the multiple levels now. You can perform operations by using these indices.
# 
# Let's group by *PERMNO*, or our Level 1 index, and calculate the average return for each stock across all dates.

# In[20]:


crsp3.groupby(level = 1)['RETX'].mean()


# Let's do the same thing using the first level, or the *date*. This gives the average return of the three stocks on each date.

# In[21]:


crsp3.groupby(level = 0)['RETX'].mean()


# As before, we can use `to.frame()` to go from a series to a DataFrame and make the output look a little nicer.

# In[22]:


crsp3.groupby(level = 1)['RETX'].mean().to_frame()


# We can use the name of the levels, too. Here I'll find the min and the max return for each stock and save it as a new DataFrame.

# In[23]:


crsp3_agg = crsp3.groupby(level = ['PERMNO'])['RETX'].agg(['max', 'min'])
crsp3_agg


# With indices defined, I can use `.unstack()` to from long to wide data. I'll take the return and create new columns for each stock.

# In[24]:


crsp3['RETX'].unstack()


# ```{margin}
# ```{note}
# The *PERMNO*s are now the column headers, so we're treating each stock like a variable. You'll see a lot of finance data like this, with tickers or another ID as columns. But, you can no longer merge on the stock if you wanted to bring in additional variables! This is why the organization of your data is so important. Long data is easier to deal with when combining data sets.
# ``````
# 
# If I had defined the *PERMNO* as the Level 0 index and *date* as the Level 1 index, then I would have unstacked my data with dates as the columns and the stocks as the rows. That's not what I wanted, though.

# ### Columns and levels
# 
# The **unstacked** data above has a *PERMNO* for each column. Underneath each *PERMNO* is a return. But, what if we have, say, both return and price data? 
# 
# We can also add **levels** to our columns, creating groups of variables when we have **wide** data. Let's go back to the *wide3* DataFrame from above. We can also go even wider. Let's get of the two indices, *PERMNO* and *date*, in *wide3* and turn them both back into columns.

# In[25]:


wide3 = wide3.reset_index()
wide3


# Now, let's create a DataFrame where **just** *date* is an index and go wider, where each column is now either a *RET* or a *PRC* for each *PERMNO*.

# In[26]:


wide4 = pd.pivot(wide3, values = ['RET', 'PRC'], columns = 'PERMNO', index = 'date')
wide4


# We only had one date, so this isn't a very interesting DataFrame. 
# 
# I can take my DataFrame, select the index, and get the name of my index. Remember, indices are about the **rows**.

# In[27]:


wide4.index.names


# But, you can tell from the above DataFrame that my columns now look different. They have what `pandas` calls **levels**.

# In[28]:


wide4.columns.levels


# See how there are two lists? One for each level of column. 
