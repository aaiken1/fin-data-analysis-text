#!/usr/bin/env python
# coding: utf-8

# # Packages
# 
# Packages, like `numpy` and `pandas`, expand what Python can do. These packages also come with the Anaconda install of Python. Packages are also sometimes called libraries. 
# 
# Other packages, like `nasdaq-data-link`, do not come with Anaconda. We are going to need to go out and get them.
# 
# We are going to see two basic ways to install packages. Both involve typing commands **in the terminal**. You can access your terminal via VSCode, or directly on your computer. On a Mac, search for [Terminal](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac). On a Windows machine, look for the [Windows Command Line Shell](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands). Both let you do things in a text-based way. This can be very powerful.
# 
# ```{note}
# By importing a package, you get access to all of the **classes** and **methods** that come with that package. This are important concepts from **software engineering** and make your code much easier to read and use. Essentially, you get built-in **modularity** -- you don't have to reinvent the wheel and define, say, an array every time you use them. We'll talk a bit more about this when we get to **object oriented programming** and related concepts.
# ```
# 
# First, if a package is [available via Anaconda](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/), you can install it at least two ways. In the terminal, you will type:
# 
# ```
# conda install package-name
# ```
# 
# where you fill in `package-name`. You can also use the Anaconda Navigator that got installed when you downloaded Anaconda. This let's you avoid the terminal and use a GUI to look for and install a package.
# 
# ```{figure} ../images/02-anaconda-packages.gif
# ---
# name: 02-anaconda-packages.gif
# align: center
# class: with-border
# ---
# You can use the Anaconda Navigator GUI to check and see which packages Anaconda has installed, including ones that you install yourself to Anaconda via `pip`. 
# ```
# 
# In the notes, you'll see that I install several packages, like `plotly`, this way. You'll need to close VS Code and open it back up when you're done.
# 
# However, many of the packages that we want to use are specialty packages for finance, so don't come with the Anaconda distribution of Python. Or, they are just new, so haven't become "official" enough to get included by the folks at Anaconda. We are going to use `pip` to install these packages. This is where it can get tricky.
# 
# `pip` is a way to install Python packages via the command line and stands for *pip installs packages*. This is a computer science joke -- the acronym is in the definition, which gives it a recursive definition. 
# 
# `pip` will also install **package dependencies**, or other packages that the package that we want is using.
# 
# But, where is it installing the packages? Which version of Python will it be associated with? This is the tricky part and one of the frustrating aspects of Python.
# 
# You can use the following to see which `pip` and which Python your computer is currently looking at. 
# 
# ```
# which -a pip
# which -a python
# ```
# 
# ```{figure} ../images/02-which.png
# ---
# name: 02-which.png
# align: center
# class: with-border
# ---
# Running **which** in the terminal on my Mac.
# ```
# 
# When I run that code, I can see that I am using the Anaconda3 distribution of `pip` and that I have two versions of `Python`, including Anaconda. This means that, when I use `pip`, that my packages will **also be installed in Anaconda**.
# 
# A bit of an aside: There's also another version of Python that doesn't get listed there, because I looked for Python, and not Python3. I can see it when I do **select Kernel** in VS Code. There's a Python 2.x and a Python 3.x that are in my `/usr/bin/` folder. These are the version of Python that came with my Mac. I want to use the latest Anaconda version and not these. So, I want all of my packages to be associated with the Anaconda version of Python. 
# 
# ```{figure} ../images/02-kernels.png
# ---
# name: 02-kernels.png
# align: center
# class: with-border
# ---
# You might have a few different versions of Python installed on your computer. You'll want to select the most up-to-date kernel when running your code.
# ```
# 
# ```{hint}
# The interpreter or kernel suggested by VS Code may not be the most up-to-date version.
# ```
# 
# Let's use `pip` to install the [data package for the NASDAQ](https://data.nasdaq.com). You can [set-up an academic account](https://data.nasdaq.com/sign-up) with them before doing this.
# 
# With my account set-up, I can [install the package](https://docs.data.nasdaq.com/docs/python-installation) by running the following in the Terminal **if the `pip` that I'm using is associated with my Anaconda3 install**. This should be the case.
# 
# ```
# pip install nasdaq-data-link
# ```
# 
# You should now **shut down VS Code and open it back up**. 
# 
# You can even go back and check to see if Anaconda now has your library. Open up the Anaconda Navigator and search for the package. 
# 
# Then, in either a Python script or Markdown cell, try the following:
# 
# ```
# import nasdaq-data-link
# ```
# 
# This `pip` method should work for all of the packages that we're using.
# 
# 
# ```{figure} ../images/02-xkcd.png
# ---
# name: 02-xkcd.png
# align: center
# class: with-border
# ---
# Managing Python installs and where everything is located is notoriously difficult.
# ```
# 
# Here's a [nice group of new libraries](https://tryolabs.com/blog/2022/12/26/top-python-libraries-2022). We'll be sticking to the basics, like `pandas`, in this course.
