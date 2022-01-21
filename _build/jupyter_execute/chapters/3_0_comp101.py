#!/usr/bin/env python
# coding: utf-8

# # The Basics
# 
# This section covers some ideas that I call **CompSci 101**. These are the sorts of topics that come up in any Intro to Computer Science class. Let's cover the basics, so that we can have some idea of what's going on with our data. 
# 
# I can't let you get out of this course without seeing some of this stuff. I'd feel bad. 
# 
# 
# ```{note}
# You'll find more details in Chapter 3 of our textbook. I am also borrowing heavily from [Chapter 1 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter1-basics.html)
# ```
# 
# The table below highlights important items that you should look for as you read our text. Also, the author quickly starts to use basic control structures, like `if`, `then`, and `while`. We'll discuss these in more detail, but he does a good job of going line-by-line and demonstrating the logic. Follow along with the examples.
# 
# 
# ## Chapter Three Highlights
# 
# | Topic         | Pages  |
# | :-------------------------------------------------------------------------------------- | :--------- | 
# | **Integers vs. floats**. Precision and how computers represent numbers. These are foundational concepts in computer science.                | 62 - 65      | 
# | **Booleans**. How computers represent true and false. We see logical operators, such as `>`, `<`, `==` and `!=`. `==` and `=` are not the same thing. | 66 - 69    | 
# | **Strings**. How computers represent text. Table 3-1 has a good list of string **methods**. We'll talk more about methods, objects, and functions. Skim the two excursions. **Regex** is an important tool in data work, but we won't get into it now.               | 69 - 70     | 
# | **Data Structures**. How computers group together other objects. For example, many stock prices or tickers. We'll use **lists** the most, though **numpy arrays** and **pandas data frames** are going to what we really focus on. These data structures are more primitive, in the sense that they are foundational to Python, but people have created new ones that are more suited for our purposes. Note **zero indexing**, where the first item in a list is 0, not 1. Table 3-2 is useful for things that you can with lists.                | 75 - 84; 76 - 79 are the most important      | 
# 
# 
# ```{margin}
# ```{tip}
# Want to really learn how computers work? Checkout [Code by Charles Petzold](http://www.charlespetzold.com/code/). It is over 20 years old now, but the basics haven't changed.
# ``````
# 

# ## Data types
# 
# Computers think of data, or a **value**, as a **type**. For example, in Python, there are three types of numbers: integers, floats, and complex. A **variable** is a name that refers to a value. Python let's you create any variable name as long as it begins with a letter or an underscore, so no numbers to start. It should also not be what is called a r[eserved word](https://docs.python.org/3.3/reference/lexical_analysis.html#keywords) in Python such as `for`, `while`, or `class`. All programming languages have special, reserved words that they don't want us using as variable names. It would get confused.
# 
# A common metaphor is to think of a variable as a box that holds some information (like a number, a vector, or a string). We use the **assignment operator** `=` to assign a value to a variable.

# ### Common built-in Python data types
# 
# Chapter 3 of our textbook covers the basic data types.
# 
# | English name          | Type name  | Type Category  | Description                                   | Example                                    |
# | :-------------------- | :--------- | :------------- | :-------------------------------------------- | :----------------------------------------- |
# | integer               | `int`      | Numeric Type   | positive/negative whole numbers               | `42`                                       |
# | floating point number | `float`    | Numeric Type   | real number in decimal form                   | `3.14159`                                  |
# | boolean               | `bool`     | Boolean Values | true or false                                 | `True`                                     |
# | string                | `str`      | Sequence Type  | text                                          | `"I Can Has Cheezburger?"`                 |
# | list                  | `list`     | Sequence Type  | a collection of objects - mutable & ordered   | `['Ali', 'Xinyi', 'Miriam']`               |
# | tuple                 | `tuple`    | Sequence Type  | a collection of objects - immutable & ordered | `('Thursday', 6, 9, 2018)`                 |
# | dictionary            | `dict`     | Mapping Type   | mapping of key-value pairs                    | `{'name':'DSCI', 'code':511, 'credits':2}` |
# | none                  | `NoneType` | Null Object    | represents no value                           | `None`          
# 
# Source: [Chapter 1 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter1-basics.html)

# [DataCamp tutorial on Python data structures](https://www.datacamp.com/community/tutorials/data-structures-python)
# 
# [DataCamp tutorial on Python strings](https://www.datacamp.com/community/tutorials/python-string-tutorial)
# 
# 
# 

# In[1]:


type(23)


# ## Writing functions
# 
# ```{note}
# This is just a first look at writing functions. We'll do more later.
# ```
# 
# [DataCamp tutorial](https://www.datacamp.com/community/tutorials/functions-python-tutorial)

# 
