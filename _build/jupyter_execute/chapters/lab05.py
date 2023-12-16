#!/usr/bin/env python
# coding: utf-8

# # Lab 05
# ## Simulation and Macroeconomic data
# 
# In this lab, we'll start with a simulation. Then, we are going to use macroeconomic data that you'll download from Nasdaq Data Link. We'll review a lot of the **time series** work from our notes and DataCamp assignments. I'll also show you how to **melt** your data. Yup, that's right.
# 
# Use our online notes to complete our labs. I have my own commentary and links that will help. You can work through the parts below in order. 
# 
# If you are getting errors and are not sure why, my first suggestion is always to **Restart** the Python kernel, to **Clear All Output**, and run each code cell **one-by-one** from the top.
# 
# ```{margin}
# My instructions will refer to VS Code, but you can use VS Code, Anaconda Jupyter notebook, or Google Colab. The key is have a Jupyter notebook when you're done that can run from start to finish. 
# ```
# 
# Let each code cell represent one idea, or output. Take advantage of **Markdown** in your write-up. Use headers and formatting. Here's a [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) that I keep handy. Once you figure out some of the basics, you might not want to go back to Word or Google Docs.
# 

# ## Part 1
# 
# Open up VS Code or Google Colab. Have you set up your class folder yet? I've posted a video that will help you figure that part out. Open up that folder under File. If you're in VS Code, you should see it in the **EXPLORER** window pane on the left. 
# 
# Type **Cmd-Shift-P** (Ctrl-Shift-P in Windows) to open up the command palette. Make sure there's a little `>` in the search bar that pops up (there should be). Search for `Jupyter: Create New Jupyter Notebook`. This will open up a blank `.ipynb` file. Save this in a new folder in your course folder called `lab05`. Call this file `lab05-lastname-firstname`, where you fill in your name, of course! 
# 
# If you're using Anaconda Jupyter notebooks or Google Colab, you'll do something very similar. Create a new `.ipynb` file. In Google Colab, this file will be saved to your Google Drive. You can then download it when you're done. See the online notes for more on using Google Colab. 

# ## Part 3
# 
# You'll see a blank code cell, or **cell**, at the top. By default, this is set to Python. See the lower right-hand corner of the cell? Click there and search and select **Markdown**. 
# 
# Create the following in that top Markdown cell.
# 
# ```
# # Lab05
# 
# Firstname Lastname
# 
# Date
# ```
# 
# As you answer the questions below, use new Markdown cells and headers to separate your answers, as appropriate.
# 
# Create your first code cell where you `import` both `numpy` and `pandas` as `np` and `pd`, respectively. 
# 
# Also include `import datetime as dt`. The `datetime` library is discussed in the first part of the second DataCamp assignment.
# 
# Include `from datetime import timedelta` and `import seaborn as sns`. Rememebr seaborn? You see it occasionally in the DataCamps too.
# 
# Finally, include `import nasdaqdatalink`. If you have not installed `nasdaq-data-link`, follow the instructions in our notes.
# 
# You can read more at: <https://data.nasdaq.com>
# 
# Add a **comment** to that cell calling it **Set-Up**. You can add comments to each code cell to remind yourself what you're doing. Comments are different from the Markdown that you're using to write your narrative - they go in the Python cells and use `#`. 

# ## Part 4
# 
# We have some notes on **simulating stock prices** using geometric brownian motion. Use these methods to create 100 simulations for 30 days of prices for *AAPL* and *TLT*. Use the last price in the data for each as the initial starting price. Make some graphs. How do they compare? Why are they different? What exactly is *TLT*?
# 
# To do this, you'll need to go back to Lab 04 and bring in the price and return data from the end. Be sure that you use the adjusted price. **Don't copy and paste all of the code!** Just use what you need.

# ## Part 5
# 
# Create three code cells to bring in and clean three separate data series: 'FRED/GDP', 'UMICH/SOC1', and 'FRED/UNRATE'.
# 
# Here's some code to get you started:
# 
# ```
# gdp = nasdaqdatalink.get('FRED/GDP')
# ```
# 
# **What are these data series? I'll bet you guess two of them!**
# 
# OK, now we have to pay attention to what we have. We'll use some of the ideas from the DataCamps. 
# 
# Take a look at the GDP data first. It is **quarterly data**. And, do you see how the date is on the first of each quarter? We're going to want that date to actually be the last day of the previous month (i.e. one day prior). Why? It is customary to use end-of-month (eom) data when dealing with economic indicators, stock data, etc. This will also help us **merge** our data, as you'll see below.
# 
# When you bring this data in from Nasdaq, the **date is the index**. As we've seen, you can access the index by using something like `df.index`, like how you would select a column from a DataFrame. 
# 
# Do the following:
# - Alter the index so that it is one day prior. We'll use the method `timedelta` from the `datetime` library. Modify this code:
# - 
# ```
# ______ = ______ - timedelta(days=______)
# 
# ```
# 
# - Use `.resample` and a monthly fill to move this data from quarterly to monthly with a forward fill. This will match the other data we've downloaded.
# - Use `.rename` to rename the *Value* column to *gdp*. Remember to include `inplace=True`. Why?
# 
# For the U of Michigan Consumer Confidence data, rename *Index* to *conf*. Also resample this data to monthly with a forward fill. We don't need to alter the date/index here. Do you see why?
# 
# Finally, adjust the date of the unemployment data the same way you did for the GDP data. Resample to monthly with a forward fill. Change *Value* to *unrate*.
# 
# I'm resampling all of the data, because some of it starts quarterly and moves to monthly. One of the data sets also has strange quarters to start. Do you see which one?
# 
# This series of steps is another nice example of the work you have to do just to get your data all nice and neat.
# 
# Remember, you can use `.info()`, `.head()`, and `tail()` to check your work. You can also just show the DataFrame. Do things in steps. Do something and check to make sure that it worked. **Don't get in a hurry.**

# ## Part 4
# 
# Let's try merging our three separate DataFrames into one DataFrame. We'll do this two ways, in order to demonstrate different types of data mergers. 
# 
# To do this, we'll use `pd.merge`. You need to tell it which two DataFrames you want to merge. Then, you tell it the **type of merge**. If you're familiar with SQL, you know about inner joins, outer joins, left joins, and right joins. We'll going to try an **inner** and an **outer join**. Finally, in our example, you need to specify the **key** to merge on. In other words, which column(s) identify your data and let you merge the two data sets. 
# 
# You can read more [here](https://www.tutorialspoint.com/python_pandas/python_pandas_merging_joining.htm). 
# 
# Modify this code to do an **inner join** of your gdp and confidence data. Then, merger that data with the unemployment data. In other words, you'll use two merge statements to join the three DataFrames.
# 
# ```
# df_inner = pd.merge(_____, _____, how='_____', on='_____')
# ```
# Call this something like `df_inner`. 
# 
# Then, do an **outer join**. Call this `df_outer`. What's the difference?
# 
# You can even try **left** and **right** joins!
# 
# In finance, we're often merger on two keys: date and firm ID. But, here, there's just one key, the date. 
# 

# ## Part 5
# 
# Add three columns for the percent change of each economic indicator. The three variables that you downloaded are **levels**. We sometimes want to look at **changes** and/or **percent changes** as well. 
# 
# Then, use `.asfreq()` to go from monthly to quarterly data. Call this new data set something like `df_inner_q`. Remember doing this in the DataCamp exercises?
# 
# Select just the percent change in GDP, the level of consumer confidence, and the unemployment rate from the DataFrame and use `pandas` `plot` to graph each on its own subplot. Add a title called "Economics Indicators". 
# 
# Finally, do the same thing, but use a `.loc` to only include data from 1999-12-31 forward.

# ## Part 6
# 
# Look at our financial time series notes online and calculate the correlations among all six variables in your DataFrame. Use `df_inner_q`. Some of our data only has quarterly observations, so no point in doing correlations at the monthly level. 
# 
# Then, use `sns.heatmap` to do the same sort of thing. But, don't give it the data itself: make a **heat map of the correlations**. Include an annotation and use `Greys` as your color map.
# 
# You can read more at: <https://seaborn.pydata.org/generated/seaborn.heatmap.html>

# ## Part 7
# 
# Let's **melt** our data. What does this mean??? Let's go from **wide** to **long**. Right now, we have a date index and then a column for each variable, six variables in total. Let's see if you create a data set with only three columns: *date*, *indicator*, and *value*, where *indicator* will have values like *gdp* and *unemp*. This creates data that is stacked **vertically**, rather than data that is spread **horizontally**. 
# 
# To do this, we'll use `pd.melt` to **melt** df_inner_q. But first, let's reset the index, so that date is a column. You don't have to do this, but I kind of like seeing everything as a separate column. Remember to use `inplace=True`. Why?
# 
# ```{figure} ../images/lab5-melt1.png
# ---
# name: lab5-melt1.png
# align: center
# class: with-border
# ---
# The basic syntax and picture of what's going on.
# ```
# 
# `pd.melt` can take several arguments. `id_vars` is what your new id will be. In our case, we have **time series data**. Therefore, our ID is the date. Let the value column be named *indicator*. Modify this code:
# 
# ```
# df_inner_q_long = df_inner_q.melt(id_vars = '_____', var_name='______')
# ```
# 
# Look at the data. Do you see what it did? Do the same thing, but only keep the three level variables using the `value_vars` argument.
# 
# You can read more about `pd.melt` here: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html>
# 
# There is also a `pd.wide_to_long` function: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.wide_to_long.html>
# 
# ```{figure} ../images/lab5-melt2.png
# ---
# name: lab5-melt2.png
# align: center
# class: with-border
# ---
# More arguments for the `pd.melt` function.
# ```
# 
# This can get a bit complicated in practice. There's a joke among data folks that no one ever does this correctly without reading the manual first. No matter how many times they've reshaped their data before. 
# 

# ## Part 8
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
# 
# You've now seen most the topics that can get you started with importing, cleaning, describing, plotting, and just generally preparing your data!
