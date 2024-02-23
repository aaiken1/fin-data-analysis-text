# Working with data

Chapter 4 of our course notes discusses how to store our data, indexing, column names, converting `numpy` arrays to `pandas` DataFrames, dates, and summarizing our data, especially **by group**. 

We'll see with how to **merge** and **reshape** our data. I'll also discuss **SQL** and the `polar` library, two alternatives to `pandas`.

**DataFrames** are the main way that we are going to organize our data. They come from the `pandas` package, which along with `numpy`, `matplotlib`, and a few others, form the core of our Python and finance toolbox.

DataFrames are a `class`. A `class` is like a blueprint. We create a DataFrame `object` from this `class`. The object then comes with certain characteristics and things that we can do to it. We call operations on a object `methods`.

```{note}
This section of the notes contains perhaps the most important topics that we'll cover. 
```

This is also where we can start looking at our **Hull textbook**. **Chapter 1** introduces **machine learning**, very generally. What types of questions can we ask? And, most importantly for this section, how should we think about the data that we need to answer these questions?

We are going to be using **time series**, like stock prices and returns. We'll be using **cross-sectional** data, like firm or house characteristics at a single point in time. And combinations of the two, sometimes call **panel data**.

Hull starts with discussing the differences between machine learning and statistics. I view this course as a blend - we're covering both. When we have theory guiding us, we're more in the traditional economics and statistics camps. When we let the models run the show, we're more in the world of machine learning. This is a simplification, but has some truth to it. 

But, no matter what, we need to understand how to **collect and organize our data**. 

For now, focus on Section 1.5 of Hull on **data cleaning**. Data cleaning will lead to a discussion of **feature engineering**, which is about constructing the variables that will go into our models.


```{note}
Sketch your data! What do you have? What do you want it to look like? Then, go look for the syntax you need to get that done.
```

## Other important sources

As always, my notes are not comprehensive - that's an impossible task.

From [Coding for Economists](https://aeturrell.github.io/coding-for-economists/intro.html)
- [Working with Data](https://aeturrell.github.io/coding-for-economists/data-intro.html) has `pandas` examples. Note the discussion of ***tidy data**. 
- [Data Transformation](https://aeturrell.github.io/coding-for-economists/data-transformation.html) has data aggregation and summary examples.
- [Exploratory Data Analysis](https://aeturrell.github.io/coding-for-economists/data-exploratory-analysis.html) has more summary examples, including making summary tables. 
- [Missing Values](https://aeturrell.github.io/coding-for-economists/data-missing-values.html) covers what to do with missing values in your data.

An [excellent and concise guide](https://www.mit.edu/~amidi/teaching/data-science-tools/study-guide/data-manipulation-with-python/#main-concepts) for data manipulation in `pandas`.

The [official `pandas` guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) is also very helpful.

From [Python Programming for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/README.html):
- [Chapter 7](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter7-pandas.html) introduces `pandas`.
- [Chapter 8](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter8-wrangling-basics.html) of Python Programming for Data Science is all about `pandas`. 

From [Python for Data Analysis](https://wesmckinney.com/book/):
- [Chapter 5](https://wesmckinney.com/book/pandas-basics.html) also introduces `pandas`.
- [Chapter 7](https://wesmckinney.com/book/data-cleaning.html) discusses data cleaning. 
- [Chapter 10](https://wesmckinney.com/book/data-aggregation.html) discusses aggregation and summarizing our data.



As you can see, this is a lot of material! That's because using `pandas` to import, organize, clean, and summarize our data is about 90% of all analysis work. We could spend the entire semester just working through these chapters. In fact, we have an entire **Data Wrangling** class that essentially does that!

