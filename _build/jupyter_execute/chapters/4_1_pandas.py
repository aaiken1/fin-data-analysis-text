#!/usr/bin/env python
# coding: utf-8

# # pandas
# 
# Now that we know how to get our data in, let's look a little more at `pandas` and what it can do. To do this, let's bring in some data from Zillow.
# 
# The data frame we will be working with contains data from Zillow.com, the housing web site, on the number of homes, the median value of homes, etc. at-risk for flooding due to rising sea levels.
# 
# You can find many different Zillow data sets [here](https://www.zillow.com/research/data/). The “uw” here stands for “under water” in a very literal sense. I first thought they were talking about mortgages!
# 
# As mentioned, take a look at [Chapter 5](https://wesmckinney.com/book/pandas-basics.html) of *Python for Data Analysis* for an introduction to `pandas`. 

# In[1]:


import numpy as np
import pandas as pd

uw = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/zestimatesAndCutoffs_byGeo_uw_2017-10-10_forDataPage.csv')


# We are going to use `read_csv` to get this data off of my Github page. `pandas` also comes with `read_excel`, `read_json`, `read_html`, and other ways to get formatted data into Python.

# ## Looking at our data
# 
# Let's peak at this data. You can do that below, or using the `.info` method. We'll get variable names, the number of non-missing (null) observations, and the type of data. One number variable, `UWHomes_Tier2`, got brought in as an integer, rather than a float. When you look at the data below, notice how that one column doesn't have a `.0` on any of the numbers. Integers can't have decimal places.

# In[2]:


uw.info()


# Just to show you, I'm going to reimport that data, but force that one variable to also come in as the same variable type. I don't want anything unexpected to happen, so let's get all numerics as floats.

# In[3]:


uw = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/zestimatesAndCutoffs_byGeo_uw_2017-10-10_forDataPage.csv', dtype={'UWHomes_Tier2':np.float64})
uw.info()


# OK, that seems better. All of these functions that we're using have many different options. The only way to learn about them is to play around, read help documents, and search online for solutions to our problems.
# 
# There's a concept in data analysis called **tidy data**. The characteristics of tidy data are:
# 
# - Each variable forms a column.
# - Each observation forms a row.
# - Each type of observational unit forms a table.
# 
# ```{figure} ../images/04-tidy.png
# ---
# name: 04-tidy.png
# align: center
# ---
# Tidy data.
# ```
# 
# The first thing to note about this data is that there are several tiers. Some numbers are at the national level, some at the region, some at the state, and some at the MSA. **Tidy data** refers to one row, one observation, across different variables (columns) and, possibly, across time. When you have multiple observations of the same firm, state, person, etc. over time, we call that panel data. Panel data is tidy too.
# 
# Note that some RegionTypes (e.g. Nation, State) are actually summaries of other rows. This is bit confusing and we need to be mindful of this different levels when using the data.
# 
# Before we get to that, just a few more methods to look at the data.
# 
# First, let's look at the first five rows.

# In[4]:


uw.head()


# `NaN` is how `pandas` shows missing values. So, that first row is `RegionType == 'Nation'` and `RegionName == 'UnitedStates'`. `StateName` and `MSAName` are undefined, since this row is **all of the data added up**. We usually don't want to have summary statistics in the same DataFrame as underlying data! What a mess!
# 
# We can also look at the last five rows.

# In[5]:


uw.tail()


# Looking at this data, I think it really has four levels that describe the numbers. The columns `RegionType`, `RegionName`, `StateName`, and `MSAName` define unique rows of data. Again, note that these values can be missing. For example, row 2606 is Zip, 98595, Washington, but no `MSAName`. Why? MSA stands for Metropolitan Statistical Area and covers multiple zip codes. This data is **not tidy**.
# 
# Let’s think about the other variable definitions a bit. Zillow places homes into three tiers based on the home’s estimated market value, with Tier3 being the highest value. `AllHomes` refers to all homes in that tier or across all tiers. `UWHomes` refers to homes that are at risk for flooding. Note that there are some variables that are counts, some that are dollar values, and others that are percentages.
# 
# Finally, when using a Jupyter notebook, you can just put the name of the DataFrame in a cell and run the cell. You'll get a peak at the DataFrame too. In the DataCamp assignments, you're using a Python **script**, not a Jupyter notebook, which is why they have to do things like use `print()` to get the data to display. The Jupyter notebook does this automatically for us.

# In[6]:


uw


# ## Saving our work
# 
# You're going to see syntax like:
# 
# `df = df.some_stuff`
# 
# This means that our work is getting saved. In this case, I'm replacing my original DataFrame *df* with another DataFrame, also called *df*. I could have changed the name of the DataFrame.
# 
# You'll also see the `inplace=True` argument in some functions. This means that the old DataFrame will get overwritten automatically by whatever you just did.
# 
# THe key: **If you don't save your work, then the Jupyter Notebook will show you a result, but it doesn't get reflected in the DataFrame. So, if you try use what you just did, Python won't know about it!**

# ## Selecting our data
# 
# You access columns in `pandas` like this, using `[]` and `''`. **A column is a variable** in our data set.

# In[7]:


uw['RegionType']


# But, wait, you can also do this! **But, only if the variable name doesn't have spaces.** The method with `['NAME']` is more general and can handle variable names with spaces, like `['Var Name']`. 

# In[8]:


uw.RegionType


# Notice how as you're typing, VS Code is trying to autocomplete for you? Helpful!
# 
# You can also do multiple columns. Use a `,` to separate the column names in `[]`.
# 

# In[9]:


uw[['RegionType', 'RegionName', 'UWHomes_Tier2']]


# You can save the new DataFrame with just those three columns if you want to use it elsewhere.

# In[10]:


uw_only_three_columns = uw[['RegionType', 'RegionName', 'UWHomes_Tier2']]
uw_only_three_columns


# We are using a **list** - the column names are in a list with `[]`. You can also pull out just certain rows. We used `head` and `tail` above to do this in an "automated" way.

# In[11]:


uw[0:10]


# Again, notice how Python starts counting from 0. That 0, 1, 2... shows the current `index` for this `DataFrame`. We could change this and will later.

# ### Using loc
# 
# `pandas` has two **location** methods: `loc` and `iloc`. They are going to let us select parts of our data. The main difference: `loc` is labelled based and `iloc` is location based. 
# 
# Since our columns have labels (our rows do not), we can use `loc` to specify columns by name. If we created an **index** for this data, then our rows would have labels. We'll do that later. Any index for this data will be complicated, since no one column uniquely identifies anything!
# 
# You can read more about the two methods [here](https://towardsdatascience.com/how-to-use-loc-and-iloc-for-selecting-data-in-pandas-bd09cb4c3d79). 
# 
# We'll start with `loc`. Again, our rows don't have labels or an index, so we can use the number of the row, even with `loc`. We can pull just the first row of data.

# In[12]:


uw.loc[0]


# That returned a **series** with just the first row and all of the columns. You can make the output in a Jupyter notebook look a little nicer by turning the series into a DataFrame using `to.frame()`. Again, this is the first row and all of the column headers, just turned sideways.

# In[13]:


uw.loc[0].to_frame()


# Things look more like what you'd expect if you pull multiple rows. This will also mean that we get a DataFrame and not just a series. 
# 
# We can pull the first ten rows and just three columns. But, now we are going to use the column names. And - notice how `0:9` actually gets us `0:9`! Because we are using `loc`, we include the last item in the range.

# In[14]:


uw.loc[0:9,['RegionType', 'RegionName', 'UWHomes_Tier2']]


# We could pull all of the columns and rows 0:9 like this.
# 

# In[15]:


uw.loc[0:9,:]


# 
# We can pull a range for columns too. Again, notice that the column name range is **inclusive of the last column**, unlike with slicing by element number.

# In[16]:


uw.loc[0:9,'RegionType':'UWHomes_Tier2']


# ### Using iloc
# 
# Now, let's try `iloc`. I'll pull the exact same data as above. The numbers used are going to work like slicing. We want to use `0:10` for the rows, because we want the first 10 rows. Same for the columns. Inclusive of the first number, but up to and excluding the second.

# In[17]:


uw.iloc[0:10,0:10]


# We can also select columns in various locations, like above.

# In[18]:


uw.iloc[0:10,[0, 1, 9]]


# ### Comparing four selection methods
# 
# You can use these methods to select and save columns to a new DataFrame. Each of the following does the same thing.

# In[19]:


uw_sub1 = uw[['RegionType', 'RegionName', 'UWHomes_Tier2']]
uw_sub2 = uw.loc[:,['RegionType', 'RegionName', 'UWHomes_Tier2']]
uw_sub3 = uw.iloc[:,[0, 1, 9]]
uw_sub4 = pd.DataFrame(uw, columns = ('RegionType', 'RegionName', 'UWHomes_Tier2'))

print(uw_sub1.equals(uw_sub2))
print(uw_sub2.equals(uw_sub3))
print(uw_sub3.equals(uw_sub4))


# ### Filtering
# 
# Let's try **filtering** our data and keeping just the MSA observations. The text calls this **complex selection**. See pg. 132.
# 
# Here's some [help on filtering](https://datagy.io/filter-pandas/) data with `pandas`.

# In[20]:


uw[uw['RegionType'] == 'MSA'].head(15)


# How about just North Carolina MSAs? I'll use the bigger DataFrame and just show the observations, rather than create a new DataFrame.

# In[21]:


uw[(uw['RegionType'] == 'MSA') & (uw['StateName'] == 'North Carolina')].head(15)


# Notice how I needed to put `()` around each condition. Python is testing to see if each of these are `True` or `False` and then filtering our data accordingly. Pgs. 132 - 135 of our text show you more about this type of **boolean** filtering. You'll also see **masking** in the DataCamp assignments. Here's an example.

# In[22]:


in_nc = (uw['RegionType'] == 'MSA') & (uw['StateName'] == 'North Carolina')
uw[in_nc].head(15)


# The series *in_nc* is a list of True/False values for whether or not an observation meets the criteria. I can then pass that series to the DataFrame *uw*, which will select observations that meet the *True* criteria.
# 
# I can also use `.loc` to filter and then select certain columns.

# In[23]:


uw.loc[(uw['RegionType'] == 'MSA') & (uw['StateName'] == 'North Carolina'), ['RegionType', 'RegionName', 'MSAName', 'AllHomes_Tier1']].head(15)


# Like with the mask above, we can an also define our criteria separately and then include them. 

# In[24]:


my_filter = (uw['RegionType'] == 'MSA') & (uw['StateName'] == 'North Carolina')
my_columns = ['RegionType', 'RegionName', 'MSAName', 'AllHomes_Tier1']
uw.loc[my_filter, my_columns].head(15)


# ## First Look at an Index
# 
# Let's go back to the stock data and work with indices a bit more. Remember how that one had the `Date` as the index?

# In[25]:


prices = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

prices.index


# Now, let's try `loc`, but using our `dtype=datetime` index. We'll pull in the SPX and VIX for just January 2010. 

# In[26]:


prices.loc['2010-01-01':'2010-01-31',['.SPX', '.VIX']]


# You can even see in the output above how `Date` is in a different row than `.SPX` and `.VIX`. The date is not a variable anymore. It is an index.
# 
# This is a much simpler example than the Zillow data. 
# 
# I do a more complicated multi-index, or multi-level, example when looking at reshaping our data.
