#!/usr/bin/env python
# coding: utf-8

# # Lab 03
# ## King County Housing, This Time With Graphs
# 
# In this lab, we are going to import data into Python using `pandas`, clean it up, and make some **graphs**. We'll again use the housing data from [King County in Washington State](https://geodacenter.github.io/data-and-lab/KingCounty-HouseSales2015/).
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
# And don't forget about our [cheat sheets](http://datacamp-community-prod.s3.amazonaws.com/f04456d7-8e61-482f-9cc9-da6f7f25fc9b).
# 

# ## Part 1
# 
# Open up VS Code or Google Colab. Have you set up your class folder yet? I've posted a video that will help you figure that part out. Open up that folder under File. If you're in VS Code, you should see it in the **EXPLORER** window pane on the left. 
# 
# Type **Cmd-Shift-P** (Ctrl-Shift-P in Windows) to open up the command palette. Make sure there's a little `>` in the search bar that pops up (there should be). Search for `Jupyter: Create New Jupyter Notebook`. This will open up a blank `.ipynb` file. Save this in a new folder in your course folder called `lab03`. Call this file `lab03-lastname-firstname`, where you fill in your name, of course! 
# 
# If you're using Anaconda Jupyter notebooks or Google Colab, you'll do something very similar. Create a new `.ipynb` file. In Google Colab, this file will be saved to your Google Drive. You can then download it when you're done. See the online notes for more on using Google Colab. 

# ## Part 2
# 
# You'll see a blank code cell, or **cell**, at the top. By default, this is set to Python. See the lower right-hand corner of the cell? Click there and search and select **Markdown**. 
# 
# Create the following in that top Markdown cell.
# 
# ```
# # Lab03
# Firstname Lastname
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
# I'll remind you about this data. 
# 
# The DataFrame we will be working with will come from `kc_house_data.csv`, which is up in my data folder on [GitHub](https://github.com/aaiken1/fin-data-analysis-python/tree/main/data).
# 
# `kc_house_data.csv` is a CSV file on home sales and characteristics from May 2014 - May 2015 in King County, Washington State. I pulled the file from Kaggle, a data science competition page and a good resource for interesting data sets. See the link above for more about the data and what's in it.
# 
# The **url** for the data is <https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/kc_house_data.csv>. Download it directly using `pandas` and put it into a DataFrame called `kc`. There is a variable called `id` in the first column. Make that the index value for the DataFrame. Clean up the `date` variable like last time.
# 
# As mentioned in the last lab, we want to think about our question first and then match that to our data. What are we interested in? Can our data answer that question? In practice, just knowing this can be really tough. For example, some questions that this data **might** be able to help us answer:
# 
# - What time period does this data cover?
# - How large our houses in King County? What are the typical number of bedrooms or bathrooms?
# - What does the distribution of prices look like?
# - What types of amenities are present?
# - What housing characteristics do people value? 
# - Can we predict home values?
# 
# Answering these questions would help you figure out what to price a particular home at, for example. Zillow's [Zestimate pricing model](https://www.zillow.com/z/zestimate/) does that. They messed up, though, when trying to use their Zestimate to [actually buy and sell houses](https://www.npr.org/2021/11/08/1053689886/ibuyers-zillow-and-the-lemons-problem). The problem wasn't their model, per se. They ran into what's called the [lemon problem](https://en.wikipedia.org/wiki/The_Market_for_Lemons). 
# 
# Anyone trading, or just buying and selling when the quality of the good is uncertain, has to be aware of this problem! Always ask: Why is this other person trying to sell me this item (e.g. house, car, stock) at this particular price?
# 
# Friends of mine have created a company that scores homes and neighborhoods based on their curb-appeal [using machine learning techniques](https://www.wsj.com/articles/selling-your-home-its-whats-on-the-outside-that-counts-11579792560) based on photos.

# ## Part 4
# 
# Let's start with some **sorting**, **filtering**, and **variable creation**. 
# 
# Create a new `pandas` DataFrame from our main data file that contains: date (date sold), price, square footage of living space, square footage of the lot, year built, number of bedrooms, waterfront, and **price per square foot**. You'll need to create one of these variables! Name this DataFrame `kc_subset`. 
# 
# You can create the year by selecting the `date` column and using the `dt.year` method on it. You can find an example [here](https://datascienceparichay.com/article/pandas-extract-year-from-datetime-column/). We did this in the last lab too. 
# 
# How can you create a `prc_sqr_ft` variable?
# 
# Remember, this new DataFrame will live in memory, but it isn't stored on your computer until you actually save it using something like `to.CSV`. 
# 
# Do the following:
# 
# - Show the ten least expensive homes sold in this data set on a price per square foot basis.
# - Print the min price.
# - Print the max price.

# ## Part 5
# 
# What does the distribution of housing prices look like? Let's create a **histogram** of prices using `pandas` `plot()` method. Note that this isn't `matplotlib` yet, at least not directly. There are many ways to do the same types of things in Python.
# 
# It’s good practice to always think about your data. For a histogram, this can mean figuring out the number of bins to use. When you create your histogram include this as an argument: `range = (0, 8000000)`. This will have the x-axis go from 0 to 8,000,000, essentially the range of prices that you should have see above.
# 
# Now, how can you figure out the **bin width** and the number of bins to use? If you choose `bin = 8`, then each bin is going to have a range of 100,000. If you choose `bin = 80`, then each bin is 10,000 wide. You might ask yourself: “What would be a meaningful difference in housing prices?” 1 is obviously too little, 500,000 might be too high.
# 
# Pick a number of bins. Add a title. Remove the legend. Add the following to style the graph automatically: `style = 'seaborn-white'`.
# 
# All of your options will go **inside** of the `plot()` method.
# 
# For various settings in `pandas` plot, check out this [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html).
# 
# `pandas` is using `matplotlib` functions to style the plots. In fact, `pandas` plot and `matplotlib` can be used together. To see a list of styles, try: `plt.style.available`. Don't change the color of the line, etc. when making the plot, or this will override your style choice.
# 

# ## Part 6
# 
# I didn't like the x-axis on my graph. It uses scientific notation and just goes 1, 2, 3... up to 8, because the top range was 8,000,000. Let's do two things now. 
# 
# - We can filter our data before plotting it. Try `kc_subset[kc_subset['price'] < 1000000].your_plot_code`, where `your_plot_code` is your histogram code from above. This will filter your data to only homes with prices less than 1,000,000 and then pass that filtered data set to the `plot()` function. Edit the range and bins to something more appropriate. **Do you see spikes in the data? What's going on there?**
# 
# By the way, there's a term for this kind of programming logic. We are filtering our DataFrame and then **piping** it, or sending it, to the plot function. Basically, there's some logic to your code that you can read from left to right. And, this is all done without changing the actual DataFrame.
#   
# - I still don't like the x-axis. Let's use `matplotlib` to make the graph. It's easier to modify things this way. You can actually use your `pandas` plot and then modify it with `matplotlib` code. But, we'll start from scratch. **Make the same histogram again, but use the `pyplot` way discussed in our notes.**
# 
# This means using the `plt.hist` function. Use **all of the price data** by plotting `kc_subset.price` or `kc_subset['price']` inside of `plt.hist`. Either pulls the column that you want out of the DataFrame. Add an x-label and a title. Do not include a legend. Style it using `plt.style.use('seaborn-white')`.
# 
# Let's fix that x-axis finally. Add the following code:
# 
# ```
# plt.ticklabel_format(axis='x', style='plain')
# plt.tick_params(axis='x', rotation=25)
# plt.gca().xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}')); # Add dollar sign and commas using StrMethodFormatter from matplotlib
# ```
# `style='plain'` will get rid of the scientific notation. The next line rotates the labels 25 degrees. The last line adds that dollar formatting with commas. Note the `gca()` bit. This means **get current axis**. This particular formatting method needs that `gca()` to "know" which plot to style. The plot I want to style is the axis (or plot) that we're working with. You don't need that code when you're doing things the **object-oriented** method, discussed in the notes. There, you just tell it what axis to do stuff to (e.g. ax or ax[1]).
# 
# Make sure that the last line has a semi-colon.
# 

# ## Part 7
# 
# Let's make that same graph **yet again** using the **object-oriented method**. This means creating a **fig** and **axes**. We only have one axis here, so you can define it as **ax**. Remember, an axis is a plot. I like this object oriented method, because it really makes it clear what you're doing. I have axes or plot. I am doing something to it, I'm styling it, etc. Then, here's another plot. I can put them together, even. They are truly **objects** that we can think about in almost a physical way.
# 
# When styling the plot, instead of `plt.`, you'll use `ax.`, since you're referring to a specific axes object that you've created. 
# 
# When searching around for how to style a plot, you'll come across **many ways to do the same thing**. Some of them work when using `panda` plot, some when using the `plt.`, and some when using `fig` and `ax`. Some methods will work with more than one way. You just have to experiment a bit. Here's some code to fill in:
# 
# ```
# ax.set_xlabel('FILL ME IN')
# ax.set_ylabel('FILL ME IN')
# ax.set_title('FILL ME IN', fontsize = 15)
# ax.ticklabel_format(axis='x', style='plain')
# ax.tick_params(axis='x', rotation=45)
# ax.tick_params(axis='y', rotation=45)
# ax.xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
# ```
# 

# ## Part 8
# 
# Let’s create some **categorical variables** from our data. Let’s define a large house as anything greater than 2,500 square feet. Implement the code below to create a new categorical variable called “large_house”.
# 
# ```
# df['new_var'] = np.where(df['old_var']>2500, 'yes', 'no')
# ```
# This uses `np.where` to do some if/else-style logic and create the new variable. You'll see the new column in your DataFrame. You can make this a **categorical** variable using `astype`, which we've see before:
# 
# ```
# kc_subset['large_house'] = kc_subset['large_house'].astype('category')
# ```
# 
# If you do a .info() on the DataFrame, you'll see that `large_house` is indeed something called a category. Pandas treats categorical variables in a particular way, letting you different things than if this variable was just text.
# 
# Let's get a little fancier. Create a new variable `sqft_living_100` that is the percentile rank of the `sqft_living` variable. Check out the second example on this page: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rank.html>. A percentile rank will give every observation a rank between 0 and 1, with 1 being the largest homes. You can print the min and max of your percentile rank variable to see.
# 
# Let's now create a house size category based on the **quantile** of living space that the house falls into. Quanitles mean splitting the data into four groups, based on the variable. This is a less ad hoc way of creating categories. You can use this code below to create the new variable, which will range from 1 to 4, depending on the size of the living space. 
# 
# ```
# # create a list of our conditions
# conditions = [
#     (kc_subset['sqft_living_100'] < 0.25),
#     (kc_subset['sqft_living_100'] >= 0.25) & (kc_subset['sqft_living_100'] < 0.5),
#     (kc_subset['sqft_living_100'] >= 0.5) & (kc_subset['sqft_living_100'] < 0.75),
#     (kc_subset['sqft_living_100'] >= 0.75)
#     ]
# 
# # create a list of the values we want to assign for each condition
# values = ['q1', 'q2', 'q3', 'q4']
# 
# # create a new column and use np.select to assign values to it using our lists as arguments
# kc_subset['large_house_4'] = np.select(conditions, values)
# ```
# 
# This code creates a list of conditions to meet and then the values that get assigned, depending on the condition. We're splitting up the data into quartiles based on a percentile ranking, so there are four conditions. The method `np.select` selects the appropriate value for each condition. Make `large_house_4` a categorical variable too. If you've used other languages, this is a bit like a `case-when` statement. If this condition is true, assign this value.
# 
# Finally, make `waterfront` a categorical variable. 

# ## Part 9
# 
# Now, we're going to make two plots. Use the `fig` and `axes` method for both.
# 
# First, make a scatter plot where you have `price` on the y and `sqft_living` on the x. Name the plot that you create **scatter**, with `scatter = ax.scatter(...)`, like you are doing for `fig`. This makes our plot an object. You'll see why we're doing this in a second.
# 
# We are going to change the color of the dots to blue when waterfront is 1. To do this, add the following to your `ax.scatter(...)`:
#   
# ```
# c=kc_subset['waterfront'], cmap='Blues'
# ```
# 
# You can see an example [here](https://www.statology.org/matplotlib-scatterplot-color-by-value/).
# 
# You can also pick the colors that you want using a dictionary and then **mapping** values to colors. You can see an example of this [here](https://kanokidotorg.github.io/2020/08/30/Matplotlib-scatter-plot-color-by-category-in-Python/).
# 
# Finally, make the plot look good with titles, labels, etc. Change the format of both the x and the y axes. You want dollar signs and commas on the y and commas in the x. Make the dots smaller using `s=`. See the `scatter()` [documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
# 
# We should have a legend for this plot to denote what the two color of dots mean. Add the following code:
# 
# ```
# legend = ax.legend(*scatter.legend_elements(),
#                     loc="lower right", title="Waterfront")
# ax.add_artist(legend);
# ```
# 
# This creates a `legend` object called **legend** that we can then add to the plot. We needed to create **scatter** up above in order to refer to it in this `ax.legend`. We're pulling the names from it. See [this](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html) from the official documentation for more.
# 
# 
# Finally, plot two histograms together using the `fig` and `axes` method. Start with this:
# 
# ```
# fig, axs = plt.subplots(2, 1, sharex=True, sharey=False, figsize=(10, 6))
# ```
# 
# This will stack two figures on top of each other. The top figure should be the distribution of price per square foot where the home is **not** on the water. The bottom figure should be all of the waterfront homes. They won't share a y-axis, since there are so few waterfront homes. Change that to `True` to see why I made it `False`. 
# 
# You'll also want to filter your data. Create two new DataFrames, one with `'waterfront' == 0` observations and one with `'waterfront' == 1` observations.
# 
# Now, create two histograms. Here's my code for the top one:
# 
# ```
# axs[0].hist(no_water['prc_sq_ft'], bins=50, color='k', alpha=0.5)
# ```
# 
# See how you'll be referring to each plot using the array? Style your graph this way. Notice my new DataFrame name. Style the plots. 
# 
# For both figures, do the following: **Make the font size of your title a little bigger.** We haven't talked about how to do this, but it is straightforward.

# ## Part 10
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
# 
# You are developing a nice set of tools. You can bring in some raw data, clean it up, summarize it, create new variables, and make some graphs. Once you have the basics down, you can read documentation and look at examples to figure out how to do a lot more.
