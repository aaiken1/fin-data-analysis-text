#!/usr/bin/env python
# coding: utf-8

# # Using ChatGPT
# 
# There are now many AI-based tools to help us code. These tools can create code outlines for us, check our own code, write functions, and explain the steps. I'm going to show you a few examples using the free [OpenAI ChapGPT tools](https://chat.openai.com).
# 
# If you use Github and VS Code, you can sign-up for [CoPilot](https://github.com/features/copilot/). 
# 
# This paper by [Liu, Miller, and Niu (2023)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4412371) has some great examples of how to use ChatGPT in a course like this one.
# 
# ## Using GPT to Write a Function For You
# 
# Let's go back to Chapter 7, where I showed you how to write a function to generate asset paths using **geometric brownian motion**. We used the Nasdaq API to bring in some bitcoin data in that example. Now, I'm going to use ChatGPT to write the same function. I gave GPT4 the following prompt:
# 
# > Write a function in Python that simulates geometric brownian motion for any number of assets. Create the appropriate inputs as arrays. The inputs should be the number of assets, the mean for each asset, the standard deviation for each asset, the number of periods, the initial value of each asset, and the number of simulations. The output should be an array that contains all of the simulations for each asset. These are uncorrelated assets, so don't worry about covariance.
# 
# Here's the code that it gave me:

# In[1]:


import numpy as np

def geometric_brownian_motion(num_assets, means, std_devs, num_periods, initial_values, num_simulations):
    if len(means) != num_assets or len(std_devs) != num_assets or len(initial_values) != num_assets:
        raise ValueError("The length of means, std_devs, and initial_values should be equal to the number of assets")

    # Initialize an array to store the simulations
    simulations = np.zeros((num_simulations, num_periods + 1, num_assets))

    # Set the initial values for each simulation
    simulations[:, 0, :] = initial_values

    # Time step
    dt = 1.0

    # Loop through each simulation
    for sim in range(num_simulations):
        # Loop through each time period
        for t in range(1, num_periods + 1):
            # Loop through each asset
            for asset in range(num_assets):
                # Generate a random normal value (using mean=0 and std_dev=1) for the brownian motion
                random_normal = np.random.normal(0, 1)

                # Calculate the change in asset value using geometric brownian motion
                change = means[asset] * dt + std_devs[asset] * np.sqrt(dt) * random_normal

                # Update the asset value
                simulations[sim, t, asset] = simulations[sim, t - 1, asset] * np.exp(change)

    return simulations

# Example usage
num_assets = 3
means = np.array([0.05, 0.06, 0.07])
std_devs = np.array([0.1, 0.12, 0.14])
num_periods = 100
initial_values = np.array([100, 120, 140])
num_simulations = 1000

simulations = geometric_brownian_motion(num_assets, means, std_devs, num_periods, initial_values, num_simulations)
print(simulations)


# Here's the GPT explanation of the code.
# 
# > This function accepts the following inputs:
# 
# > num_assets: the number of assets \
# means: a NumPy array containing the mean return for each asset \
# std_devs: a NumPy array containing the standard deviation of return for each asset \
# num_periods: the number of time periods \
# initial_values: a NumPy array containing the initial value for each asset \
# num_simulations: the number of simulations to run
# 
# > The function returns a 3D NumPy array containing the simulations for each asset, with dimensions (num_simulations, num_periods + 1, num_assets).

# Let's look a bit more at the output. I'll get its `.shape` attribute.

# In[2]:


type(simulations)


# In[3]:


simulations.shape


# The output is a **three-dimensional array**. We can pull out all of the simulations for one asset, as well as a single simulation for one asset. Or anything else.

# In[4]:


# All simulations for the first asset.
simulations[:,:,0]


# In[5]:


# All simulations for the second asset.
simulations[:,:,1]


# In[6]:


# First simulation for the first asset

simulations[0,:,0]


# Compare this code to the one we used above. What's different? What stands out to you? What assumptions did it make? What's up with these numbers?
# 
# GPT is quite good at creating code that has been done in a lot of places. It has trained on millions of online tutorials and examples. However, you still want to follow the logic and check for errors. **There will be errors.**
# 
# **You can have a "dialog" with GPT.** Look at the code. Is it what you want? You can ask it to change it for you.
# 
# **What does that leave for us to do?** Use GPT to start sketching your code, do to certain tasks. Figure out what you need. Figure out the questions that you're trying answer. What's the problem that you're trying to solve? Who are you solving it for? What will the answer look like? What will it tell you?
# 
# Using tools like GPT, Github Co-Pilot, etc. is like having a team of junior programmers working for you. They can make the job easier, but it is still up to you to know what's an interesting question in the first place. **You still need to use your domain expertise and creativity to come up with solutions to problems that aren't in an online Python tutorials.**

# ## Using ChatGPT to Check Our Code
# 
# Below, I have borrowed some code from our portfolio optimization code. However, there is one small problem, based on one I encountered in class. One of those small, tiny errors that can be so frustrating! Do you see it?

# In[7]:


# Read in some eod prices
import numpy as np
import pandas as pd

from pylab import mpl, plt

import scipy.optimize as sco

raw = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True).dropna() 

symbols = ['AAPL.O', 'MSFT.O', 'SPY', 'GLD'] #two stocks and two ETFs

noa = len(symbols) #noa = number of assets

data = raw[symbols]

rets = data.pct_change().dropna()

noa = 4

weights = np.random.random(noa)
weights /= np.sum(weights)

ann_rets = rets.mean() * 252

def port_ret(weights):
    return np.sum(ann_rets * weights)

def port_vol(weights):
    return np.sort(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))

def sharpe(weights):  
    return port_ret(weights) / port_vol(weights)  

sharpe(weights)


# Huh... Let's see if ChatGPT can help us out. I'm going to copy and paste the code and ask it to find the mistake. It does!
# 
# ```{figure} ../images/17-gpt-find-error.png
# ---
# name: 17-gpt-find-error.png
# align: center
# class: with-border
# ---
# You can use ChatGPT to find errors in your code.
# ```
