#!/usr/bin/env python
# coding: utf-8

# # Lab 07
# ## Risk Management and Portfolio Management
# 
# In this lab, we are going to use the price of four ETFs to find returns and the weights for both an optimal Sharpe and a minimum variance portfolio. Then, we'll calculate non-parametric VaR and CVaR measures for both portfolios and compare. Finally, you download some ETF data and run a factor model regression. You can think of this as part of risk management too - what risks are you exposed to with the ETF that you choose?
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
# Bring in the ETF data from my Github page: <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/etf-reproducible-finance.csv>. Parse that date column, as we usually do. You can also let it be the index.
# 
# Calculate **discrete returns** using the prices and show some descriptives to make sure things look good.
# 

# ## Part 2
# 
# Use `sco.minimize` from the `scipy` library to find the portfolio weights that give you the portfolio with the maximum Sharpe ratio. You can assume a risk-free rate of 0%. Don't allow short selling (i.e. negative weights). Make sure that you use annualized returns and variances/covariances.
# 
# Notice that you result is saved inside of an OptimizeResult **object**. We'll need to figure out how to get the weights out of this object.

# ## Part 3
# 
# Use the same method, but find the global minimum variance (GMV) portfolio. You're saving this result to a different OptimizeResult **object**.

# ## Part 4
# 
# Briefly discuss the assumptions that we're making when we do portfolio optimization like this. Compare the expected returns and risk of the two different portfolios

# ## Part 5
# 
# Now comes the fun part. Your daily returns for each ETF and two sets of weights. Use these weights to come up two sets of **daily portfolio returns**, one for the max Sharpe and one for the GMV. 
# 
# This is where you have to figure out how to get the weights out of the OptimizeResult **object**. How do you do this? Have Python show you all of the different parts of the object by just calling the name of the OptimizeResult **object**. You see the `x:` at the bottom? Those are the weights. You can access them with `your_name_of_object.x`. You can even access specific weights like you would any array, using`[]`. Cool!
# 
# We'll use some code from your DataCamp assignments here. First, you'll create a new DataFrame of weighted returns, where you use `.mul` to multiply your returns DataFrame and the weights across `axis = 1`, or across columns. In other words, each daily return is being multiplied by its corresponding weight. 
# 
# Then, you'll calculate a new portfolio return column in that new DataFrame of weighted returns by summing up the individual weighted returns, also across `axis = 1`. Use the `.sum` function. 
# 
# Here's some code (commented out) for you to fill in that does this. The first line creates a new DataFrame with the weighted returns. The second line sums up the weighted returns to get the portfolio return.
# 

# In[1]:



#rets_max_sharpe_weighted = rets.mul(opt_max_sharpe.x, axis=1)
#rets_max_sharpe_weighted['portfolio'] = rets_max_sharpe_weighted.sum(axis=1)


# 
# 
# In the end, you'll have two new DataFrames, one for each optimization method, that contain the weighted returns and the overall portfolio return. 
# 
# We are also making another assumption here. We are **re-balancing our portfolio daily** to get back to these optimal weights. This is something no one would do! Daily re-balancing is costly. In other words, we are not setting our portfolio weights at the beginning of the period and then just letting it ride. We are implicitly selling our "winners" and buy our "losers" each day to get back to the optimal weights.

# ## Part 6
# 
# Find the **non-parametric** 95th and 99th percentile VaR and CVaR for each of these two portfolios. That's eight different measures. Briefly discuss what you find.
# 
# Make a histogram for each set of returns and add the 95th and 99th VaR as a line to each. 

# ## Part 7
# 
# Let's end with some **factor models**. Use one of our finance packages (e.g. https://github.com/ranaroussi/yfinance) to pull in monthly prices/returns for an equity-based ETF. You might need to calculate returns from the prices, so be sure that you include dividends and capital gains distributions. See https://finance.zacks.com/calculate-mutual-fund-percentage-returns-distributions-1869.html. 
# 
# Make sure that you have at least two years worth of returns. 
# 
# Then, download the Fama-French returns from here: 
# 
# http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html#Research
# 
# You'll want the CSV files for the Fama/French 3 Factors (the first option). Then, scroll down until you find Momentum Factor (Mom). You'll want the CSV files for that too. Note that you're downloading .zip files. Open up these .zip files and find the monthly factor returns. Clean up the CSV files in Excel (or Python). Import the CSV into Python. Merge the factor returns to your ETF returns on date. This is the tedious part!
# 
# With the merger done and the dates lined up, you can run what is called a Carhart 4-factor model to explain the returns of your ETF. The Carhart model is the Fama-French model plus momentum. Carhart was [Co-Chief Quantitative Investment Officer](https://www.cfamontreal.org/static/uploaded/Files/Conferenciers/2015-2016/15-10-08-BIO-MARK-CARHART.pdf) at Goldman Sachs before leaving to start his own hedge fund. He was Fama's student at the University of Chicago.
# 
# What are the risks that affected your ETFs returns? Did the ETF have alpha? **Should** your ETF have had alpha? What was its strategy?
# 

# ## Part 8
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
