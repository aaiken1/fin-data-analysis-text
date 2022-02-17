# Importing and using data

DataFrames are the main way that we are going to organize our data. They come from the `pandas` package, which along with `numpy`, `matplotlib`, and a few others, form the core of our Python and finance toolbox. 

DataFrames are a `class`. A `class` is like a blueprint. We create a dataframe `object` from this `class`. The object then comes with certain characteristics and things that we can do to it. We call operations on a object `methods`. 

This section begins with Chapter 5 of our text and getting data into Python. We'll look at some stock data as an example. We also have our other online textbooks.

From [Python Programming for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/README.html):
- [Chapter 7](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter7-pandas.html) introduces `pandas`.
- [Chapter 8](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter8-wrangling-basics.html) of Python Programming for Data Science is all about `pandas`. 

From [Python for Data Analysis](https://wesmckinney.com/book/):
- [Chapter 5](https://wesmckinney.com/book/pandas-basics.html) also introduces `pandas`.
- [Chapter 7](https://wesmckinney.com/book/data-cleaning.html) discusses data cleaning. 
- [Chapter 10](https://wesmckinney.com/book/data-aggregation.html) discusses aggregation and summarizing our data.

From [Coding for Economists](https://aeturrell.github.io/coding-for-economists/intro.html)
- [Working with Data](https://aeturrell.github.io/coding-for-economists/data-intro.html) has `pandas` examples.
- [Exploratory Data Analysis](https://aeturrell.github.io/coding-for-economists/data-exploratory-analysis.html) has data aggregation and summary examples.

You'll see more about `pandas` in the second DataCamp assignment, **Intermediate Python for Finance**. You'll see dates and times using `datetime`. 

As you can see, this is a lot of material! That's because using `pandas` to import, organize, clean, and summarize our data is about 90% of all analysis work. We could spend the entire semester just working through these chapters. In fact, we have an entire **Data Wrangling** class that essentially does that!

## Chapter Five Highlights

| Topic         | Pages  |
| :-------------------------------------------------------------------------------------- | :--------- | 
| **What are DataFrames?**. The way we are going to store our data. Indexes and column names.                | 114 - 118      | 
| **Arrays to DataFrames**. We can convert `numpy` arrays to `pandas` DataFrames. Dates are discussed as well. | 119 - 123    | 
| **Looking at DataFrames**. Describing our data. Some basic descriptive statistics.              | 123 - 126     | 
| **Basic Plotting**. More on this later. | 126 - 130
| **Group By**. When summarizing data, we often want to do that **by group**, like by firm or by year. | 130 - 132
| **Data Manipulation**. Selection, or **filtering our data**. Joining data together. Merging data together. **Really important!** | 132 - 140


