#!/usr/bin/env python
# coding: utf-8

# # Lab 01
# ## Getting Started with Python, Jupyter Notebooks, and VS Code
# 
# In this lab, we'll send some time getting comfortable with our work environment. The first Data Camp assignment will introduce you to Python basics. We'll walk through the basic set-up.
# 
# I am writing these notes in **Markdown**. You can open up this `.ipynb` file (iPython, or Jupyter, notebook - they changed names) in VS Code and check out the actual code. 
# 
# 
# ```{note}
# You can do this assignment in VS Code, an Anaconda Jupyter notebook, or in Google Colab. You want an .ipynb file when you're done.
# ```
# 
# Use our online notes to complete our labs. I have my own commentary and links that will help. You can work through the parts below in order.
# 
# In particular, [this from Visual Studio will help](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
# 
# In our online notes, I point your towards the [Coding for Economists](https://aeturrell.github.io/coding-for-economists/intro.html) site. His [coding basics page](https://aeturrell.github.io/coding-for-economists/code-basics.html) is also a great resource for the basic Python concepts that we're going to discuss here. You'll see a lot of this material in our first Datacamp as well.
# 
# Coding for Economists also has more notes that cover [getting started in VS Code](https://aeturrell.github.io/coding-for-economists/code-preliminaries.html).

# ## Part 1
# 
# Open up VS Code. Have you set up your class folder yet? I've posted a video that will help you figure that part out. Open up that folder under File. You should see it in the **EXPLORER** window pane on the left. 
# 
# Type **Cmd-Shift-P** (Ctrl-Shift-P in Windows) to open up the command palette. Make sure there's a little `>` in the search bar that pops up (there should be). Search for `Jupyter: Create New Jupyter Notebook`. This will open up a blank `.ipynb` file. Save this in a new folder in your course folder called `lab01`. Call this file `lab01-lastname-firstname`, where you fill in your name, of course! 
# 

# ## Part 2
# 
# You'll see a blank code cell, or **cell**, at the top. By default, this is set to Python. See the lower right-hand corner of the cell? Click there and search and select **Markdown**. 
# 
# Create the following in that top Markdown cell.
# 
# ```
# # Lab01
# Firstname Lastname
# Date
# ```
# 
# If you look at my markdown for this file, you'll see that I have that code "fenced" with three single quotes. This lets me show you the code without the code trying to run. In other words, though `#` means header, I'm not actually creating the header. I'm showing you the code, instead.
# 
# You can find the actual `.ipynb` file for these lab instructions on our [Github page](https://github.com/aaiken1/fin-data-analysis-python).
# 
# As you answer the questions below, use new Markdown cells and headers to separate your answers, as appropriate.

# ## Part 3
# 
# OK, let's try some code now. Create a new Python cell underneath your Markdown. Type:
# 
# ```
# formula_string = 'Capital Asset Pricing Model' 
# ```
# 
# Run that cell. VS Code may ask you which version of Python you want to use to execute your code. You should see a window open that the bottom that now displays your **JUPYTER:VARIABLES**. 
# 
# - What type is this variable?
# - Add code to print this variable in the same cell that you define it.
# 
# In Python, everything is something called an **object**. All objects have **types**.

# ## Part 4
# 
# What is the present value of $150 received two years from now, if the discount rate is 5%? Do your work in a new code cell. Save this value in variable called _pv_. What type is _pv_?
# 
# In a new cell, use the following to print the variable _pv_. 
# 
# ```
# print("Present Value: $%.2f" % pv)
# ```
# 
# OK, what is this `print()` function doing? It prints the text inside of the quotation marks. But, you can insert a variable to get printed as well. There's a placeholder for that, which also gives the format for the variable. This is the `%.2f` part. This is telling Python "Put the variable here and format it as a float with two decimal places. Now, what variable is it going to put there? The one you specified -- _pv_. 

# ## Part 5
# Create a `list` that contains the following: 'Apple Inc.', 'AAPL', and 172.39. Call this `list` _stock_. In the same cell, check the type of this object. Finally, use an **index** to print just the second element of the `list`, the ticker.
# 
# This material and data types is covered in our online notes and in the first Datacamp assignment. 

# ## Part 6
# 
# Data types are important in coding. So are **control structures**. Control structures let us create some logic in our code, telling it to do something only if something else is true. This means _if_, _elif_, _for_, and _while_. Let's look at a few of these. There are examples in our online notes. 
# 
# ```{note}
# Indentation is important in Python and actually tells the code what to do. Indentation works like brackets `{}` in other languages and define the scope of the control structure.
# ```
# 
# - Define a new variable called _StockPercentile_ and define it to be 90. Write an `if` statement that prints 'Add this stock to buy list.' if _StockPercentile_ is greater than or equal to 90.
# - In a new cell, copy and modify this `if` statement to include an `else` that prints 'Exclude stock.' in all other cases. Redefine _StockPercentile_ to be 80 in order to test this.
# - Finally, use an `if`, `elif`, `else` construction to test if _StockPercentile_ is greater than 100, if _StockPercentile_ >= 90, and then all remaining cases. If _StockPercentile_ is greater than 100, print 'Check calculations.' When ranking things, percentiles can't be greater than 100. Redefine _StockPercentile_ to be 110 to test the code.
# 
# Did you notice how VS code helped you out with the indentation? If it didn't, make sure that you have all of the suggested extensions installed. 
# 
# I am using something called **CamelCase** to write out the variable _StockPercentile_. You want to pick a consistent method for naming your variables to make things easier to read. 
# 
# Do you see _StockPercentile_ down there in the variable window? Also, highlight _StockPercentile_. Do you see how all other instances of the word are also highlighted in your notebook? VS Code is making it easier to see where you use something.

# ## Part 7
# 
# Let's look at another control structure, a `while` loop. This will run some code **while** a condition is true. 
# 
# In a new code cell, write a `while` loop that will print `Counting down...` and then a number. Count down from 10. You should defined a variable `i` to equal 10. Then, every time through the `while` loop, you should subtract 1 from i. 
# 
# When you get to 0, print "Blastoff!". 
# 
# Like above, note how the `print` function can be used to insert a variable into it, as well as for formatting that variable in the output. Instead of using `%.2f` as your placeholder, use `%d`, which means **integer** to Python. 

# ## Part 8
# 
# Let's import our first library, `numpy`. Do this the standard way and so that we can refer to `numpy` as `np` in our code. We are going to use `numpy` to deal with `arrays`. Arrays are covered in our notes and in the first Datacamp assignment. 
# 
# `numpy` is one of the libraries that lets us do math and handle data in Python. It works well with `pandas`, which is the library that lets us actually import and use our data.
# 
# ```{note}
# If you try to import a package and Python in VS Code tells you that it can't find it, make sure that you are using the Anaconda distribution kernel. This is the version of Python that comes with all of the packages already installed. You can select the version of Python that you're using by clicking on the Python version given in the upper right.
# ```
# 
# Then, do the following:
# 
# - Use `np.arange` to create an array of numbers from 5 to 100 (including 100) by 5. You can call this array _a_. 
# - Print the 1st element of the array.
# - Print the 10th element of the array.
# 
# Remember, Python starts counting elements or **indexing** arrays at 0. You can do all of this in one cell.
# 
# Finally, in a new cell, square every number in this array and call this new array _b_. Check and make sure it worked by showing the contents of _b_. Check the `type` of _b_ in your code. Then, go to the VARIABLES window below and find _b_. Click the "pop out" button on the left. Your data should open up in a new window and look a bit like an Excel file. This lets you look at your data sets inside of VS Code.

# ## Part 9
# 
# Arrays can have **multiple dimensions**. For example, a **matrix** is a two-dimensional array, with rows and columns. In Python, the different dimensions of the array are called **axis**. For example, with a two-dimensional array, the rows are axis 0 and the columns are axis 1. 
# 
# See our notes for more. There are also some examples [here](https://www.w3schools.com/python/numpy/numpy_array_slicing.asp)
# 
# Let's look at a two-dimensional array:
# 
# - Create a 4 x 4 diagonal matrix with ones along with diagonal and save this as array _c_. You can do this with the `np.eye` function. [Matrices that look like this](https://en.wikipedia.org/wiki/Identity_matrix) come up all of the time, which is why there's a special command. Get it, "eye"? "I"? Math is funny.
# - Use the appropriate `np` attributes to check the following for _c_: size, number of dimensions, shape, and type. See pg. 97. Notice how the syntax changes when we move from a function that is creating an object to checking an attribute of an existing object?
# - Multiply each element of this array by 3. This is an example of **vectorization**. No need to create loops that look at each element separately and then performs an operation.
# - Print the element in the 2nd row and 2nd column. And by "2nd", we are talking about **indexing**, so you want to start counting from zero. Do you get 1 or 3? Why?
# - Print just the 2nd column. This creates a one-dimensional array, where the column is now along axis 0 (i.e. it looks horizontal). 
# - This one is a bit tricky. Print just the first two columns of the array. You'll use a **slice** for this. 
# - Let's end with the trickiest one. Print just this portion of the array:
# 
# ```
# [[0. 0.]
#  [1. 0.]]
# ```

# ## Part 10
# 
# Finally, **clear the outputs of all of your cells** using the button at the top of the notebook. Restart your Python kernel. This will clear everything from memory. Then, **Run All**. All of you cells should now run, in order, from top to bottom.
# 
# I like to do this occasionally, to make sure things are working correctly. One downside of working in a notebook environment is that it is very easy to run code "out of order". For example, you can run code in one cell, then skip down and run another cell. But, if that cell below needed something from a cell in the middle to run, it won't work. You can lose track of what variables have been defined, what inputs have been created, what Python "knows" about. So, it's a good idea to run things from scratch.
# 
# You are done! **Turn in this .ipynb file via Moodle.**
