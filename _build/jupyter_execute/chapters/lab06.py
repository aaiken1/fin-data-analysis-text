#!/usr/bin/env python
# coding: utf-8

# # Lab 06
# ## Portfolio Optimization
# 
# In this lab, we are going use some mutual fund returns to try to find some optimal portfolios. I have given you four return series for four different Vanguard index funds.
# 
# Use our online notes to complete our labs. I have my own commentary and links that will help. You can work through the parts below in order.
# 
# If you are getting errors and are not sure why, my first suggestion is always to **Restart** the Python kernel, to **Clear All Output**, and run each code cell **one-by-one** from the top.
# 
# Let each code cell represent one idea, or output. If you change a DataFrame and then re-run a code cell that is expecting the unchanged data, you'll get an error. Again, restart and run all.
# 
# Take advantage of **Markdown** in your write-up. Use headers and formatting. Here's a [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) that I keep handy. Once you figure out some of the basics, you might not want to go back to Word or Google Docs. 
# 
# Finally, use our textbook, notes, and DataCamp as a resource. 

# ## Part 1
# 
# Import the CSV file called "mutual_funds.csv" from our Github page. The link is: <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/mutual_funds.csv>.
# 
# Don't set an index yet. *mret* are discrete returns for each mutual fund, including all distributions. Just what you want for this exercise.
# 
# Look up each mutual fund and **write a brief, 2-3 sentence description**. In particular, what is **VMVFX**? Is it related to a particular kind of factor-based investing? See our factor model notes and look under **style factors**.  

# ## Part 2
# Use `.info()` to see what data types the four columns are. Uh oh. The returns, *mret*, got brought in as an object. Basically, Python thinks this column is text, not numbers. You can actually open up the data and see why. Two observations have "R" instead of a number. There are also some missing values. 
# 
# We can use `.to_numeric()` from `pandas` to turn a string/object column into a numeric column. Fill in this code:
# 
# ```
# _______ = pd.to_numeric(_______, downcast='float', errors='coerce')
# ```
# 
# `downcast='float'` means that the column will be turned into a float-type. `errors='coerce'` means that any text it finds, like that "R", will be set to `NA`. 
# 
# This is a really useful function!

# ## Part 3
# 
# What shape is this data? It's **long**! There's an ID variable with four different tickers and a return column, rather than four columns of returns, one for each fund. This is not the way our data in our notes or Datacamp is shaped. But, that doesn't mean that we can't use it.
# 
# Find and show the mean returns, **grouped by each ticker**. 
# 
# Then, **drop** the *crsp_fundno* column. We don't need it. We'll use *ticker* as our ID.
# 
# Then, **pivot** this data so that it is **wide**. Let *caldt* be your index. You should now have four return columns, one for each fund, and a date index/column. Make sure that you save the new data to a new DataFrame.
# 

# ## Part 4
# 
# If you open up this new, wide data, it will be clear that we're missing data for the *VMVFX* fund. This fund just hasn't been around very long. Drop rows where any of the funds have missing returns. We want to compare them over the same time periods.
# 
# And, yeah, we're doing this using very limited data. 
# 
# Find the mean monthly returns for each fund and then annualize them by doing the mean return $\times$ 12. Do the same for the standard deviation of each, though you annualize these by multiplying by the square root of 12. 
# 
# Also find the sample variance-covariance and correlation matrices. Annualize the variance-covariance matrix. You don't annualize correlations. Try it and see why!
# 
# Why 12? These are monthly returns.
# 
# **Do these seem like good funds to try to form a portfolio with, if we accept our estimates for risk and return we just found?**

# ## Part 5
# 
# Use `scipy.optimize` to find two portfolios. First, find the max Sharpe portfolio. Then, find the portfolio with a return of 9.5% that has the least amount of risk. Don't allow negative weights, since these are mutual funds. You can't short those!
# 
# Also, don't let any fund be more than 50% of your portfolio.
# 
# You'll need to set up some weights to start, as well as define a few functions. See our notes and textbook.
# 

# ## Part 6
# 
# Use `PyPortfolioOpt` to do the **exact same thing**! You can use the annualized returns and variance-covariance matrix that you've already found. 
# 
# You can assume a risk-free rate of 0, since that's the way we did the Sharpe ratio above. You should also set the same weight bounds. You'll get the same portfolio weights!
# 
# **What does the resulting portfolio look like? Does it make sense? Would you invest this way?**

# ## Part 7
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
# 
# This was our first, true, **finance** assignment. A good project topic would be to explore the `PyPortfolioOpt` package in more detail. 
