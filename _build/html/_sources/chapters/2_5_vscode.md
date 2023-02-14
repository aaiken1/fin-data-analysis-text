# VS Code

I am new to [VS Code](https://code.visualstudio.com). I've used R Studio for years, which is a development environment for the [R statistical language](https://www.r-project.org). Designed for R, by [the folks at R Studio](https://www.rstudio.com). It's a wonderful development environment for my day-to-day research.

I am not much of a programmer by training. I've dabbled for over 25 years in a variety of languages, but with only a few years of combined formal training (but only if [Pascal in 1995 counts](https://en.wikipedia.org/wiki/Pascal_(programming_language))). I'm coming to a lot of these tools with fresh, inexperienced eyes.

That said, I really like VS Code. I'm going to show you the basics, how to navigate it, where to find stuff, how to run your code, how to write Markdown in it, and how to get your output. You can do a lot from this one set of windows.

And, it is not just for Python. You know Java? Here you go. C/C++, same. You design web pages? Works for that. Want to learn [OCAML](https://ocaml.org) and [become rich](https://blog.janestreet.com)? Start coding!

You can learn more about this popular coding environment on [their web page tutorials](https://code.visualstudio.com/learn).

They also have a [series of introduction videos](https://code.visualstudio.com/docs/introvideos/basics) that you can watch.

## Using VS Code

We'll discuss the basics of using VS Code in class. We don't need to be experts. But, we'll need to understand our coding environment, how to use extensions, how to see what data we have in memory, how cells and Markdown work, etc.

```{figure} ../images/02-vs-gettingstarted.png
---
name: 02-vs-gettingstarted.png
align: center
class: with-border
---
Opening up VS Code. This is the start-up window that opens by default until you turn it off.
```

VS Code can be used for just about any programming language. We'll be using two types of files: regular Python scripts (.py) and Jupyter notebooks (.ipynb). The latter lets us mix Python and Markdown to create integrated reports.

Visual studio has many helpful tutorials, like this one on using [VS Code with Python](https://code.visualstudio.com/docs/languages/python). 

There'a also a tutorial for using [VS Code and Jupyter Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). Definitely look at this one.

Let's start with the **Explorer**. This is where you'll see your current files and folders. The top button on the left vertical menu bar gets you there, as does Command-Shift-E. I usually **start by opening a folder under File**. This gets what I want in the Explorer window. You'll want to open up your folder for the class.

You can create a new **Jupyter Notebook** in VS Code by hitting Command-Shift-P. This brings up the **command palette**. Search for **Jupyter**. You can also find it under View::Command Palette

These notebooks operate just like the notebooks we saw in actual Jupyter.

```{figure} ../images/02-vs-blank-notebook.png
---
name: 02-vs-blank-notebook.png
align: center
class: with-border
---
A blank Jupyter notebook in VS Code.
```

In a Jupyter notebook, we write our code in **cells**. Click the **+ Code** button at the top to add a code cell. Make sure it is Python - you'll see that in the lower right of this cell. Click the **+ Markdown** button to add a Markdown cell. 

Your labs, exams, and projects are going to be a mix of Markdown and Python. Run some code, show a graph, write-up your results in a nicely formatted way. Python goes in Python cells and Markdown goes in Markdown cells.

Let's look at the other buttons going across the top of your notebook. 

- **Run All** will run all of your cells, Markdown and Python.

- **Clear Output of All Cells** deletes any output that appears below each code cell when it is run. It does not affect anything in memory, like data that you've imported.

- **Restart** clears your Python kernel. This means that all of your work, like data imported, variables created, etc. will be deleted. It **does not** affect your code. You can always just re-run things.

- **Variables** let's you see any data that you've imported. A window will open down below. We don't have any right now. 

- **Outline** uses your Markdown to show you an outline of your written document, like Google Docs. You can also find your outline in the bottom left of the VS Code window. You will be using the Markdown tags `#` and `##` to create headers for your text.

You can run individual cells, all of the cells above the cell you're in, or all of the cells below the one you're in. Each Python cell will give you a single output below it, if there is one. You might also get some feedback from the code, like an error message!

When you run a Markdown cell, you'll get formatted text. Double-click in the cell again to edit the Markdown code. You can also click the **pencil** icon in the upper right of the cell. 


```{figure} ../images/02-vs-extensions.png
---
name: 02-vs-extensions.png
align: center
class: with-border
---
You can see the extensions that I have installed on the left.
```

You can access **extensions** in the bar on the left, or under View:Extensions, or with Command-Shift-X. See the figure above for the extensions that I have installed. 

You definitely need:
- Python
- Pylance
- Jupyter
- Jupyter Keymap
- Jupyter Notebook Renderers
- Markdown All in One

I recommend: 
- Code Spell Checker
- Excel Viewer
- indent-rainbow
- Rainbow CSV
- markdownlint
- Python Indent



### Using Live Share in VS Code

I've never used this feature, but I have tested it and it seems cool. You'll need a Github account to set-up the [Live Share extension in VS Code](https://code.visualstudio.com/learn/collaboration/live-share).


### Tips, tricks, and shortcuts

The more you use VS Code, the faster you'll get. They have a [tips and tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) guide that is helpful.

You'll come across the term **linting**. In fact, the Python extension for VS Code comes with a "linter". Linting is about finding [syntax and stylistic errors in your code](https://code.visualstudio.com/docs/python/linting).

```{margin}
```{note}
If you want the Linux cheat sheet, then you get to teach the class. Those are the rules.
``````

You can also find a [shortcut sheet for Macs](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf) and [one for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf). 
