#!/usr/bin/env python
# coding: utf-8

# # Final Exam
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
# Call the Jupyter notebook for this exam `lastname_firstname_exam2`.
# 
# 
# # Our Questions
# 
# Please answer the following questions in order. 
# 
# **Use Markdown to clearly mark your questions and answers, as well as for formatting any discussion, in order to receive full credit.** 
# 
# Be aware of what **libraries** you need to import. 
# 
# Remember to **do things in order**. Many errors are caused by running code out of order, or trying to run code twice, where Python is expecting a different input, but, since the code was already run, the input has been altered. 
# 
# **Use code cells to clearly separate tasks**. 
# 
# **Use ChatGPT (or the equivalent) if it is helpful for you!**
# 
# When in doubt, **restart and run from the top**.
# 
# 
# # Part 1
# 
# **5 points.** Use `pandas data-reader` to pull in some stock returns using Yahoo!. Let’s look at these five stocks: MSFT, PG, BA, AXP, and KSS. Pull in daily price data from 2010 through 2021 and calculate discrete returns.  Only keep observations where none of the stocks have missing returns.
# 
# As mentioned in class, Yahoo! keeps breaking the different ways to access their webpage. In order to use `pandas data-reader`, include this in your set-up code.
# 
# ```
# import yfinance as yf
# yf.pdr_override()
# from pandas_datareader import data as pdr
# ```
# 
# Then, you need to get the price data. Try something like this - you'll need to add a few more steps, of course.
# 
# ```
# stock_data = pdr.get_data_yahoo(ticker_list, start_date, end_date)
# prices = stock_data['Adj Close']
# ```
# 
# ```{margin}
# Notice that you can select different *levels* of this DataFrame, like *Adj Close*. Check the lab solutions for more.  
# ```
# 
# Provide a set of summary statistics for the returns. We're cheating a bit - you can just use the adjusted close to create the returns. Don't worry about dividends. Use Python to show the number of observations and the number of columns. Also, what's the index for this data?
# 
# # Part 2
# 
# **10 points.** Let's try some slicing and dicing.
# 
# - Use `.loc` to select only *PG* and *BA* returns for 2013. Just show the first 20 results.
#   
# - Use `.iloc` to select the first 10 *PG* and *BA* returns. Notice that selecting 10 and showing the first 20 are subtly different. 
#   
# Go back to the full set of returns.
# 
# - Use `.min` to create a **new variable** that is the **minimum daily return across all of the stocks**. Call this new variable *min_ret*. Hint: `.min()` can take an *axis* argument. First, you tell it what function to use. You tell it the axis you want to apply it to using `axis=`. Do you want to apply the calculation column-wise (e.g. a value of each column) (`axis=0`) or row-wise (e.g. a value for each row) (`axis=1`)? This is a [helpful explanation](https://www.statology.org/axis-0-axis-1-python-pandas/).  
#   
# - Now, use `.aggregate()` to do the exact same thing, but call this new variable *min_ret_2*. Hint: `.aggregate()` takes **two** arguments. This first is the function to use. The second is the axis to apply it to. 
# 
# 
# # Part 3
# 
# **10 points.** Some more slicing and dicing!
# 
# - Create a new DataFrame with only *PG* and *BA* daily returns where *one of the* daily returns is negative. Note that this is an "OR" boolean test. **You can use | as the OR operator**. You can call this DataFrame *pg_ba_negative*. This is an example of **filtering**. 
# ```{margin}
# Use `.loc` to select the columns you want. 
# ```
# Go back to the main data. 
# 
# - Create a new variable called *year* using the *Date* index. You can refer to the index as `df.index`, where `df` is whatever you named this DataFrame. You can pull the year **attribute** out of date using `.year` if you have the `datetime` package imported.
#   
# - Find the average daily return by year for all of the stocks. Instead of typing in each column/ticker that you want to take the mean of, **use a separate list that contains all of the tickers.** 
#   
# ```{margin}
#   Do you already have a list with the tickers? Check your data import code.
# ```
# 
# 
# # Part 4 
# 
# **10 points.** Use `pandas plot` to make a graph of **cumulative returns** for all of the stocks. Remember, these are discrete returns.
# ```{margin}
# How can you tell if something is `pandas plot` vs. `matplotlib`? `pandas plot` is applied directly to a DataFrame, like this: `df.plot()`. `matplotlib` can be used different ways, but you'll often see a `plt` or an `ax` involved. `pandas plot` is using `matplotlib` under the surface, so you can actually mix and match methods. 
# ```
# You have some columns in your DataFrame, like *year* and *min_ret*, that aren't going to make sense in this graph. Drop these columns when calculating your cumulative returns. You can subset your main returns DataFrame when doing the calculation using your ticker list. Or, you can create a new DataFrame that only has what you want. Subsetting is easier, though!
# 
# What do I mean by **subsetting**? That's just column selection. You can select the columns you want and work with that, without saving things to a new DataFrame first. 
# 
# Multiply all of the cumulative returns by 100. Include a title on your graph and change the `alpha` to be 0.7. 
# 
# **Explain what the cumulative returns code you are using does.**
# 
# ```{margin}
# Notice how useful this ticker list is. If we change the list at the start of the code, then we don't need to change anything else - everything should just work, no matter what stocks we selected.
# ```
# 
# 
# 
# 
# # Part 5
# 
# **15 points.** I have downloaded some **daily** Fama-French factor data for you. You can find it on my GitHub here: https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/F-F_Research_Data_Factors_daily.CSV
# 
# - Show me the data type of each variable. Is *Date* an integer? If so, turn this into an actual date and make it the index. That way, both your returns data and this Fama-French factor data will have a daily date as their index. There are several ways to do this, including when importing the data.
#   
# ```{margin}
# You need to pay attention to the format of the date as integer. Both the DataCamp and our online notes will help with this. Also, make sure that you use `inplace=True` when setting the index. Remember, an index in `pandas` is just a special column that that let's us identify observations. In finance, a lot of our data has a date that we want to merge on, so making the date the index is common. We have multi-index data, too, where both a date and a ticker or firm ID are the indices. We don't have the data organized that way here.
# ```
# - With a "real" date created, **merge** this Fama-French data with the return data, **keeping only the observations that are in your stock data**. Call this new merged DataFrame *rets_ff*. 
# 
# - Rename *Mkt-RF* as *market_rf*, *SMB* as *smb*, and *HML* as *hml*.
#   
# - Check out the Fama-French variables. Do they look like they are in different units when compared to you stock returns? They are! There's an *implied* percent sign. Divide *market_rf*, *smb*, and *hml* by 100. There are many ways to do this. I used `.div(100)`, which you saw a lot in the DataCamp. Make sure that you are saving the result back to that column. I could have also *multiplied* the stock returns by 100. 
# 
# - Finally, **run a Fama-French three-factor regression** on the stock of your choice and **interpret the results**. The three Fama-French factors are the market return, the value factor (hml), and the small factor (smb). 
# 
# ```{margin}
# If you don't get the returns in the same units, the regression will still work fine and the *t*-statistics will be identical. But, the coefficients will be off by a factor of 100 in this case. 
# ```
# 
# # Part 6
# 
# **15 points** Let's think about the risk of one of these stocks.
# 
# - Print the mean and standard deviation of the daily returns for *MSFT*.
#   
# - Create a **histogram** showing the actual return distribution for *MSFT*. Use `matplotlib` to make a plot that is 10x7, with grey bars, and a title and properly labeled x-axis. This is called the **empirical distribution**, since it uses actual returns.
#   
# - Use `scipy` and `matplotlib` to create a graph that has overlapping **probability density functions** (PDF), where one PDF is a normal distribution assuming the mean and standard deviation of *MSFT*, while the other is a *t* distribution, assuming *MSFT* return characteristics. Again, include a labeled x-axis, a title, and a legend. Change the color of the normal distribution to black and the *t* distribution to "skyblue". These are called **theoretical distributions**.
#   
# ```{margin}
# When creating theoretical distributions, you'll need to create an x-axis variable to plot. See our notes for an example.
# ```
# - What's the 99% **parametric VaR** for *MSFT*, assuming that their returns are normally distributed? What does this number **tell us**? Crucially, what **doesn't it tell us**?
#   
# - Finally, **explain to me**, without any statistical jargon, the **difference between these distributions**: an empirical distribution, a theoretical normal distribution, and a theoretical *t* distribution.
# 
# 
# 
# # Part 7
# 
# **15 points** Use `scipy` and that package's optimizer to find the **max Sharpe portfolio** for these five stocks. You can assume a risk-free rate of zero. We are going to just use the stocks, so it might be easier to create a DataFrame that just has those five stocks in it and work with that. You can also subset, like above. 
# 
# - **Optimize** using the mean and standard deviation of the **daily** returns. Allow shorting, but don't let any position be less than -20% of the portfolio.
# 
# - **Print** the weights. Which stock gets the largest weight? Does that make sense?
#   
# - What is the **annualized Sharpe ratio** for this portfolio? You can (approximately) annualize a daily Sharpe like this by multiplying by the square root of 252. 
# 
# 
# 
# # Part 8
# 
# **15 points** We are going to end our semester with **loan data**. This data set is a bit different. It contains information on loans made by the Small Business Administration (SBA). These SBA loans are made by the government and go to firms that might have had a difficult time otherwise accessing credit, in the hope of creating jobs. This data is for the state of California.
# 
# You can bring in the data from my Github: https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/loan_data_sba.csv
# 
# - Import this data as a DataFrame called *sba*. 
# 
# - Print the number of **missing values** by variable. Notice anything?
#   
# - Show a **count for each possible value** of the *UrbanRural* variable.
#   
# - Let's use a function called `np.select` to match up conditions and outcomes to create a new variable called *location*. Essentially, if the first condition is met, then the first listed outcome is used to give a new variable that value. And so on...
# 
# Here's what the logic that we want to do: If `UrbanRural == 0`, then `location = 'Rural'`. If `UrbanRural == 1`, then `location = 'Urban'`. If `UrbanRural == 2`, then `location = 'Other'`. We can do this without writing a single If-statement. 
# 
# How? Take a look at [this post on StackOverflow](https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o). Go down to the 3rd solution, the one using `np.select` and talking about **vectorization**. Modify this solution to work for our task.
# 
# Two things to note. First, the third argument for `np.select` is the default, "What do I put?", if no condition is met. Make this 'NA', for Not Available, rather than 'Other', since 'Other' is actually a category. Second, note that the author is saving this to a new series. We want to instead create a new variable in the *sba* DataFrame.
# 
# Why am I having you do this? First, modifying a solution you find online is a crucial skill. Think about ChatGPT! Second, the idea of vectorization is an important programming concept if you ever need to care about speed. Basically, it has to do with how Python is doing the calculation and avoiding loops.
#   
# - Create a nice looking table that has the number of observations, total dollars, mean loan size, median loan size, and the standard deviation of loan size, where the loan size for the amount of money disbursed (DisbursementGross), grouped by the new *location* variable. You'll find sum, mean, median, and standard deviation in the notes. To get a count, use `np.size`. 
# 
# This means **creating a table as a DataFrame** and then working with it to style it the way we want. In other words, you'll want to **save the table as something** in order to change the style.
#   
# For formatting, try this code: `table.loc[:, 'sum'] = table['sum'].map('${:,d}'.format)`. Do you see what it's doing? We're picking out *sum* and using the `map` function to format each number in the column a certain way. This won't work exactly for the other variables - they are floats, not integers, like *sum*. You'll need to change the 'd' to 'f'. You can use '${:,0f}' to get rid of all decimal places. `map` is an example of **vectorization** and just means "apply this function to every item in this column or row".
# 
# Add a caption to the table. Use `style.set_caption()`. 
# 
# 
# # Part 9
# 
# **5 points** Tell me something cool that you learned this semester. 
# 
# 
# # Part 10
# 
# And that's it! I hope that this final exam has shown you how much you've seen and learned this semester. As I mentioned the first day of class, my main goal was to get you to feel comfortable using your computer and to let you know about a whole other set of tools that are available to you. You have made it over the worst part of the learning curve and are ready to explore more, whether that's another class, a book to work through, or just trying out other people's code.
# 
# Best of luck if you're graduating! And, I'll see you around next year if you aren't. 
# 
