#!/usr/bin/env python
# coding: utf-8

# # Lab 08
# 
# ## Simulation and options
# 
# In this lab, we are going to try simulating some correlated stock returns, as well as price an option.
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
# Use `pandas data-reader` to download four stocks of your choosing. Use the **Monte Carlo** methods, discussed in our online notes, to simulate 100 days of future returns for each stock. To do this, make sure that the returns of each stock are **correlated**, using their historical correlations.
# 
# Use two years of prices to get returns. Use your tickers to add column names to each of the return columns. When you create the returns, the columns will be labeled as 0, 1, 2, and 3. 
# 
# Graph the resulting 100 days for daily returns for each of the four stocks on a single plot. Include a title and legend.

# ## Part 2
# 
# Combine these four stocks into an **equally-weighted portfolio**. **Simulate the portfolio returns** 100 times and make a graph for these future portfolio **cumulative return paths**.

# ## Part 3
# 
# Take one of your stocks and find a listed option price. You can use Yahoo! finance, [like this](https://finance.yahoo.com/quote/AAPL/options?p=AAPL). 
# 
# Use the drop down menus to pick a **put option** expiring in May. Pick an option with a lot of open interest. Note the strike price and the time to maturity. 
# 
# Use the **BSM pricing model** from our notes, modified for a **put option**, to find the BSM model-implied price of this option. You'll need an estimate for volatility - try using the standard deviation of returns for the stock that you used above. You'll find **daily covariance** in the covariance matrix. How can you get that to annualized standard deviation?
# 
# You can use `.iloc` to easily get the covariance estimate for your stock from the covariance matrix. The matrix will be stored as a DataFrame.
# 
# You can find the put option formula [here](https://www.macroption.com/black-scholes-formula/). Ignore the exponent with the *q* - that's the dividend yield, which we'll assume are zero.
# 
# How does your price compare to the observed market price for the option? Why might it be different?
# 
# 

# ## Part 4
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
