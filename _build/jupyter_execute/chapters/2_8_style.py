#!/usr/bin/env python
# coding: utf-8

# # Code style, PEP8, and linting
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
# 
# Here are some other style guides for you. Just keep them handy.
# 
# <https://realpython.com/python-pep8/>
# 
# <https://www.datacamp.com/tutorial/pep8-tutorial-python-code>
# 
# <https://google.github.io/styleguide/pyguide.html>
# 
# For the Google Style Guide, check out Section 3 first. 
# 
# All of this will make sense as we start to code. But, I think it is helpful to be aware that there are conventions before we start. However, don't get too hung up on them at first. They will start to feel natural as we look at examples and write our own.
# 
# Here's an example of a style guide from the DataCamp tutorial.
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

# ## Files, file paths, and the names of things
# 
# We'll go over absolute and relative file paths in class. You can see the notebook `1-file-paths.ipynb` on our Github page for some examples.
# 
# ```{margin} Know where your stuff is!
# It is very important that you use a consistent organization and structure. Files, folders, and paths are very important. **If you are using the lab computers, bring your own USB Drive**.
# ```
# 
# My layout is simple. A folder for this class. Then, inside that folder, I have the following sub-folders: data, output, images, and code. 
# 
# ```{figure} ../images/02-my-files.png
# ---
# name: 02-my-files.png
# align: center
# class: with-border
# ---
# My class folder, **fin-data-analysis-python** and sub-folders. You won't have the readme.md file. That is generating the Read Me text on Github. You also probably don't have hidden files and folders visible on your machine.
# ```
# 
# When I open up Jupyter or VS Code, I open up that class folder. Then, I can see my folder structure. I then use **relative file paths** to open and save files. 
# 
# And, instead of a single code folder, you can set-up a folder for each assignment. Then, inside each of these folders are folders called *code*, *data*, etc.
# 
# ```{figure} ../images/02-file-paths.png
# ---
# name: 02-file-paths.png
# align: center
# class: with-border
# ---
# Each assignment can get its own folder and sub-folder structure.
# ```
# 
# And, this is a [great presentation](https://speakerdeck.com/jennybc/how-to-name-files) on how to name files. You want your file names to be machine readable, human readable, easily searchable, and easily sorted. There's something of a science to doing this correctly. 
# 
# Getting this stuff right will make your life easier.

# ## Linting
# 
# **Linting** refers to not just properly formatted code, but also checking for unintentional errors and issues, such as functions that never get called, missing parentheses, and other "bugs".
# 
# VS code has built-in linting support when you are working in a `.py` file. Note that this is different from working in a Jupyter notebook.
# 
# <https://code.visualstudio.com/docs/python/linting>
