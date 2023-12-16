#!/usr/bin/env python
# coding: utf-8

# # Using SQL in Python
# 
# SQL stands for [Structured Query Language](https://en.wikipedia.org/wiki/SQL) and is perhaps the number one tool that any data analyst needs to know. Well, after Excel I guess. Everyone assumes that you know Excel.
# 
# You can use SQL everywhere. This is the OG database language. There are many different iterations. But, they all let you create databases and do the standard ETL (extract, transform, and load) [processes](https://blog.panoply.io/sql-and-etl-the-dynamic-data-duo). They key - there are standard SQL ways to do things. If you know the terms and ideas, you can use them across a variety of platforms and languages.
# 
# SQL is used for [relational, structured databases](https://en.wikipedia.org/wiki/Relational_database), where there are keys that uniquely identify observations and where the data is the traditional column/variable format. Basically, the data that we are using.
# 
# ```{note}
# If you're doing data science, business analytics, anything that involves something bigger than a financial model in Excel, learn SQL.
# ```
# 
# However, databases have changed a lot the last 25 years or so, as companies deal with more and more data with limited structure. These tools, broadly speaking, are sometimes called [NoSQL](https://en.wikipedia.org/wiki/NoSQL). This is beyond the scope of what we're doing, but would be taught in any data engineering or databases course.
# 
# If you'd like to learn more about SQL, there are also some [DataCamp](https://www.datacamp.com/learn/sql) tutorials. 
# 
# And here's the [cheat sheet](https://res.cloudinary.com/dyd911kmh/image/upload/v1675360372/Marketing/Blog/SQL_Basics_For_Data_Science.pdf).
# 
# I found this [page helpful for some syntax](https://towardsdatascience.com/pandasql-interesting-way-to-run-sql-queries-in-python-18a4fc36406a). 
# 
# ## Pandas SQL
# 
# We are going to use [pandassql](https://pypi.org/project/pandasql/) to use SQL in Python. Using this method will let use use **standard SQL queries** with our `pandas` DataFrames. If you already know SQL, you might like this better!
# 
# I'll use `pip` to install `pandassql`. Don't forget to use `! pip` in Google Colab.
# 
# ```
# pip install pandasql 
# ```
# 
# This is a much "lighter weight" way to use SQL. There are others, like [pyspark](https://spark.apache.org/docs/latest/api/python/index.html) from [Apache Spark](https://spark.apache.org) that are whole set of data engineering tools.
# 
# You'll see my import statement below. 
# 
# I'll also bring in that NC Brewery data.

# In[1]:


# Set-up

from pandasql import sqldf

import numpy as np
import pandas as pd

nc_df = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/ncbreweries.csv')


# From here, you can use the standard set of SQL queries. I won't go over all of them. Let me give you a few examples, though, so that you can see what things look like. 
# 
# Let's start by turning this DataFrame into a SQL database.

# In[2]:


nc = sqldf("SELECT * FROM nc_df")

nc


# Can't tell a difference from the output, right? If you've used SQL before, though, you should start to feel at home. 
# 
# Here's a standard query. Again, I'm not going over all of SQL here, but you can probably read this and figure out what it is doing. I print the query at the end. It is traditional in SQL to put the **actions** in all caps.

# In[3]:


q = """SELECT 
      Type as brewery_type, City as city, AVG("Beer Count") as avg_beer_count 
      FROM 
         nc 
      GROUP BY 
         City
      ORDER BY
         City;"""

print(q)


# We can then run this query and save it to a new DataFrame.

# In[4]:


nc2 = sqldf(q)
nc2


# In[5]:


type(nc2)


# In short, if you have SQL that you want to run, it is easy enough to copy and paste it into Python!
