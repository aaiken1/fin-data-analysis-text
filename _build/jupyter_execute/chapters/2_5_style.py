#!/usr/bin/env python
# coding: utf-8

# # Code Style, PEP8, and Linting
# 
# As we learn to write code, we want to strive for **readable** code. This means code that is both easy for someone else to read and code that is easy for a **future you** to read!
# 
# I don't want to overwhelm you with rules right now, but we should be aware of how to format our Python code for readability and consistency. Python programmers like to follow a certain style, called [PEP8](https://pep8.org).
# 
# PEP8 lays out conventions for indentation, spacing, commenting, naming, line length, etc. Some basics rules to know for now:
# 
# - Use 4 spaces per indentation level.
# - Limit you code line length to 79 characters. You can indent onto the next line.
# - Package imports should be at the top and on separate lines. 
# - Pay attention to how you are naming your variables, functions, etc. Pick a style and be consistent.
# 
# Here are some other style guides for you. Just keep them handy.
# 
# <https://realpython.com/python-pep8/>
# <https://www.datacamp.com/tutorial/pep8-tutorial-python-code>
# 
# All of this will make sense as we start to code. But, I think it is helpful to be aware that there are conventions before we start. However, don't get too hung up on them at first. They will start to feel natural as we look at examples and write our own.
# 
# ```{figure} ../images/02-style.png
# ---
# name: 02-style.png
# align: center
# class: with-border
# ---
# Indentation is important in Python. Improper indentation will lead to syntax errors and your code won't run.
# ``
# 
# **Comments** are also an important part of readability. We can add comments using `#`. For example,

# In[1]:


# This prints Hello World!

print("Hello World!")


# Notice the one space after the `#` in the comment. This is part of commenting style in Python.

# ## Linting
# 
# **Linting** refers to not just properly formatted code, but also checking for unintentional errors and issues, such as functions that never get called, missing parentheses, and other "bugs".
# 
# VS code has built-in linting support when you are working in a `.py` file. Note that this is different from working in a Jupyter notebook.
# 
# <https://code.visualstudio.com/docs/python/linting>
