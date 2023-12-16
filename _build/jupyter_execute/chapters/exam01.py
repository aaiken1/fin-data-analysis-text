#!/usr/bin/env python
# coding: utf-8

# # Midterm Exam
# 
# 
# ```{figure} ../images/exam01-python.png
# ---
# name: exam01-python.png
# align: center
# figclass: margin
# ---
# Source: Found on Twitter
# ```
# 
# ## Academic Honesty Statement
# 
# **THIS IS AN INDIVIDUAL ASSESSMENT. THIS DOCUMENT AND YOUR ANSWERS ARE FOR YOUR EYES ONLY. ANY VIOLATION OF THIS POLICY WILL BE IMMEDIATELY REPORTED TO THE ELON HONOR BOARD.**
# 
# *Add the text below to the first cell of your notebook. Replace the underscores below with your name acknowledging that you have read and understood our academic community standard.*
# 
# I, ____________, hereby state that I have not communicated with or gained information in any way from my classmates or anyone other than Professor Aiken during this exam, and that all work is my own. I have properly cited any code that I have used from other sources.
# 
# ## A note about grading
# 
# This is an exam, not a lab. **I do not expect everyone to be able to answer every question.** As with any exam, you do not start with 100 points and then subtract. You are starting with zero and then earning credit. For certain questions, I have indicated what you need to do in order to earn full credit.
# 
# While code correctness is the most important component of the exam, I will also be looking for well-formatted graphs, proper use of Markdown, thoughtful writing, and easy-to-read code. You need to pay attention to these items to earn full credit.
# 
# You can your work in VS Code, Google Colab, and Jupyter Anaconda. **Whatever works best for you.**
# 
# **If you get stuck because you can't complete the first part of a question**, write commented code (i.e. put a `#` in front of each line of code inside the cell) that does what you **would do** if you have the correct inputs. **There is partial credit.**
# 
# **IF YOU GET IN TROUBLE, RUN YOUR CODE FROM START TO FINISH!**
# 
# ## Exam name
# 
# Call the Jupyter notebook for this exam `lastname_firstname_exam1`.
# 
# 
# # Our Questions
# 
# Please answer the following questions in order. 
# 
# **Use Markdown to clearly mark your questions and answers, as well as for formatting any discussion.**
# 
# We are going to start with, you guessed it, housing data. This data is a sample of Zillow data from a [Kaggle data contest](https://www.kaggle.com/c/zillow-prize-1), where the idea was to help Zillow improve the company's "Zestimate" value for each home. There was $1.2 million in prize money awarded. Zillow recently lost a bunch of money trying to buy and sell homes based, in part, on their Zestimate. Not because the Zestimate is necessarily flawed. Instead, they ran into a problem called **adverse selection** where the homes that looked undervalued were only undervalued because the homeowner knew that there were serious problems that Zillow didn't know about. 
# 
# I've posted the data dictionary on [Github](https://github.com/aaiken1/fin-data-analysis-python/), if you have questions about the variable definitions. We are only going to use a small number of them. The main data set (properties_2016_sample10_1.csv) has housing characteristics for houses listed in three Southern California counties in 2016. The other data set (train_2016_v2.csv) contains the log(pricing error) for houses sold, as well as a transaction date. I'll tell you more about the pricing error below.
# 

# ## Part 1
# *10 points* Let's **get our data into Python and Pandas**. 
# 
# The housing data is here: <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/properties_2016_sample10_1.csv>
# The pricing and transactions data is here: <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/train_2016_v2.csv>
# 
# Load in the **properties_2016_sample10_1.csv** file. This is a random sample of 10% of the actual data from the contest. The real file was too large for our purposes. Then, load in the **train_2016_v2.csv** file. This file has the log(price error) for houses sold in the area, as well as the sale date. You might get a warning about mixed data types. That's OK!
# 
# **Inspect the data using appropriate Python methods**. Briefly describe that types of variables that you see. There are a lot, so just give me a general sense. 
# 
# **Merge them together** and keep only the observations in both data sets. Call the resulting data frame *zillow_data*.
# 

# ## Part 2
# *5 points* What is the **min and max transaction date in the data**? To do this, you'll want to get the date into a proper DateTime format first.
# 
# **Do the min and max date make sense?** Always good to check these sorts of things in your data!
# 

# ## Part 3
# *10 points* First, what are the **twenty most common vales for *yearbuilt* in the data**? To do this, I want you to combine a `groupby` and a `.agg('count')`, where you are counting *parcelid*.
# 
# Note that the year built is, of course, different from the transaction date.
# 
# Then, what are the **twenty most common region city and region county pairs in the data**? These columns are *regionidcity* and *regionidcounty*, respectively.
# 
# For both parts, how can you show the most common values in your notebook? Should the data, perhaps, be sorted in a particular way?

# ## Part 4
# *10 points* Create a **summary of the mean and standard deviation lot size (in square feet) and the tax value (in current dollars) by regionidcity** for all houses in the data. Then, do the same thing, but **filter** to only include houses with a pool.
# 
# Round everything to two decimal places. See our notes and text for examples. You're again thinking in terms of groups and `.agg()`. What functions do you use inside of `.agg()` to get the mean and standard deviation?
# 
# **Can you figure out why standard deviation is sometimes missing?**
#    
# 

# ## Part 5
# *10 points* Are there any **duplicate parcel ID's** in the data? In other words, does the same house appear more than once? 
#    
# Create a **new DataFrame** with just the parcel ID, the pricing error, the transaction date, and the *regionidcity*. Do **not** save over your main data.
# 
# Now, we want to show any observations that have multiple parcel IDs (i.e. dupes) in your notebook. To do this, use `.duplicated()` from `pandas` and the idea of **masking** from the DataCamp. 
# 
# See here for the syntax: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html>. 
# 
# Within `.duplicated()`, you'll want to subset on the parcel ID and choose `keep = False`. This function returns **True or False** for each observation in your DataFrame according to whether or not it is a duplicate. Here, we're checking for duplicate parcel IDs, but if you leave out that argument, then an observation would only be a duplicate if it had the same values across all variables as another row in the data. 
# 
# Use `.duplicated()` to create a DataFrame of True or False values. Then, use this DataFrame to **mask** and only select duplicated observations (i.e. observations where `.duplicated()` returned *true*) from your subset of data with only parcel ID, the pricing error, and the transaction date. Call this new DataFrame *non_unique_data*. 
# 
# Show these values in your notebook. **What's going on with these observations?** Why do a small number of houses appear twice? 
# 
# Now, what does this mean? If there are duplicate parcel IDs, then parcel ID **is not** a transaction ID. We should create a real, unique transaction ID in this data. Every row is a unique transaction. So, do that -- create a new variable in the DataFrame that is simply the observation (row) number. Use `.insert()` from `pandas` to create a new first column. You can look up the syntax [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html). Call this new column **transactionID** and make sure that it is in your main DataFrame. Use `np.arange()` and `len()` together to create the row numbers. Think about what `np.arange()` does. What argument does it take? What does that argument do? What does `len()` do? What argument does it take?
# 
# Why are we using `.insert` to create a new variable in this case? It lets us avoid [this warning](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy). That warning may still pop up from time-to-time. 
# 

# 
# ## Part 6
# *15 points* Where does Zillow do the worst job at pricing homes? In other words, where do their Zestimates have the largest absolute difference from the actual sale price? The pricing error is called *logerror* in the data.
# 
# \begin{align}
# log(pricing error) = log(Zestimate) − log(SalePrice)
# \end{align}
# 
# Log here means the natural log. We often take the natural log of data, as the log has some nice properties (i.e. reduces the skew of the data, the influence of outliers).
# 
# Now, we are going to count variables two ways, with different outputs. 
# 
# ### Table of counts
# 
# Go back to the Zillow data **before you did Q5 and saved that new DataFrame** with only a subset of the variables and the transaction ID. In other words, the DataFrame that has all of the variables. 
# 
# Using the main data, first **count up the number of times each *regionidcity* appears in the data** and output this to a new DataFrame. You'll want to use `.value_counts()`. But, note that `.value_counts()` outputs a series. This is not a DataFrame. What can you add after `.value_counts()` to get the output saved into a DataFrame? Check the notes.
# 
# **You are counting up the number of unique observations for each *regionidcity*, and, since each row is a transaction in the data, this is a count of transactions by *regionidcity*.** Show me a table that gives only the *regionidcity* that have over 100 transactions (i.e. observations) in the data. 
# 
# ### Creating a new variable based on a count
# 
# Next, again go back to the main data and **count up the number of houses sold in each *regionidcity*** and **create a new variable called *houses_sold***. This new variable, however, needs to live in the main DataFrame -- each row will have a value for the number of houses sold in that transaction's *regionidcity*. To do this, use the usual variable creation and `groupby`, but use the method `.transform('count')` from `pandas` to count *logerror* by *regionidcity*. `.transform()` will add a new column, with counts by zip code, that will become the new variable. Since each Zip code can appear many times in the data, the same count will appear multiple times. 
# 
# Then, only keep rows where the *regionidcity* has 5 or more houses are sold and **save this set to a new DataFrame**. So, more filtering based on a condition. Add `.copy()` at the end of your filtering statement to get rid of a potential warning from Python. Why? When you're doing something like New DataFrame = Old DataFrame[YOUR FILTER STATEMENT], Python wants you to be explicit that you are copying over a subset of the old DataFrame with a new one. 
# 
# It will look like this: 
# 
# `New DataFrame = Old DataFrame[YOUR FILTER STATEMENT].copy()`
#  
# We didn't do this earlier because we weren't saving the filtered data - we were just using it in another step in the same line of code.
# 
# We're doing this now to get rid of cities with only a few houses sold in the data. Cities in the middle of no where. **This is why I wanted a new variable in the main DataFrame based on the count of transactions in each city**.
# 
# Then, using the new DataFrame, find the mean and median of the **absolute value of the log error** by *regionidcity*. So, another summary table and `groupby`. You can use `.abs()` to find the absolute value of a number.
# 
# Show the *regionidcity* with the 10 largest mean pricing errors. Round to five decimal places.
# 
# **What does the absolute value measure? What do the differences in means and medians tell you?**
# 

# 
# ## Part 7
# *10 points.* Again, go back to the main Zillow data as of the end of Q4, before you started looking for dupes or doing counts. **Create a new DataFrame** that just has *parcelid*, *transactiondate*, and *logerror*. Create that same absolute value of the log pricing error in it. You might get the "A value is trying to be set on a copy of a slice from a DataFrame." warning here. Ignore it.
# 
# Next, **create another new DataFrame** that has just *parcelid*, *transactiondate*, and *bedroomcnt*.
# 
# Merge these two DataFrames together. What should you merge on? In other words, what is the **key** that uniquely identifies each row?
# 
# I know, I know. This is kind of silly. You could have just started with the original data and kept what you wanted. There's no point in sub-setting the data and then merging it back together. This is purely an exercise in merging. I want you to feel comfortable manipulating DataFrames.
# 
# **How many rows does this new DataFrame have? Does that make sense?**
# 
# OK, let's do something potentially useful. **Use pandas plot to make a single histogram.** First, though, I want you to **filter your data based on multiple conditions** -- only keep observations where *bedroomcnt* > 2 and *logerror_abs* < 0.5. Then, show me the distribution for *logerror_abs*. Use 100 bins and add a title. 
#    
# **What am I missing by filtering on *logerror_abs*?**

# ## Part 8
# *10 points.* OK, enough housing data. Actually, we'll just bring in some **different** housing data! Let's end with some **financial time series** related to housing, also from Zillow. 
# 
# I have uploaded four .csv files to the Github page: regions.csv, zabt.csv, zatt.csv, and zsfh.csv. Import each of these as DataFrames. Use the same URL address that you usually use -- just change the name of the .csv file at the end
# 
#  The *regions* DataFrame has all of the different region types and values in the Zillow data. For example, you can pull cities, zip codes, counties, metro-areas, etc. Note that this data is in a **long format** -- there's a variable name and the value. See how this way of structuring data is useful? You can get all of the different regions and codes stacked on top of each other.
# 
# You also have three other data sets from Zillow: ZSFH, ZATT, and ZABT. These are overall single family home, top-tier, and bottom-tier price series. This is also **long data**.
# 
# I brought in prices series for three counties that I've lived in: Orange County, NC (region_id = 1289), Maricopa County, AZ (region_id = 2402), and Fairfield County, CT (region_id = 2694). We'll learn about APIs and bringing in data from various sources after this mid-term. Then, you can choose you're own data!
# 
# **Clean up each DataFrame.** Drop that *None* column and save the resulting new DataFrames.
# 
# Then, go to the *regions* DataFrame and **filter to just show the three rows with those three *region_id***. Do this in one line of code using a **boolean filter** for "or", which is denoted as `|`. For example, (x == 5) | (x == 4) | (x == 3).
# 

# ## Part 9
# *5 points.* Because we have **long data** that has the **same variables**, we can **concatenate**, or stack, three DataFrames on top of each other. Do you see why? 
# 
# Stack the three price series. Do this using `pd.concat`. Include `ignore_index = True` and `sort = False` as options. Save the DataFrame with all three variables across the three regions as a new DataFrame called **indices**.  

#   
# ## Part 10
# *15 points.* Let's calculate the **percent change** in housing values by region and indicator type. Keep this in mind: We are in **long data** now. We are going to need to sort our data and work by group. Think carefully about what our groups are. We have three! We always have to pay attention to how our data are structured. This type of data is called **multi-level data**. We have indicators and regions, by date. So, each value for each date, is uniquely identified by the indicator and the region.
# 
# `indices['pct'] = indices.sort_values('____', ascending=True).groupby(['_______', '_______']).value.pct_change()`
# 
# When you're done, check the calculation. Where would you expect missing calculations?
# 
# It is actually often easier to do calculations like this in **long data** since you can **group**. Being able to group things is what makes data "long" to me. When every variable is its own column, things get more cumbersome.
# 
# Let's finish with two tasks. 
# 
# 
# ### Going Wide
# 
# First, let's **keep certain data and get it into wide format**. 
# 
# First, **select just the data for the ZSFH indicator**.
# 
# Then, drop the *indicator_id* column. Why? There's only one indicator ID now, so the column is redundant. Modify this code and make sure you save the resulting DataFrame.
# 
# `indices.drop('FILL IN COLUMN NAME', axis=1)`
# 
# `axis=1` means that whatever you typed in is a column name. 
# 
# Then, **pivot the data** to go wide. Keep your percent change column as your `values`. Modify this code:
# 
# `indices = pd.pivot(indices, values='_____', columns='_____', index='_____')`
# 
# See our online notes for an example. Note I'm using `.pivot()`, not `.pivot_table()`. They are similar.
# 
# Once the data are wide, rename those silly numerical column names. To do this, use `.rename` from `pandas` and a **dictionary**. Like this:
# 
# `indices = indices.rename(columns = {_____:'Orange_NC', _____:'Maricopa_AZ', _____:'Fairfield_CT'})`
# 
# Check your work. Much better!
# 
# ### You didn't really think I'd forget to include matplotlib?
# 
# Finally, use this new wide data and `matplotlib` and the `fig` and `axs` method to create three stacked histograms of price changes, one for each county. Give each histogram different color bars. You can use 100 bins for each. Do the following for formatting:
# 
# - Use `.set_xlabel` to label the bottom x-axis "Percent Price Change"
# - Use a similar method to label the middle y-axis "Frequency"
# - Give each individual histogram a title: Orange County, NC, Maricopa County, AZ, and Faifield County, CT, respectively. Set a 12 point font size for each.
# - Include the following code at the end:
# 
# ```
# axs[2].ticklabel_format(axis='x', style='plain')
# 
# axs[2].tick_params(axis='x', rotation=45);
# 
# ```
# 
# See how I included the semi-colon on the last line? That suppresses strange output in your Jupyter notebook when using `matplotlib` and other plotting packages.
# 

# 
# **ENJOY SPRING BREAK**
# 
# Please upload your Jupyter notebook to Moodle! I hope that this "exam" did more than just reinforce some basic data wrangling principles. I tried to introduce you to a few new tools and really show you how the day-to-day data process works. Financial data has its own peculiarities too.
