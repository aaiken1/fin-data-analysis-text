#!/usr/bin/env python
# coding: utf-8

# # plotly
# 
# We've now seen the basics of plotting with `pandas` and `matplotlib`. Let's try another package, called [plotly](https://plotly.com/python/), that let's us create interactive graphics. To install the Plotly package, you'll need to run this your terminal/command window.
# 
# ```
# conda install -c plotly plotly
# ```
# 
# You should then restart VS Code.
# 
# I won't do a comprehensive overview, but I can show you a couple of examples. We'll look at [Plotly Express](https://plotly.com/python/line-charts/#line-plots-with-plotlyexpress).
# 
# Let's start by getting our stock data back in.

# In[1]:


# Set-up

import numpy as np
import pandas as pd

# This brings in all of matplotlib
import matplotlib as mpl 

# This lets us refer to the pyplot part of matplot lib more easily. Just use plt!
import matplotlib.pyplot as plt

# Bring in Plotly Express
import plotly.express as px

# Bring in Plotly graphic objects
import plotly.graph_objects as go

import plotly.offline as py

# Keeps warnings from cluttering up our notebook. 
import warnings
warnings.filterwarnings('ignore')


# Read in some eod prices and select just the S&P 500
stocks = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True)  

stocks.dropna(inplace=True)  

from janitor import clean_names

stocks = clean_names(stocks)

stocks.info()


# Let's make a simple line graph of prices for Apple. As a reminder, our date is our index in this DataFrame.

# In[2]:


fig = px.line(stocks, x=stocks.index, y='aapl_o', title='Apple Price History')
fig.show()


# Not bad! You can create what `plotly` calls **graphic objects**. You than add **traces**, similar to **axes**, and start to layer things together. Here, we'll create our "blank" figure and then add three more price sequences.

# In[3]:


# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=stocks.index, y=stocks.aapl_o,
                    mode='lines',
                    name='AAPL'))
fig.add_trace(go.Scatter(x=stocks.index, y=stocks.msft_o,
                    mode='lines',
                    name='MSFT'))
fig.show()


# We can create a histogram of returns too. I added a **rug** on the top which helps you see the distribution and outliers better. I am also showing the percentage of observations in a bin, not a count.
# 
# And, I made a bunch of other changes, just to give you an idea of the syntax.

# In[4]:


stocks['aapl_ret'] = np.log(stocks.aapl_o / stocks.aapl_o.shift(1))  

fig = px.histogram(stocks, x='aapl_ret', 
                   marginal="rug", # That thing at the top!
                   histnorm='percent', 
                   opacity=0.75, # alpha
                   width=600, #pixels
                   height=400,
                   template="simple_white")

fig.update_layout(
    title_text='Apple Return Distribution', # title of plot
    xaxis_title_text='Return', # xaxis label
    yaxis_title_text='Percent', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)


fig.show()

