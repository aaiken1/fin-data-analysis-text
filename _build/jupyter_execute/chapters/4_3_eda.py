#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis (EDA)
# 
# Exploratory data analysis, or **EDA**, means just that. We are going look at and summarize our idea. The data cleaning that we've already done, the looking for missings and understanding our variables, is actually part of EDA. In these notes, however, we'll focus on **grouping**, or **aggregating**, and summarizing our data.
# 
# This type of data work is sometimes called **split-apply-combine**, where we split, or **group** our data, apply a function (e.g. mean), and then combine the summary statistics back together.
# 
# We are starting to **ask questions** of our data. For example,
# 
# - What variables do we have and what are their data types? Are they numeric or text?
# - Which variables are **continuous**? Which are **discrete**?
# - Are any variables **categorical**? These variables might be either numeric or text. 
# - Do we have any **datetime** variables?
# - How are our variables related to each other?
# - How can we **summarize** them?
# 
# We'll graphically summarize our data in the [next section](#dataviz). We'll look more at **datetime** variables when we get to our work on [financial time series](#financial-times-series). 
# 
# We want to eventually be able to open up a new data, see what questions **can be answered**, and then have the tools to actually **answer the questions**. Sometimes we want to ask questions that data can't answer - we need to recognize when that's the case too.
# 
# [DataCamp](https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python), of course, has a tutorial on some EDA ideas, perhaps more related to what people are doing in machine learning.
# 
# [Chapter 10](https://wesmckinney.com/book/data-aggregation.html) of *Python for Data Analysis* discusses aggregation and summarizing our data. 
# 
# [Exploratory Data Analysis](https://aeturrell.github.io/coding-for-economists/data-exploratory-analysis.html) from *Coding for Economists* has data aggregation and summary examples. That chapter also covers the logic of opening up a data set and seeing what you have to work with. I am following along with a lot of that material in these notes.
# 

# ## Set-up
# 
# Let's bring in some data on NC breweries. We'll again use my Github URL to download the data directly: <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/ncbreweries.csv>. 
# 
# We'll bring in our usual libraries. I'll also use `pyjanitor`, in case we need to clean anything.
# 
# I'll name the DataFrame **nc**. 

# In[1]:


# Set-up
import numpy as np
import pandas as pd
import janitor

nc = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/ncbreweries.csv')
nc.info()


# Looks pretty good. I'll use `pyjanitor` to clean up the variable names and get rid of any spaces and capitalizations. We're transforming them into something called **snake case**, which gets rid of capital letters and uses "_" as spaces.

# In[2]:


nc = nc.clean_names()
nc.info()


# See what it did? Let's take a peak at the first few rows.

# In[3]:


nc.head()


# 
# We can also change the data types. For example, let's get brewery *type* to be something called a **category**. Categories tell `pandas` that some of your variables are in discrete groups. This will be helpful when working with our data. I'll also change a few others to be **strings**. They were **objects** before, which `pandas` can work with as text, but might as well tell `pandas` that we want text.

# In[4]:


nc = nc.assign(
    name=nc['name'].astype('string'),
    city=nc['city'].astype('string'),
    type=nc['type'].astype('category'),
    status=nc['status'].astype('category'),
    url=nc['url'].astype('string'),
)

nc.info()


# I'm using a method called `assign()` that creates (assigns) a new column. In this case, I'm creating new *name*, *city*, etc. variables from the existing ones, but am changing their type as I go. 
# 
# Notice this new type of syntax I'm using. `assign()` can create more than one new column at once. I've put each new column on a new line with proper indentation. It will still run without that indentation, but the spacing makes it much easier to read. 
# 
# Finally, let's just check for missing data. Doesn't seem like we have any from that `info()`.

# In[5]:


nc.isna().sum()


# ## Exploring NC breweries
# 
# We'll start with `describe()`. The will give us summary statistics for our numeric variables.

# In[6]:


nc.describe()


# Anything stand out to you? The variable *est* is the year that the brewery was established. The minimum is 1900. That seems very early? Is that right? A beer count of 424 seems high, but could be right.
# 
# We can make that table look a little better.

# In[7]:


sum_table = nc.describe().round(1)
sum_table


# We can **select** just a single column to describe.

# In[8]:


sum_table_beer = nc['beer_count'].describe().round(1)
sum_table_beer


# This doesn't look as good, right? It's because, by picking out just that one column, we've created a `pandas` **series**, rather than a **DataFrame**.

# In[9]:


type(sum_table_beer)


# We can make it a DataFrame again using `.to_frame()`

# In[10]:


sum_table_beer.to_frame()


# Going back to the original summary DataFrame, we can flip things around, or **transpose**, the table to make it look better. This is usually how summary statistics are presented.

# In[11]:


sum_table = sum_table.T
sum_table


# Let's look at the variable *type*. What types of breweries are in our data? We can use `.value_counts()` to do counts by category.

# In[12]:


nc['type'].value_counts()


# Mainly microbreweries. 
# 
# ### Group and .agg
# 
# I wonder what type of brewery has the largest number of beers on average? This is where we can start using the idea of **split-apply-combine**.

# In[13]:


nc.groupby('type')['beer_count'].mean()


# This code is **grouping** our data by *type*, pulling out *beer_count*, and calculating the mean.
# 
# ```{note}
# You first group by your variables. Then, you need to tell Python what variable you want to aggregate. For grouping by more than one variable, you need to use a **list** inside of the `()`. 
# ```
# 
# We can use the `.agg` method to include more than one summary statistic. The `np.` means that the function is being pulled from the `numpy` package. Pay attention to the syntax - there are no `()` after the `np.mean`, `np.median`, and `np.std` functions now, because they are being used inside of the `.agg` function. They are also grouped together with `[]` as a **list**.
# 
# The `.agg` function is the same thing as `.aggregate`, which you'll see in our textbook.
# 
# You could also pull multiple columns to summarize, but this data set really only has one numeric variable of interest. 

# In[14]:


nc.groupby('type')['beer_count'].agg([np.mean, np.median, np.std]).round(1) 


# An interesting Python note: See how I used `np.` inside of `.agg`? This tells `.agg` that I am passing a function from `numpy`, like `np.mean`. You can also use the **name** of the function and pass the arguments `'mean'`, `'median'`, and `'std'` to `.agg`. You might see that if you're looking at other examples.
# 
# I also added that `round(1)` to get only one decimal place. You can also make your table and then style it in separate lines. This code will style **just that table**. You can also set global style options that will affect all of your results.
# 

# In[15]:


sum_table_group = nc.groupby('type')['beer_count'].agg([np.mean, np.median, np.std])

sum_table_group.style.format(precision=0, na_rep='-')


# The code above reads from left to right. You do something, have a `.`, do something else, etc. For example, we are taking the DataFrame **nc**, grouping it by *type*, pulling out *beer_count*, and then aggregating using three different statistics. I am saving this to a **new DataFrame**, called **sum_table_group**. Finally, I am using `style.format` to change the look at the DataFrame that is being displayed as a table in out notebook.
# 
# We can also change the column header names if we want. Here's the same code, but with `.rename()`. Note that the way the DataCamp renames columns inside of the `.agg()` function is no longer recommended by `pandas`. 

# In[16]:


sum_table_group = nc.groupby('type')['beer_count'].agg([np.mean, np.median, np.std]).rename(columns={'mean': 'avg', 'median': '50th', 'std': 'sigma'})

sum_table_group.style.format(precision=0, na_rep='-')


# 
# Let's look at how to do this using some different syntax. Something more vertical. Note that `()` surrounding all of the code.

# In[17]:


(
    nc.groupby('type')
    .mean()['beer_count']
    .to_frame()
    .style
        .format(precision=0)
        .set_caption('Beer Count by Brewery Type')   
)


# We are starting with the **nc** DataFrame and grouping by *type*. I am calculating the mean of *beer_count*. This actually creates a **series**, not a DataFrame. You can't style a series and make it look good in your output. So, I use `to.frame()` to put it back into a DataFrame that can be styled. I then use different style functions on that DataFrame. Both `format` and `set_caption` are functions found as part of `style`. 
# 
# I can also use the `.agg` function in this way. I'll again pass the list of `numpy` functions for `.agg` to use when summarizing the *beer_count* variable. Now, note that `.agg` creates a DataFrame, not a series, so I don't need the `to.frame()` in there to get back to a DataFrame for styling.
# 
# ```{note}
# It's important to keep track of the data types that functions expect and the types that they return. What goes in and what comes out?
# ```

# In[18]:


(
    nc.groupby('type')
    .agg([np.mean, np.median, np.std])['beer_count']
    .rename(columns={'mean': 'avg', 'median': '50th', 'std': 'sigma'})
    .style
        .format(precision=0)
        .set_caption('Beer Count by Brewery Type')   
)


# ### Grouping by more than one variable
# 
# Let's go back to just the mean. I'll group by **two variables** now. We give `.groupby()` a **list** of what to group by. Note the square brackets.

# In[19]:


nc.groupby(['type', 'status'])['beer_count'].mean().to_frame()


# That looks pretty good. You can see the two columns being used as groups.
# 
# Let's style this table a bit more. The first line groups, creates the means, and puts all of this back into a DataFrame. The second line formats the DataFrame.
# 
# The summary DataFrame, *sum_table_mean*, **is our table**. 

# In[20]:


sum_table_mean = nc.groupby(['type', 'status'])['beer_count'].mean().to_frame()

sum_table_mean.fillna('-').style.format(precision=0).set_caption('Beer Count by Brewery Type and Status')


# We can try our more vertical style too.

# In[21]:


(
    nc.groupby(['type', 'status'])
    .mean()['beer_count']
)


# See how that doesn't look as good? We've made a series again. We need to make it a DataFrame and style it.

# In[22]:


(
    nc.groupby(['type', 'status'])
    .mean()['beer_count']
    .to_frame()
    .fillna('-')
    .style
        .format(precision=0)
        .set_caption('Beer Count by Brewery Type and Status')
)


# ### GroupBy objects
# 
# We've been splitting our data into groups. Let's look at `GroupBy` objects themselves. These are created by the `groupby` function. Our textbook discusses these, starting pg. 130. Essentially, it's another way of doing what we've already done in these notes.
# 
# Let's create a `GroupBy` object with the brewery data and take an look.

# In[23]:


nc_groups = nc.groupby('type')
print(type(nc_groups))
print(nc_groups.size())


# This `GroupBy` object has all of our data, but grouped by *type*. We can calculate the mean of all numeric data in the `GroupBy`. 

# In[24]:


nc_groups.mean()


# We can also use `.agg` again to get multiple statistics. I'll put out just *beer_count* and get the sum, mean, min, and max by group *type*. So, very similar to above, but now we are dealing with a DataFrame that's "pre-grouped" in a sense. Also, note again how I use `np.mean`, but just `sum`. The `sum` function is base Python, but `mean` comes from `numpy`, so I need the `np.mean`. 

# In[25]:


nc_groups['beer_count'].agg([sum, np.mean, min, max])


# ## Outliers
# 
# Our summary statistics can give us a sense of the **distribution of the data**. We'll be plotting the actual distributions in the coming chapters. Sometimes, we might want to work with just a portion of the data, after removing some extreme examples. 
# 
# We'll go back to the original *nc* data, before we grouped it. I'll **mask**, or **screen**, for only active breweries and then only keep the breweries with a beer count less than the 95th percentile threshold. 

# In[26]:


nc = nc[nc['status'] == 'Active'] # Active breweries only
outliers = nc['beer_count'].quantile(.95) # Outlier threshold is at the 95th percentile of beer count
outliers


# The 95th percentile of beers on tap is 123.75. Let's only keep breweries with fewer beers than that. I won't save the DataFrame, but I'll sort it so that you can see that the outliers have been removed.

# In[27]:


nc[nc['beer_count'] < outliers].sort_values(by='beer_count', ascending=False) # Remove outliers


# ## skimpy
# 
# Adding in some new libraries really lets us see why using something like Python can improve our workflow. The `skimpy` library gives us a nice summary of our data. We can install `skimpy` via Anaconda. To use this package, you'll need to type the following in the terminal (Mac) or command prompt (Windows). You'll need to restart VS Code.
# 
# ```
# python -m pip install skimpy
# ```
# 
# This *should* install skimpy in your Anaconda distribution of Python. Remember, you actually have several versions of Python on your computer. This is why you have that choice of Python kernel when you're running code.
# 
# I'm going to bring back the Zillow **uw** DataFrame, just because it has more variables to look at. 
# 
# You can read about this package [here](https://aeturrell.github.io/skimpy/). 

# In[28]:


import pandas as pd
from skimpy import skim

uw = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/zestimatesAndCutoffs_byGeo_uw_2017-10-10_forDataPage.csv')

skim(uw)


# ## pandas profiling
# 
# If you want something more in-depth, try `pandas-profiling`. We can install `pandas-profiling` via Anaconda. To use this package, you'll need to type the following in the terminal (Mac) or command prompt (Windows). You'll need to restart VS Code.
# 
# ```
# conda install -c conda-forge pandas-profiling
# ```
# 
# You can [read all about it on their Github page](https://github.com/pandas-profiling/pandas-profiling). It's ridiculous what it can do. 
# 
# Let's add the `import` needed to bring `ProfileReport` from `pandas_profiling`.

# In[29]:


from pandas_profiling import ProfileReport


# This will create the report.

# In[30]:


profile = ProfileReport(uw, title='Zillow Housing Data for Flood Risk', minimal=True)


# We can now view the report in a Jupyter widget. It will take a couple of minutes to summarize everything. 

# In[31]:


#profile.to_widgets()


# You can also create an HTML file. Using the code below, the file will end up in the same folder as your `.ipynb` notebook. I've commented it out so that it doesn't run and create large file everytime.

# In[32]:


#profile.to_file("nc_profile.html")


# Finally, I'll create a profile that will appear in this `.ipynb`.

# In[33]:


profile.to_notebook_iframe()

