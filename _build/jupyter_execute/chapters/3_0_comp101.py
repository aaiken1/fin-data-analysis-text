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

# ```{note}
# Want to really learn how computers work? Checkout [Code by Charles Petzold](http://www.charlespetzold.com/code/). It is over 20 years old now, but the basics haven't changed and never will.
# ```
