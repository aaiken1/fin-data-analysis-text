#!/usr/bin/env python
# coding: utf-8

# # Importing data
# 
# Let's start by getting some data into Python. This will usually be the first step in our code, right after we import any of the libraries, like `numpy` and `pandas` that we need.
# 
# There is a [DataCamp tutorial on Excel files and Python](https://www.datacamp.com/community/tutorials/python-excel-tutorial) that you might find helpful. You can read also more about [reading in CSV files at DataCamp](https://www.datacamp.com/community/tutorials/pandas-read-csv). 
# 
# We'll typically be either **importing** our data from CSV and Excel files or using **data APIs** (Application Programming Interfaces) to pull in data from external sources. We'll do more of the latter in a separate section of the notes.

# There's some price data up on our [course Github page](https://github.com/aaiken1/fin-data-analysis-python). Let's import this both as a downloaded CSV file and then directly from Github. No need to download the file to your computer and deal with folders. 
# 
# First, we need to import `pandas`. Just like `numpy`. In fact, at the top of basically all of your code, you will import both of these libraries (and more!).
# 
# Everyone imports `pandas` as pd.

# In[1]:


import pandas as pd


# Let's start by making a DataFrame ourself, just to see how they are different from `numpy` arrays.

# In[2]:


df = pd.DataFrame([75,79,82,60], columns = ['Prices'], index =[1,2,3,4])


# This is similar to an example from [Python for Finance, 2e](https://www.oreilly.com/library/view/python-for-finance/9781492024323/). I am creating a DataFrame with one column. This column has four stock prices. I am labeling that column as `Prices`. I then have an `index` value that refers to each row. I am using numbers. This could easily be a date and, in fact, will be later on when we import real price data.
# 
# See how this is kind of like a spreadsheet? And, unlike an array, we have **labels** or **headers** for columns. And we have indexes for each row that aren't really part of the data. 
# 
# We'll do more with this in the next section.
# 
# Ok, let's import that CSV file into a `DataFrame`. You'll need to data on your local computer (or Google Drive) for code like this to work. We'll change that in a second.

# In[3]:


prices = pd.read_csv('../data/tr_eikon_eod_data.csv',
                  index_col = 0, parse_dates = True)


# First, if you're in Jupyter Notebook in VS Code, click the **Variables** button at the top. Google Colab has a similar button on the left. You'll see the two DataFrames that we now have in memory appear below. Click the pop-out button to view them.
# 
# Notice how I did the path name. `../` means to start start from my home directory. What's my home directory? That's where your `.ipynb` file lives. **Relative** to that directory, Python looks for a folder called `data`. Finally, it looks for the .csv file called `tr_eikon_eod_data.csv` inside of that folder.
# 
# What are those other options doing? `index_col=0` tells `pandas` to create a DataFrame where column 0 (the first column in the .csv file) is the index. Check out the CSV file - that's the date. With finance data, the date will often be the index, since we are dealing with time series data (e.g. stock prices or returns).
# 
# Sometimes data will be **multi-index**. For example, if we have multiple stocks and dates. More on this later - it depends on how the data are organized.
# 
# The option `parse_dates` is telling `pandas` to look at the index column and try to turn what it sees into official Python dates. That works in this case. Finance coders will joke that 90% of their time is spent doing date corrections. For example, what happens if you have multiple markets in different time zones and you're trying to deal with time series at a trade-level frequency (i.e. less than a second)? Have fun!
# 
# You can read about the `pd.read_csv` method on the [`pandas` web page](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).
# 
# You can also write Python data to a .csv or Excel file.
# 
# Let's now read in this file directly from our class Github page. When reading data in from Github, you won't have to download it first. I'll call the resulting DataFrame `prices2`, just so that we can see that we actually have the same thing twice.
# 

# In[4]:


prices2 = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv')


# I made a "mistake" on purpose there. Notice how I didn't do the `index_col`? Check out the `prices2` DataFrame below. You'll see an index column with 1, 2, 3,.. and then the date column. The `read_csv` created an index for me, since I didn't specify one.

# In[5]:


prices2


# Let's redo that.

# In[6]:


prices2 = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True)

prices2


# That's better! We'll end by looking at some of the **attributes** of our `prices` DataFrame.
# 
# First, let's check our index. Is it really a date?

# In[7]:


prices.index


# It is! We'll do more with dates. A lot more. 
# 
# Let's look at the columns.

# In[8]:


prices.columns


# Yup, those are our column headers from the .csv file.
# 
# There are many options that can go into the `pd.read_csv` function. For example, you can load just a certain number of rows.
# 
# 
# 

# In[9]:


prices100 = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True, nrows = 100)


# You can bring in just certain columns. In `pandas`, we select columns using `['COLUMN']`.

# In[10]:


prices_spx= pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True, usecols = (['.SPX']))


# You can also specify if a particular value should be set to missing. `read_csv()` already looks for common items, like 'NA' or 'n/a'. I'll have it look for '-' as well, though that isn't a missing value in this data.

# In[11]:


prices2 = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col = 0, parse_dates = True, na_values = '-')


# We can also read data in from **Excel files**, using `.read_excel()`. I'll read in some HF return data.

# In[12]:



hf = pd.read_excel('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/hf_rets.xlsx',
                  index_col = 0, parse_dates = True, sheet_name = 'rets')  


# We can use the option `sheet_name=` to specific a particular sheet from the Excel file. You can read more about the various options [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html). 

# We have our data in Python! Now, we can manipulate it, clean it, merge it with something else, summarize it, plot it, and do some actual finance.
