#!/usr/bin/env python
# coding: utf-8

# # Regression topics
# 
# This section will go into more detail on running regressions in Python. We already saw an example using [factor models](10_factor_models.html#factor_models), like the CAPM and Fama-French 3-factor models. 
# 
# We could spend an entire semester going over linear regression, how to put together models, how to interpret models, and all of the adjustments that we can make. In fact, this is basically what a first-semester Econometrics class is!
# 
# I will be following code examples from [Coding for Economists](https://aeturrell.github.io/coding-for-economists/econmt-regression.html), which has just about everything you need to know to do basic linear regression (OLS) in Python. I recommend giving it a read, especially if you've taken econometrics and have already seen the general ideas.
# 
# [The Effect](https://theeffectbook.net) great book for getting starting with econometrics, regression, and how to add meaning to the regressions that we're running. [Chapter 13](https://theeffectbook.net/ch-StatisticalAdjustment.html) of that book covers regression (with code in R).
# 
# You can read more about [statsmodels on their help page](https://www.statsmodels.org/dev/regression.html).
# 
# I'll be using our Zillow pricing error data in this example.

# In[1]:


import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

pd.options.display.max_columns = None


# In[2]:


housing = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/properties_2016_sample10_1.csv')
pricing = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/train_2016_v2.csv')

zillow_data = pd.merge(housing, pricing, how='inner', on='parcelid')
zillow_data['transactiondate'] = pd.to_datetime(zillow_data['transactiondate'], format='%Y-%m-%d')


# In[3]:


zillow_data.describe()


# I'll print a list of the columns, just to see what our variables are. There's a lot in this data set.

# In[4]:


zillow_data.columns


# Let's run a really simple regression. Can we explain pricing errors using the size of the house? I'll take the natural log of `calculatedfinishedsquarefeet` and use that as my independent (**X**) variable. My dependent (**Y**) variable will be `logerror`. I'm taking the natural log of the square footage, in order to have what's called a "log-log" model.

# In[5]:


zillow_data['ln_calculatedfinishedsquarefeet'] = np.log(zillow_data['calculatedfinishedsquarefeet'])

results = smf.ols("logerror ~ ln_calculatedfinishedsquarefeet", data=zillow_data).fit()


# In[6]:


print(results.summary())


# That's the full summary of the regression. This is a "log-log" model, so we can say that a 1% change in square footage leads to a 1.39% increase in pricing error. The coefficient is positive and statistically significant at conventional levels (e.g. 1%). 
# 
# We can pull out just a piece of this full result if we like. 

# In[7]:


results.summary().tables[1]


# We can, of course, include multiple **X** variables in a regression. I'll add bathroom and bedroom counts to the regression model.

# In[8]:


results = smf.ols("logerror ~ ln_calculatedfinishedsquarefeet + bathroomcnt + bedroomcnt", data=zillow_data).fit()
print(results.summary())


# Hey, all of my significance went away! Welcome to the world of [multicollinearity](https://en.wikipedia.org/wiki/Multicollinearity). All of these variables are very correlated, so the coefficient estimates become difficult to interpret.
# 
# Watch what happens when I just run the model with the bedroom count. The $t$-statistic is quite large again.

# In[9]:


results = smf.ols("logerror ~ bedroomcnt", data=zillow_data).fit()
print(results.summary())


# ## Indicators and categorical variables
# 
# The variables used above are measured numerically. Some are **continuous**, like square footage, while others are **counts**, like the number of bedrooms. Sometimes, though, we want to include an **indicator** for something? For example, does this house have a pool or not?
# 
# There is a variable in the data called `poolcnt`. It seems to be either missing (NaN) or set equal to 1. I believe that a value of 1 means that the house has a pool and that `NaN` means that it does not. This is bit of a tricky assumption, because `NaN` could mean no pool or that we don't know either way. But, I'll make that assumption for illustrative purposes.

# In[10]:


zillow_data['poolcnt'].describe()


# I am going to create a new variable, `pool_d`, that is set equal to 1 if `poolcnt >= 1` and 0 otherwise. This type of 1/0 categorical variable is sometimes called an **indicator**, or **dummy** variable. 

# In[11]:


zillow_data['pool_d'] = np.where(zillow_data.poolcnt.isnull(), 0, zillow_data.poolcnt >= 1)
zillow_data['pool_d'].describe()


# I can then use this 1/0 variable in my regression.

# In[12]:


results = smf.ols("logerror ~ ln_calculatedfinishedsquarefeet + pool_d", data=zillow_data).fit()
print(results.summary())


# Pools don't seem to influence pricing errors. 
# 
# We can also create more general **categorical** variables. For example, instead of treating bedrooms like a count, we can create new categories for each number of bedrooms. This type of model is helpful when dealing states or regions. For example, you could turn a zip code into a categorical variable. This would allow zip codes, or a location, to explain the pricing errors. 
# 
# In Python, you can turn something into a categorical variable by using `C()` in the regression formula. 
# 
# I'll try the count of bedrooms first.

# In[13]:


results = smf.ols("logerror ~ ln_calculatedfinishedsquarefeet + C(bedroomcnt)", data=zillow_data).fit()
print(results.summary())


# And here are zip codes as a categorical variable. This is saying: Is the house in this zip code or no? If it is, the indicator for that zip code gets a 1, and a 0 otherwise. If we didn't do this, then the zip code would get treated like a numerical variable in the regression, like square footage, which makes no sense!

# In[14]:


results = smf.ols("logerror ~ ln_calculatedfinishedsquarefeet + C(regionidzip)", data=zillow_data).fit()
print(results.summary())

