#!/usr/bin/env python
# coding: utf-8

# # Midterm Exam
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
# **If you get stuck because you can't complete the first part of a question**, write commented code (i.e. put a `#` in front of each line of code inside the cell) that does what you **would do** if you have the correct inputs. **There is partial credit.**
# 
# ## Exam name
# 
# Open up your folder for this class and create a new `exam1` folder. Save your Jupyter Notebook in the folder. Call this file `lastname_firstname_exam1`.
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
# *10 points* First, what are the **fifteen most common vales for *yearbuilt* in the data**? To do this, you'll want to combine a `groupby` and a `.agg('count')`, where you are counting *logerror*.
# 
# Note that the year built is, of course, different from the transaction date.
# 
# Then, what are the **fifteen most common county/zip code pairs in the data**? These columns are *regionidcounty* and *regionidzip*, respectively. Again, `groupby` and `.agg('count')` are your friends. 
# 
# For both parts, how can you show the most common values in your notebook? Should the data, perhaps, be sorted in a particular way?
# 
# By the way, I searched for the Zip codes and couldn't find a lot of them! But, the long-lats given in the data seem to work. No idea why.
# 

# ## Part 4
# *10 points* Create a **summary of the mean and median number of bedrooms and bathrooms by year built** for all houses in the data. Then, do the same thing, but **filter** to only include houses built after 1990. 
# 
# Round everything to one decimal place. See our notes and text for examples. You're again thinking in terms of groups and `.agg()`. What functions do you use inside of `.agg()` to get the mean and median?
#    
# 

# ## Part 5
# *10 points* Are there any **duplicate parcel ID's** in the data? In other words, does the same house appear more than once? 
#    
# Create a new DataFrame with just the parcel ID, the pricing error, and the transaction date and show any observations that have multiple parcel IDs (i.e. dupes) in your notebook. To do this, use `.duplicated()` from `pandas` and the idea of **masking** from the DataCamp. 
# 
# See here for the syntax: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html>. Within `.duplicated()`, you'll want to subset on the parcel ID and choose `keep = False`. This function returns **True or False** for each observation in your DataFrame according to whether or not it is a duplicate. Here we're checking for duplicate parcel IDs, but if you leave out that argument, then an observation would only be a duplicate if it had the same values across all variables as another row in the data. 
# 
# Use `.duplicated()` to create a DataFrame of True or False values. Then, use this DataFrame to **mask** and only select duplicated observations (i.e. observations where `.duplicated()` returned *true*) from your subset of data with only parcel ID, the pricing error, and the transaction date. Call this new DataFrame *non_unique_data*. 
# 
# Show these values in your notebook. **What's going on with these observations?** Why do a small number of houses appear twice? 
# 

# 
# ## Part 6
# *15 points* Where does Zillow do the worst job at pricing homes? In other words, where do their Zestimates have the largest absolute difference from the actual sale price? The pricing error is called *logerror* in the data.
# 
# \begin{align}
# log(pricing error) = log(Zestimate) ??? log(SalePrice)
# \end{align}
# 
# Log here means the natural log. We often take the natural log of data, as the log has some nice properties (i.e. reduces the skew of the data, the influence of outliers).
# 
# First, **count up the number of houses sold in each zip code** and create a new variable called *houses_sold*. To do this, use the usual variable creation and `groupby`, but use the method `.transform('count')` from `pandas` to count *logerror* by zip code. `.transform()` will add a new column, with counts by zip code, that will become the new variable. Since each Zip code can appear many times in the data, the same count will appear multiple times. 
# 
# Next, only keep zip codes where 10 or more houses are sold and **save this set to a new DataFrame**. So, more filtering based on a condition. Add `.copy()` at the end of your filtering statement to get rid of a potential warning from Python. Why? When you're doing something like New DataFrame = Old DataFrame[YOUR FILTER STATEMENT], Python wants you to be explicit that you are copying over a subset of the old DataFrame with a new one. 
# 
# It will look like this: New DataFrame = Old DataFrame[YOUR FILTER STATEMENT].copy(). We didn't do this earlier because we weren't saving the filtered data - we were just using it in another step in the same line of code.
# 
# We're doing this to get rid of Zips with only a few houses sold in the data. Weird Zips in the middle of no where. 
# 
# Then, using the new DataFrame, find the mean and median of the **absolute value of the log error** by zip code. So, another summary table and `groupby`. You can use `.abs()` to find the absolute value of a number.
# 
# Show the zips with the 10 largest mean pricing errors. Round to five decimal places.
# 
# What does the absolute value measure? What do the differences in means and medians tell you?
# 

# 
# ## Part 7
# *10 points.* Go back to the original Zillow data (before you filtered the Zip codes above) and create that same absolute value of the log pricing error in it. **Make two histograms**, one for the absolute value of log pricing error for houses with 4 or fewer bedrooms and another one for houses with more than four bedrooms. Stack them on top of each other. Include appropriate labels and titles. **What is this plot trying to answer?**
# 
# See the problem sets and notes for some examples of this type of graph.
#    
# 

# ## Part 8
# *10 points.* OK, enough housing data. Actually, we'll just bring in some **different** housing data! Let's end with some **financial time series** related to housing, also from Zillow. Use Quandl via the Nasdaq Data Link to bring in the following: 
# 
# `regions = quandl.get_table("ZILLOW/REGIONS", paginate=True)`
#   
# This will create a DataFrame called *regions* that has all of the different region types and values in the Zillow data. For example, you can pull cities, Zip codes, counties, metro-areas, etc. Note that this data is in a **long format**. See how this way of structuring data is useful? You can get all of the different regions and codes stacked on top of each other.
# 
# **Open up the *region* DataFrame in VS Code and search for the county that you're from.** You can do this by searching at the top of the **region column**. Look for *county* in the **region_type** column. Note the region ID for your county.
# 
# Now, bring in the following three data sets from Zillow: ZSFH, ZATT, and ZABT. These are overall single family home, top-tier, and bottom-tier price series. Modify this code as needed:
# 
# `zsfh = quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id=['1289', '2402'])`
# 
# Add your own county ID to the list I included. Those are Orange County, NC and Maricopa County, AZ. So, you'll bring in three price series for three counties. Save them to three different data frames. 
#    
# 

# ## Part 9
# *10 points.* Because we have **long data** that has the **same variables**, we can **append**, or stack, three DataFrames on top of each other. Do you see why? 
# 
# Do this. See the online notes for details. We have three DataFrames, so the logic is a lot like what we saw when **merging** three DataFrames in our lab. Save the DataFrame with all three variables across the three regions as a new DataFrame called **indices**.
# 
# I used `.append()` from `pandas`, though `.concat()` works as well. Include `ignore_index=True` as an option.
#   

#   
# ## Part 10
# *10 points.* Let's calculate the **percent change** in housing values by region and indicator type. Keep this in mind: We are in **long data** now. We are going to need to sort our data and work by group. Think carefully about what our groups are. We have two! We always have to pay attention to how our data are structured. This type of data is called **multi-level data**. We have indicators and regions, by date. So, each value for each date, is uniquely identified by the indicator and the region.
# 
# `indices['pct'] = indices.sort_values('____', ascending=True).groupby(['_______', '_______']).value.pct_change()`
# 
# When you're done, check the calculation. Where would you expect missing calculations?
# 
# It is actually often easier to do calculations like this in **long data** since you can group. When every variable is its own column, things get more cumbersome.
# 
# Let's finish up with a graph. To do so, let's **keep certain data and get it into wide format**. 
# 
# First, **select just the data for the ZSFH indicator**.
# 
# Then, drop the *indicator_id* column. Why? There's only one indicator ID now, so the column is redundant. Modify this code:
# 
# `indices.drop('FILL IN COLUMN NAME', axis=1, inplace=True)`
# 
# Note the `inplace=True`. `axis=1` means that whatever you typed in is a column name. 
# 
# Then, **pivot the data** to go wide. You can ignore that *pct* column now - we'll drop it as we pivot. Modify this code:
# 
# `indices = pd.pivot(indices, values='_____', columns='_____', index='_____')`
# 
# See our online notes for an example.
# 
# Finally, use `.plot()` from `pandas` to graph all three price series on the same chart. Make it look nice. The labels should appear automatically, though they will have the Zillow IDs, which don't mean much. You can change that, but we'll leave it for now. You're done. 
# 

# 
# **ENJOY SPRING BREAK**
# 
# Please upload your Jupyter notebook to Moodle! I hope that this "exam" did more than just reinforce some basic data wrangling principles. I tried to introduce you to a few new tools and really show you how the day-to-day data process works. Financial data has its own peculiarities too.
# 
# By the way, 2402 is Maricopa County. See it in your graph? I bought a condo in 2005 and sold in 2010. This is why I don't teach the real estate course.
