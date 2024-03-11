#!/usr/bin/env python
# coding: utf-8

# # seaborn
# 
# We will start our very broad discussion of data visualization with [seaborn](https://seaborn.pydata.org). `seaborn` is based on `matplotlib`, but is "higher-level" (i.e. easier to use) and makes what many consider nicer looking graphs (i.e. many = me). 
# 
# So, why do we still look at `matplotlib`? I think it is good to see `matplotlib`, since it is the most popular way to create figures in Python. But, you should take a look at `seaborn` as well.
# 
# [Some people](https://www.emilyriederer.com/post/py-rgo/), especially those coming to Python from other languages, are suggesting that you just start with `seaborn` instead.
# 
# `seaborn` comes with Anaconda and Github Codespaces, so there's nothing to install. Just add `import seaborn as sns` to your set-up and you're ready to go. In my set-up, I'll set a theme, so that the same theme is used across all of my graphs. I'll create my returns directly in the **stocks** DataFrame.
# 
# DataCamp has a [seaborn tutorial](https://www.datacamp.com/community/tutorials/seaborn-python-tutorial) as well.
# 
# There's an [example gallery](https://seaborn.pydata.org/examples/index.html) as well.
# 
# You can find other examples [here](https://pythonforfinance.net/2018/07/22/seaborn-module-and-python-distribution-plots/).
# 
# Finally, I'm going to use the `df.var_name` convention for pulling out variables from a DataFrame. I find it easier than `df['var_name']`. I'll go back and forth in the notes, to get you use to the different styles.
# 

# In[1]:


# Set-up
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="white")

# Include this to have plots show up in your Jupyter notebook.
get_ipython().run_line_magic('matplotlib', 'inline')

# Read in some eod prices
stocks = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True)  

stocks.dropna(inplace=True)  

from janitor import clean_names

stocks = clean_names(stocks)

stocks['aapl_ret'] = np.log(stocks.aapl_o / stocks.aapl_o.shift(1))  
stocks['msft_ret'] = np.log(stocks.msft_o / stocks.msft_o.shift(1))  

stocks.info()


# If you don't have `janitor` installed, you'll need to run in a code cell above your set-up code. You should only have to install a package once per code space.
# 
# ```
# pip install pyjanitor
# ```
# 
# You can read more about `janitor` [here](https://pyjanitor-devs.github.io/pyjanitor/#installation).

# Let's start with a line plot. We'll plot just AAPL to start.

# In[2]:


sns.lineplot(x=stocks.index, y=stocks.aapl_o)
plt.show();


# We can also make a distribution, or histogram, as well. I'll add what's called the **kernel density estimate** (kde), which gives the distribution. We'll do more data work like this when thinking about **risk**.

# In[3]:


sns.displot(stocks.aapl_ret, kde=True, bins=50)
plt.show();


# In[4]:


sns.jointplot(x=stocks.aapl_ret, y=stocks.msft_ret)
plt.show();


# In[5]:


sns.jointplot(x=stocks.aapl_ret, y=stocks.msft_ret, kind='hex')
plt.show();

