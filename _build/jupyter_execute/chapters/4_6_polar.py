#!/usr/bin/env python
# coding: utf-8

# # polars: A fast, fancy pandas alternative
# 
# Most data folks use `pandas`. However, there is an alternative that I just wanted to bring to your attention. [polars](https://www.pola.rs) is a faster and, perhaps, more modern way to handle data in Python. Still, `pandas` is ubiquitous, so I wanted to start with that. 
# 
# Here's the [user's guide](https://pola-rs.github.io/polars-book/user-guide/). I'm not going to go through every command here. As always, think about what you want to do. Sketch it out. Then, look for the syntax to do the job.
# 
# Why not use `pandas`? Here's the [author of pandas](https://wesmckinney.com/blog/apache-arrow-pandas-internals/) on why `pandas` isn't always the best tool for data manipulation. We're getting more advanced here, worrying about speed, being closer to the "metal", etc. 
# 
# [Some people](https://www.emilyriederer.com/post/py-rgo/), especially those coming to Python from other languages, are suggesting that you just start with `polars` instead.
# 
# [Coding for Economists] discusses alternatives to `pandas`, like `polars`.
# 
# We can insall `polars` using `pip` the usual way. Don't forget to use `! pip` in Google Colab.
# 
# ```
# pip install polars
# ```
# 
# You'll see my basic import statement below.

# In[1]:


# Set-up

import polars as pl
import numpy as np
import pandas as pd

df = pl.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/ncbreweries.csv')

type(df)


# See what I did there? That was `pl.read_csv` from `polars`. I've created a `polars` DataFrame.
# 
# Now, you can read the manual to find out all of things that you can do!

# In[2]:


df.describe()


# Looks a little different. I like it.
# 
# You can select certain columns, as well. You can filter, do "group bys". All the usual things.

# In[3]:


df.select(
    pl.col(['Name', 'City'])
)


# In[4]:


df.filter(
    pl.col("Beer Count").is_between(10, 100))


# In[5]:


df.filter(
    (pl.col('Beer Count') <= 10) & (pl.col('Status') != "Closed")
)


# In[6]:


df.groupby("Type").count().sort(by="count", descending=True)


# Not bad!
