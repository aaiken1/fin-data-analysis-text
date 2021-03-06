#!/usr/bin/env python
# coding: utf-8

# # Lab 02
# ## King County Housing
# 
# In this lab, we are going to import data into Python using `pandas` and play around. We'll do some **exploratory data analysis**, as well. We'll use more housing data, this time from [King County in Washington State](https://geodacenter.github.io/data-and-lab/KingCounty-HouseSales2015/).
# 
# Use our online notes to complete our labs. I have my own commentary and links that will help. You can work through the parts below in order.
# 
# If you are getting errors and are not sure why, my first suggestion is always to **Restart** the Python kernel, to **Clear All Output**, and run each code cell **one-by-one** from the top.
# 
# Let each code cell represent one idea, or output. Take advantage of **Markdown** in your write-up. Use headers and formatting. Here's a [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) that I keep handy. Once you figure out some of the basics, you might not want to go back to Word or Google Docs. 
# 
# And don't forget about our [cheat sheets](http://datacamp-community-prod.s3.amazonaws.com/f04456d7-8e61-482f-9cc9-da6f7f25fc9b). 
# 
# Finally, use **Chapter 5** of our textbook as a resource. I have that chapter open as I'm making this lab. I will refer to page numbers. I will also be incorporating ideas from the first two DataCamp assignments.

# ## Part 1
# 
# Open up VS Code. Have you set up your class folder yet? I've posted a video that will help you figure that part out. Open up that folder under File. You should see it in the **EXPLORER** window pane on the left. 
# 
# Type **Cmd-Shift-P** (Ctrl-Shift-P in Windows) to open up the command palette. Make sure there's a little `>` in the search bar that pops up (there should be). Search for `Jupyter: Create New Jupyter Notebook`. This will open up a blank `.ipynb` file. Save this in a new folder in your course folder called `lab02`. Call this file `lab02-lastname-firstname`, where you fill in your name, of course! 
# 

# ## Part 2
# 
# You'll see a blank code cell, or **cell**, at the top. By default, this is set to Python. See the lower right-hand corner of the cell? Click there and search and select **Markdown**. 
# 
# Create the following in that top Markdown cell.
# 
# ```
# # Lab02
# Firstname Lastname
# Date
# ```
# 
# As you answer the questions below, use new Markdown cells and headers to separate your answers, as appropriate.
# 
# Create your first code cell where you `import` both `numpy` and `pandas` as `np` and `pd`, respectively. 
# 
# Also include `import datetime as datetime`. The `datetime` library is discussed in the first part of the second DataCamp assignment.
# 
# Add a **comment** to that cell calling it **Set-Up**. You can add comments to each code cell to remind yourself what you're doing. Comments are different from the Markdown that you're using to write your narrative - they go in the Python cells and use `#`. 

# ## Part 3
# 
# Let's get that data.
# 
# The DataFrame we will be working with today will come from `kc_house_data.csv`, which is up in my data folder on [GitHub](https://github.com/aaiken1/fin-data-analysis-python/tree/main/data).
# 
# `kc_house_data.csv` is a CSV file on home sales and characteristics from May 2014 - May 2015 in King County, Washington State. I pulled the file from Kaggle, a data science competition page and a good resource for interesting data sets. This file is **tidy data**, as each row represents an observation and each column represents a variable.
# 
# > What???s not tidy? Using colors to represent values in a spreadsheet. Lots of spacing in the data file. Multiple values in the same column separated by a comma. All of these things might make a spreadsheet easier to read to the eye, but machines do not care.
# 
# The **url** for the data is <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/kc_house_data.csv>. Download it directly using `pandas` and put it into a DataFrame called `kc`. There is a variable called `id` in the first column. Make that the index value for the DataFrame.
# 
# Take a peek at your DataFrame and view its dimensions and variables with the `info()` function. Also, check that we did the index correctly. You can do this using the `index` attribute. Functions use `()`. Attributes do not. Functions are taking the DataFrame and doing something. Attributes are checking on a specific feature of the DataFrame. Or, at least that's how I think about it.
# 
# Let???s say that we were trying to understand this particular housing market. Let???s think about some questions we might want to answer with these data:
# 
# - What time period does this data cover?
# - How large our houses in King County? What are the typical number of bedrooms or bathrooms?
# - What does the distribution of prices look like?
# - What types of amenities are present?
# - What housing characteristics do people value? 
# - Can we predict home values?
# 
# We will start to answer these questions in this lab. Other questions will need to wait until we???ve covered additional tools, like `matplotlib` for making graphs. We'll also need statistical methods, such as OLS and logit. 

# ## Part 4
# 
# We brought in the data with `id` as our **index**. This lets us refer to each row by that value. Now, let's clean up the **date**. You'll see more about dates in the second DataCamp assignment.
# 
# Right now, Python thinks that the `date` variable is an `object`. An object is a `pandas` data type that is very general. It can have mixed values, or be text. Basically, when `pandas` isn't sure what something is, it brings it in as an `object.
# 
# You can read more about `pandas` data types [here](https://pbpython.com/pandas_dtypes.html). 
# 
# Look at the raw data on Github using the URL I gave you. The `date` variable as this "T000000" in it. Python sees that, shrugs, and calls the `date` an object, rather than something date-specific. We want Python to know that this is a date, so that you can use date-specific functions. 
# 
# We will use a basic `str` method to remove that extra text. Use this code, changing it as needed:
# 
# ```
# kc['VARIABLE'] = kc['VARIABLE'].str.replace('TEXT TO REPLACE','')
# ```
# 
# Do you see what this is doing? This is just one of many ways to get rid of that extra text.
# 
# Check that this worked by printing just the `date`, `price`, and `sqft_living` columns.

# ## Part 5
# Let's finally fix that date. Use this code, changing it as needed:
# 
# ```
# kc['VARIABLE'] = pd.to_datetime(kc['VARIABLE'], format='FILL ME IN')
# ```
# 
# `pd.to_datetime` is a `pandas` method that takes a variable in your DataFrame and tries to convert it to a `datetime` format. 
# 
# What should you fill in for the `format`? Check out the first part in the second DataCamp assignment or [this](https://datagy.io/pandas-datetime/) for a summary of how `datetime` formats work.
# 
# Show that you have successfully changed the data type. We'll be working with dates all semester.
# 
# Finally, let's **create a new variable** in our DataFrame called `year` and another called `month`. 
# 
# See [this page](https://www.geeksforgeeks.org/get-month-and-year-from-date-in-pandas-python/) for how to create a new variable from a `datetime`. 

# ## Part 6
# 
# We've cleaned things up a bit, saw our first date, and created our first new variable. We can now **explore this data** to see what we have. Try the following:
# 
# - Use `shape` to give the number of rows and columns in the DataFrame.
# - Use `columns` to show our variables.
# - Use `describe()` to get summary statistics for all of the columns
# - Use `describe()` to get summary statistics for just `price`, `bedrooms`, `bathrooms`, and `sqft_living`.
# - That doesn't look great. Add this code and re-run your last `describe()`: `pd.options.display.float_format = '{:,.2f}'.format`. This will change the format for any float variables that had a lot of decimal places being displayed. Note that it is a "permanent" change in that all floats will look like this when displayed from now on in your notebook. You can also do some temporary formatting using other methods.
# 
# This [page](https://www.statology.org/pandas-describe/) gives you some of the details for the `describe()` method. You can also take a look at our online notes for more.
# 
# We should check for **missing values**. Print the total number of missing values by variable. Include all variables. 
# 
# Finally, we have some interesting variables in this data set. What do `view`, `condition`, and `grade` represent? How many unique values do they each have?

# ## Part 7
# 
# This data set is from May 2014 through May 2015. Let's see what our date range looks like and then do some `groupby` summary stats. You'll see these ideas called **group-apply-combine**, or **split-apply-combine**. You take your DataFrame, split your data and **group by** some characteristic (e.g. firm or date), **apply** a calculation to find a statistic for that group (e.g. mean or median), and the **combine** these summary statistics back into a new DataFrame. 
# 
# You can see [this page](https://datagy.io/pandas-groupby/) for some examples, as well as our textbook, starting on pg. 130. This section of [Chapter 8 in Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter8-wrangling-basics.html#grouping) also has nice examples for the group-apply-combine framework. 
# 
# - Use `min()` and `max()` to print the min and max date in the data set. Note how there are both May 2014 and May 2015 observations. So, "May" will not uniquely identify a set of sales by year. 
# - Let's create a new year-month `datetime` variable. This is different from the original `date`, since that included the day. We just want something like "2014-05" and "2015-05". Why? We want to look at housing sales **by each year-month group**. Try this and describe what it is doing in your write-up.
#   
#   ```
#   kc['ym'] = kc['date'].dt.strftime('%Y-%m')
#   ```
# 
# Let's work on our data by year-month group.
# - Create a `GroupBy` object called `ym_group` and print both the number of groups and the size of each group. You should see that we have 13 groups. This is why we couldn't assume that each month as unique. Which two months have the smallest number of home sales? Why?
# - Print mean `price` by `ym_group`. How can you select just one column, `price`, from the group?
#   
# Notice that there is now a new variable of `DatFrameGroupByObject` type in the variables window at the bottom.
# 
# We actually didn't need to create the new `GroupBy` object. See the link above for how to do this. I also have examples in our online notes.
# 
# - Use `groupby()` to find the mean of price by `ym`
# - Use `groupby()` and `agg()` to find the mean, median, and standard deviation of price by `ym`.
# 
# And, believe it or not, we actually didn't even need to create that `ym` variable. Use `groupby()` and `agg()` to again to find the same set of summary statistics, but instead of `ym`, give `groupby()` the `year` and `month` variables. See if you can figure out the syntax. Add this line of code right above your work `pd.options.display.float_format = '${:,.0f}'.format`. This is changing the formatting of all floats to have a dollar sign and no decimal places. Looks good!
# 
# 

# ## Part 8
# 
# We've now see `groupby()`, which lets us summarize our data by different groups. We can also select just portions of our data for analysis, as we've seen in our notes. Do the following:
# 
# - We have changed our formatting a few times. Let's set it back to a default with:
# 
# ```
# pd.options.display.float_format = '{:.2f}'.format
# ```
# We keep changing the float formats, but not any date or integer formats.
# 
# - Use `loc` to select all rows and just columns `date`, `price`, and `sqft_living`. Remember, you can use `:` to select all of one axis, like the rows.
# - Use `loc` to select just the observation where `id` is 5631500400, all columns. Note that you don't need `''` around the `id` when using `loc`. 
# - Use `iloc` to select the 10th through 25th `id` values and the 2nd through 5th columns. We are starting our count from 0.
# - Filter to find all of the home sales where `ym` is '2014-12'. 
# - That's a lot. Find just the first week of December 2014. Can you use the `ym` variable now?
# 
# That's still a lot, so the notebook won't show you all of them. You could save this subset of observations to a new DataFrame. Nothing is ever saved to memory until you define a new DataFrame. And, just because a file is in memory, that doesn't mean that it is saved to a drive.
# 
# We'll be doing more on summarizing, sorting, and filtering our data. 
# 

# ## Part 9
# 
# You have added new variables to this DataFrame. Let's export it to a CSV file. You should try to save it in a data folder for this class. You can do this using either a **relative path** or an **absolute path**. Let's use an **absolute path**, just for now. Your solution to this lab should live in a folder called `lab02` inside of your main course folder. However, we are going to be using the same data again and again. Let's figure out how to save this data in a folder called `data` inside of the main class folder. For me, that path is: 
# 
# ```
# /Users/adamaiken/fin-data-analysis-python/data
# ```
# 
# Add the following code in a cell at the **top of your notebook**. Alter it to fit your file structure. 
# 
# ```
# from pathlib import Path
# 
# data_path = Path('/Users/adamaiken/fin-data-analysis-python/data')
# ```
# 
# Can you alter that to get it to work on your end? You'll need the actual path for the file. On a Mac, Control- or right-click a file or folder. After the menu appears, press the Option key. Your menu choices will change. Select Copy ???file name or folder name??? as Pathname. For Windows, check out [this page](https://www.addictivetips.com/windows-tips/get-complete-path-to-a-file-or-folder-on-windows-10/). 
# 
# Now, you can do this **at the bottom of your notebook** to save to that folder:
# 
# ```
# kc.to_csv(data_path / 'kc_house_data_edit.csv')
# ```
# 
# We'll do more with **relative paths** when we get to input/output operations later on. I just wanted to get you use to the idea of your files living in certain places.
# 

# ## Part 10
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# I like to do this occasionally, to make sure things are working correctly. One downside of working in a notebook environment is that it is very easy to run code "out of order". For example, you can run code in one cell, then skip down and run another cell. But, if that cell below needed something from a cell in the middle to run, it won't work. You can lose track of what variables have been defined, what inputs have been created, what Python "knows" about. So, it's a good idea to run things from scratch.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
# 
# We've only done two labs. I hope that you're beginning to feel more comfortable in VS Code and with Python. You already know enough to use Python instead of Excel to clean up some data, make new variables, create a summary, and then save it as something you can then use in Excel!
