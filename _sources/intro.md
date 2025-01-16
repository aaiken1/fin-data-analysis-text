# Welcome

**Spring 2025 with Prof. [Adam Aiken](https://aaiken1.github.io)**

```{image} /images/elon-signature.png
:alt: elon-signature
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{note}
This is a living textbook. I will be updating the notes and making improvements as we go.
```

Welcome! This online text contains my notes and code examples. There are essentially three parts to this course. First, we'll get set-up and become comfortable with our coding environment. We will be using Github Classroom and VS Code within Github Codespaces.

We also have a course [Github repository](https://github.com/aaiken1/fin-data-analysis-python), where I will keep data and code (e.g. Jupyter notebooks) that we use in class.

We also have a course [YouTube page](https://www.youtube.com/playlist?list=PLo4Q9ijN3eTG6t2-Lwzf7KlOooypFQak8), where I will post the occasional video, as needed. Most of our work will of course be done in class together.

Our labs and exams are posted using Github Classroom. You'll find links to these on Moodle.

The most important part is to make sure that you are up and running with Github, Jupyter Notebooks, and Github Codespaces/VS Code. We'll discuss how to get started in [Chapter 2](chapters/2_intro.html#python_set-up). Your coding environment can be entirely **browser-based**, if you choose to do so. If you have some experience with IDEs and git, you can use a local install as well. 

```{hint}
Bookmark important links so that you don't have to go searching for them.
```

We also have a textbook on [machine learning in finance](https://www-2.rotman.utoronto.ca/~hull/MLThirdEditionFiles/index3rdEd.html). If you've taken a derivatives class, you might have seen the author's other textbook - every derivatives trader in the world has read Hull. We'll get to these topics more in the second-half of the course.

## Course Goals
By the end of this course, you will:

- **Set Up Your Coding Environment**: Learn how to use Github Classroom, VS Code, and Github Codespaces for data analysis. Datacamp exercises will cover git and using ChatGPT for coding.
- **Master Python Basics**: Gain a solid understanding of Python programming, including data structures, functions, and libraries essential for data analysis.
- **Perform Data Analysis**: Learn how to import, clean, and manipulate data using libraries such as Pandas and NumPy.
- **Visualize Data**: Create insightful visualizations using Matplotlib, Seaborn, and Plotly to effectively communicate your findings.
- **Apply Machine Learning Techniques**: Understand and implement basic machine learning models, including linear regression, logit models, and clustering.
- **Integrate Finance Knowledge**: Apply your coding skills to financial data, exploring topics such as factor models, risk management, and options trading.
- **Develop Analytical Reports**: Combine code, output, and text in Markdown reports to create comprehensive analytical documents.

## Getting help

```{note}
No programming background is required for this class. For both students and instructor.
```

Learning to code means learning how to get help. No one has all of this stuff in their head at all times. That means using our textbook, the online books above, cheatsheets, and other resources. The links posted above will help a lot.

You can find help on [Stackoverflow](https://stackoverflow.com), though "copy and paste" isn't really the best way to learn to code. Go slowly, line-by-line, and try to think like a computer. They do exactly what you tell them to do. No more, no less.

Even better, you can use tools such as [ChatGPT](https://openai.com/chatgpt) and [Github Copilot](https://github.com/features/copilot/) to help you code. We'll look at [some examples](https://www.datacamp.com/tutorial/chatgpt-data-science-projects) as we go, but you should have one of these tools open whenever you are coding. The basic version of ChatGPT is free. Github Copilot is free for [verified students](https://education.github.com/pack), so sign-up! You'll be able to link it to your Codespaces and VS code installs, as I'll show you.

Some more suggestions for using ChatGPT in data projects:

- [Datacamp - suggested prompts](https://www.datacamp.com/cheat-sheet/chatgpt-cheat-sheet-data-science)
- [MIT Sloan Tech Review - ChatGPT 4 and Data Analysis](https://mitsloanedtech.mit.edu/ai/tools/data-analysis/how-to-use-chatgpts-advanced-data-analysis-feature/)
- [AI prompts for economists](https://sites.google.com/view/lastunen/ai-for-economists?authuser=0)

## Sources

I have pulled material from many different sources in order to create these notes and I am very grateful that they have made their work available. For example, I include commentary on examples from our book. There are also many other excellent and, often, free guides to using Python, Jupyter notebooks, and VS Code.

For each topic we cover, I'll let you know if I'd like you to read or watch something beyond what's in these notes. 

[The Python Tutorial](https://docs.python.org/3/tutorial/index.html). This is the main tutorial from the folks who develop Python. I'll refer to it throughout the text if you want a more in-depth look at something.

[Python for Finance, 2e](https://www.oreilly.com/library/view/python-for-finance/9781492024323/). This is one of the few "python and finance" books, though it jumps from the basics into more advanced material quite quickly. This textbook also has a Github repository that [contains the code used in the book](https://github.com/yhilpisch/py4fi2nd).

There are also many free resources available. The key is being able to find what's helpful - web searches often lead you to awful AI-generated Medium posts. While these guides are not finance-related, *per se*, they cover material that will come up in any sort of data science project. I thank the authors for making these resources available and I use examples from them in my notes.

[Coding for Economists](https://aeturrell.github.io/coding-for-economists/intro.html) is an excellent online book that discusses getting Python set up, importing and exploring your data, as well as more advanced econometrics topics that we won't get into here. But, if you're using STATA in another class, I recommend taking a look at what you can do for free in Python. You might not have that STATA license on the job! He even tells you how to automate your VS Code set-up, if you're into that kind of thing.

[Python Programming for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/README.html) is another great, general resource. You'll find a discussion of the basics, along with a Python style guide for writing readable code, details and about NumPy and Pandas, and tips for data wrangling and cleaning.

[Python for Data Analysis, 3E](https://wesmckinney.com/book/) is also available for free online. The author has just updated to a third edition.

[The StatQuest YouTube Channel](https://www.youtube.com/@statquest) is a good place to see get additional explanation about some of the statistical techniques that we'll see in this class.

[DataCamp](https://www.datacamp.com/cheat-sheet) also has lots of mini-tutorials and **cheatsheets** that can help get you started. We are going to see all of these tools this semester.

- [Python Basics](https://www.datacamp.com/cheat-sheet/python-for-data-science-a-cheat-sheet-for-beginners)
- [The Shell/Terminal](https://www.datacamp.com/cheat-sheet/bash-and-zsh-shell-terminal-basics-cheat-sheet)
- [git](https://www.datacamp.com/cheat-sheet/git-cheat-sheet)
- [Markdown](https://www.datacamp.com/cheat-sheet/markdown-cheat-sheet-23)
- [OpenAI API](https://www.datacamp.com/cheat-sheet/the-open-ai-api-in-python)
- [Supervised Machine Learning](https://www.datacamp.com/cheat-sheet/supervised-machine-learning-cheat-sheet)
- [Unsupervised Machine Learning](https://www.datacamp.com/cheat-sheet/unsupervised-machine-learning-cheat-sheet)
- [Dates and Times](https://www.datacamp.com/cheat-sheet/working-with-dates-and-times-in-python-cheat-sheet)
- [Juypter Notebooks - how we will write our code](https://www.datacamp.com/cheat-sheet/jupyter-notebook-cheat-sheet)
- [Numpy - arrays and numerical computing](https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python)
- [Pandas - data frames](https://www.datacamp.com/cheat-sheet/reshaping-data-with-pandas-in-python)
- [Data Wrangling in Python - cleaning up that mess of data](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-data-wrangling-in-python)
- [Matplotlib - visualizing our data](https://www.datacamp.com/cheat-sheet/matplotlib-cheat-sheet-plotting-in-python)
- [Seaborn - another visualization package with better looking output](https://www.datacamp.com/cheat-sheet/python-seaborn-cheat-sheet)
- [Scikit Lean - basic machine learning in Python](https://www.datacamp.com/cheat-sheet/scikit-learn-cheat-sheet-python-machine-learning)
- [SciPy - linear algebra in Python because everything is linear algebra](https://www.datacamp.com/cheat-sheet/scipy-cheat-sheet-linear-algebra-in-python)

Here's a collection of non-DataCamp cheat sheets.

- [Comprehensive Python Cheatsheet](https://gto76.github.io/python-cheatsheet/)

I have also found the [The Self-Taught Programmer](https://www.theselftaughtprogrammer.io) a useful book, especially for someone like me, who does write code for research, but has only had a few formal computer science courses.

If you've used R in the past, here's a [guide to setting up Python to be more like R](https://www.emilyriederer.com/post/py-rgo/).





