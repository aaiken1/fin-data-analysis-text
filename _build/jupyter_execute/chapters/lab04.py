#!/usr/bin/env python
# coding: utf-8

# # Lab 04
# ## Stock Stuff
# 
# In this lab, we are going to look at ETF and stock returns. This means dealing with **financial time series**. We are also going to see how data can be organized **two different ways**. The traditional way, at least for financial time series, is called **wide data**. Each column will represent an asset and a characteristics of that asset, like a price or return. You'll see names like `aapl_ret`. The index will be a date of some kind. This could mean daily, weekly, monthly, etc.
# 
# There is also **long, or narrow, data**. This is like taking the wide data and stacking it on top of itself. So, instead of a column like `aapl_ret` with `date` as the index, you'll have a column called `id` (or ticker, or CUSIP, etc.) and a column called `ret`, and a column called `date`. Together, `id` and `date` now uniquely identify each observation. 
# 
# You'll see both in this assignment. I will walk you through how to do the conversion.
# 
# Use our online notes to complete our labs. I have my own commentary and links that will help. You can work through the parts below in order. I will also be incorporating ideas from the first two DataCamp assignments.
# 
# If you are getting errors and are not sure why, my first suggestion is always to **Restart** the Python kernel, to **Clear All Output**, and run each code cell **one-by-one** from the top.
# 
# ```{margin}
# My instructions will refer to VS Code, but you can use VS Code, Anaconda Jupyter notebook, or Google Colab. The key is have a Jupyter notebook when you're done that can run from start to finish. 
# ```
# 
# Let each code cell represent one idea, or output. Take advantage of **Markdown** in your write-up. Use headers and formatting. Here's a [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) that I keep handy. Once you figure out some of the basics, you might not want to go back to Word or Google Docs. 
# 
# 

# ## Part 1
# 
# Open up VS Code or Google Colab. Have you set up your class folder yet? I've posted a video that will help you figure that part out. Open up that folder under File. If you're in VS Code, you should see it in the **EXPLORER** window pane on the left. 
# 
# Type **Cmd-Shift-P** (Ctrl-Shift-P in Windows) to open up the command palette. Make sure there's a little `>` in the search bar that pops up (there should be). Search for `Jupyter: Create New Jupyter Notebook`. This will open up a blank `.ipynb` file. Save this in a new folder in your course folder called `lab04`. Call this file `lab04-lastname-firstname`, where you fill in your name, of course! 
# 
# If you're using Anaconda Jupyter notebooks or Google Colab, you'll do something very similar. Create a new `.ipynb` file. In Google Colab, this file will be saved to your Google Drive. You can then download it when you're done. See the online notes for more on using Google Colab. 

# ## Part 2
# 
# You'll see a blank code cell, or **cell**, at the top. By default, this is set to Python. See the lower right-hand corner of the cell? Click there and search and select **Markdown**. 
# 
# Create the following in that top Markdown cell.
# 
# ```
# # Lab04
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
# Include `import matplotlib.pyplot as plt` and `from matplotlib import style`. We are going to automatically style our graphs too.
# 
# Include `from matplotlib.ticker import StrMethodFormatter`. This will let us format the text on our axes below.
# 
# Add a **comment** to that cell calling it **Set-Up**. You can add comments to each code cell to remind yourself what you're doing. Comments are different from the Markdown that you're using to write your narrative - they go in the Python cells and use `#`. 

# ## Part 3
# 
# Bring in the following data: <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/crsp_022722.csv>. Name the DataFrame `dsf`, for daily stock file. Don't set an index, for now.
# 
# This data comes from [CSRP](https://www.crsp.org) and is the "last word", so to speak, for a lot of financial data. Practitioners and academics alike use their data. It is clean and easy to bring into an environment like Python to use. More so than, say, Bloomberg data. It doesn't come cheap, though. Elon has a subscription.
# 
# You can find the data manual [here](https://www.crsp.org/files/data_descriptions_guide_0.pdf). 
# 
# **Briefly describe how the data are organized**. Is this long or wide data? Note the variable names. What's a *PERMNO*? How about *SHROUT*? I'll bet you can guess what *PRC*, *VOL*, and *RET* are. We'll look at the other variables in a bit.
# 
# **Use `pd.to_datetime` to turn `date` into an actual `date`**. What `format=` should you use? Note that if you don't include the format statement, you'll get a starting date in 1970. This data starts in 2019! Dates are fun.
# 
# Finally, **only keep observations where *RET* and *PRC* are not missing**. Modify this code to use `.notna()`. 
# 
# ```
# dsf = dsf[(dsf['___'].___) _ (dsf['___'].___)]
# ```
# 
# Remember, you can use `.info()` and `.head()` to check your work. Do things in steps. Do something and check to make sure that it worked. **Don't get in a hurry.**

# ## Part 4
# 
# You have figured out, by now, that this is **long data**. There are columns for the different IDs, like *PERMNO*, *TICKER*, and *CUSIP*. PERMNOs are... permanent, unlike tickers and CUSIPS. The same firm can have different tickers (and even different names!) over time. This makes using them to identify companies tricky. CRSP adds the PERMNO to fix this. 
# 
# How should we deal with long data? We'll need to think in terms of **ids** or **groups**. There are groups of observations stacked on top of each other. Look at the dates. They will start over as you scroll down and reach a different security. What do we do?
# 
# Let's start by learning about the **adjustments** that let you compare prices and shares outstanding over time. For example, when a stock splits 2:1, the price is going to drop in half and the shares outstanding will double. But, nothing has changed fundamentally about the firm! If you don't take this into account, you'll calculate a -50% on that day. 
# 
# You also want to make sure that your return calculations include any **distributions**, like dividends. If you just use prices, then you're missing a big part of many returns.
# 
# Having the data in long-format makes this easier to deal with. 
# 
# From the CRSP Manual:
# 
# > Price, dividend, shares, and volume data are historically adjusted for split events to make data directly comparable at different times during the history of a security... An adjustment base date is chosen as the anchor date. All data on this date are unadjusted, and other data are converted based on the split events between the base date and the time of that data.
# 
# To see why this is important, check out Apple on 8/28/20. See how the price goes from 499.23 to 129.04? The stock had a 4:1 split! But, if we divide all of the prices by `CFACPR`, or the [cumulative factor to adjust price](https://crsp.org/products/documentation/data-definitions-f), then we'll be able to compare prices across time. 
# 
# **Create a new variable called `PRC_ADJ` that does this.**
# 
# ```{margin} CRSP Returns
# The `RET` variable already does all of this for us. These are just the returns, calculated correctly. But, it is good to see all of the careful work that goes into calculating returns!
# ```
# 
# OK, we can compare prices across time now. Let's calculate our own returns **by group**. We'll use **discrete, or simple, returns** and include any distributions made.
# 
# \begin{align}
# R_{t} = \frac{V_t}{V_{t-1}} - 1 =  \frac{P_t + D_t}{P_{t-1}} - 1
# \end{align}
# 
# We need to use our adjusted prices to get things right. And, we need a **lagged** price in the calculation. This means using something like `.shift()`. But, how can we do a `.shift()` when we have groups? If we're not careful, we'll use another stock's price in our calculations because there are different security prices all stacked on top of each other! We need think in **groups**.
# 
# Modify this code to create a new `PRC_ADJ_LAG1` variable that is the adjusted price for the day before for that security. In other words, the one day lagged price.
# 
# ```
# __________ = dsf.groupby(['______'])['______'].shift(___)
# ```
# 
# Open up `dsf` and scroll down to where XOM stops and AAPL begins, row 757. See how there a NaN `PRC_ADJ` for Apple? That's good! We don't want to use an XOM price for AAPL. This is what the `.groupby()` did for us.
# 
# Now, what about our dividends? Those are in `DIVAMT`. But, see how `DIVAMT` is NaN, unless there is a dividend? We need to change those missings to zeroes. 
# 
# **Use `.fillna()` to make any missing dividend amounts equal to 0.**
# 
# We now have all of the pieces needed to calculate our own returns. **Create a new return variable called `RETURN`. Compare it to `RET`.** Are the differences zero? Why or why not?
# 
# 

# ## Part 5
# 
# OK, we can use the official CRSP return now. Let's use the `ret` variable to create cumulative returns **by group**. These are discrete returns, **not** log returns. So, we can't add them up to get cumulative returns. How do you do this? If the first return is at time i = 1, then the cumulative return at time T is:
# 
# \begin{align}
# \text{Cumulative Return}_{T} = \prod_{i=1}^T (1+r_i) - 1
# \end{align}
# 
# We do this in our notes, but it is when the entire DataFrame are returns for individual securities in a wide format. Now, we are in a long format and we want to **create a new variable for cumulative returns by security**. 
# 
# Start by creating a new **gross return variable** called `RET_G`. Gross returns are just actual returns plus 1.
# 
# Then, use a `.groupby()` and `.cumprod()` to create cumulative returns by security. Note that you'll need that gross return to do this. The formula above shows you why. You can use `.sub(1)` to then subtract one from every cumulative return. Again, the formula shows why.
# 
# This is a great example of how you chain or **pipe** together methods in Python. Take a DataFrame, group it by the security ID, take the gross return and do the cumulative product, then subtract one from everything. All in one line of code.

# ## Part 6
# 
# Now we have some cumulative returns. Let's plot them **by ticker**. I've warned you to be careful with tickers, but I know that we're safe for these three securities during this short time frame.
# 
# First, we need to make sure the data are indexed correctly. **Use `.set_index()` to make *date* the index. Use `inplace=` to save this change.** We do this to get the x-axis to show up as the date. For line graphs, the index is automatically added to the x-axis. 
# 
# Then, use a `.groupby()` and `pandas` `.plot()` to graph all three cumulative returns **on the same graph**. Modify this code:
# 
# ```
# dsf.groupby('_______')['_____'].plot(legend=True, title = 'Cumulative Returns');
# ```
# 
# Finally, graph the cumulative returns on **three different sub-graphs**. There are a couple of ways of doing this. I want to have you transform the data and then make the graph. What do I mean by transform?
# 
# Reset the index on your DataFrame using .reset_index(). We are going to use a new `pandas` method called `.pivot_table()`. With this method, you select the index, the new columns, and the values you want. In other words, you are going to **spread this data from long to wide**. Our date is the index. We want each ticker to get a column. And we want the cumulative returns for each ticker. Modify this code:
# 
# ```
# dsf_wide = dsf.pivot_table(index='_____', columns='_____', values='_____')
# ```
# 
# Do you see what it did? Now, **plot this pivoted data using `pandas` `plot()`, but have a separate plot for each ticker.** You can do this by setting `subplots = True` as an argument of `.plots()`. You could do this without rearranging the data, but I wanted you to see that process.
# 

# ## Part 7 
# 
# We just saw our first way to really transform data. We went from long data, where we had a date and an security identifier, to wide data, where each identifier became a new column. But, maybe you can see why long data is really useful? What if we had wanted two variables, not just cumulative returns? What would our column names be? We would need new names like `aapl_ret` and `aapl_ret_c`. Kind of awkward. But - it can be done! You can also take wide data and make it long. We'll do more of this in the next lab.
# 
# **Create a new DataFrame where you take `RET` and go from long to wide. Do the same thing for `PRC_ADJ`.** Make sure that the date is your index. Save the new DataFrames as `dsf_ret_wide` and `dsf_price_wide`, respectively.

# ## Part 8
# 
# With our two wide data sets created, let's try using some of the time series methods we've seen in our notes and in the DataCamp assignments. 
# 
# **Create a simple 30-day moving average for the price of each security.**
# 
# Note that we don't have to set the index for this DataFrame, since this was done when we created it using `.pivot_table()`. 
# 
# **Create two stacked plots. Each plot show have both the actual price and the moving average for the security.**
# 
# See the notes on the NASDAQ API in our text for some examples.

# ## Part 9
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
# 
# You just saw a lot of good stuff! We are learning how to think about data structures and shape things the way we want them. We'll do more with shaping our data and merging data sets in the next lab.
