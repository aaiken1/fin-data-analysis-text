# Welcome

**Spring 2026 with Prof. [Adam Aiken](https://aaiken1.github.io)**

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

## Why These Skills Matter

The tools and workflows in this course reflect how finance professionals actually work today. At investment banks, hedge funds, asset managers, and fintech companies, you'll find:

- **Python everywhere** - From quantitative research to risk management to automating Excel reports, Python has become the common language of finance.
- **Version control is expected** - Teams use git and GitHub (or GitLab/Bitbucket) to collaborate on code, track changes, and maintain reproducibility.
- **The terminal isn't optional** - Whether you're SSH-ing into a server, running a backtest, or deploying a model, command-line fluency is essential.
- **AI tools are the new normal** - Analysts and developers use GitHub Copilot, Claude, and ChatGPT daily. Knowing how to prompt effectively and review AI-generated code is now a core skill.

This course is designed for students with varying backgrounds. About half of you have Python and SQL experience; the other half are starting fresh. That's fine. The goal isn't to make you a software engineer - it's to give you enough fluency that you can learn what you need on the job and collaborate with technical teams.

## Course Goals

By the end of this course, you will:

- **Set Up a Professional Coding Environment**: Use GitHub, VS Code, and GitHub Codespaces - the same tools used at top finance firms. Learn git for version control and collaboration.
- **Work Effectively with AI Coding Assistants**: Use Claude Code, GitHub Copilot, and ChatGPT to accelerate your workflow, debug code, and learn new techniques. Understand when to trust AI output and when to verify.
- **Master Python Basics**: Gain a solid understanding of Python programming, including data structures, functions, and libraries essential for data analysis.
- **Perform Data Analysis**: Import, clean, and manipulate data using Pandas and NumPy - the workhorses of financial data analysis.
- **Visualize Data**: Create insightful visualizations using Matplotlib, Seaborn, and Plotly to communicate findings to technical and non-technical audiences.
- **Apply Machine Learning Techniques**: Understand and implement models used in finance, including regression, classification (logit), and clustering.
- **Integrate Finance Knowledge**: Apply your coding skills to real financial problems: factor models, portfolio optimization, risk management, and options.
- **Develop Analytical Reports**: Combine code, output, and narrative in Markdown and Jupyter notebooks - the format used for research reports and model documentation in industry.

## AI Coding Assistants

```{note}
No programming background is required for this class. AI tools make it easier than ever to get started - but you still need to understand what the code is doing.
```

Learning to code in 2026 means learning to work *with* AI. These tools won't write your code for you (well, they will, but you need to verify it), but they will dramatically accelerate your learning and productivity. Professionals use these tools daily - you should too.

### Your AI Toolkit

**Claude Code** - An agentic coding assistant that runs in your terminal. Unlike chat-based tools, Claude Code can read your files, run commands, and make edits directly. It's particularly powerful for:
- Exploring unfamiliar codebases ("What does this function do?")
- Debugging ("Why is this throwing an error?")
- Refactoring ("Clean up this code and add comments")
- Learning ("Explain this pandas operation step by step")

You can install it and get started at [claude.ai/download](https://claude.ai/download). We'll use it extensively in class.

**GitHub Copilot** - An AI pair programmer that lives inside VS Code. As you type, it suggests completions - sometimes a single line, sometimes entire functions. It's free for [verified students](https://education.github.com/pack) through the GitHub Student Developer Pack. Once you link it to your Codespaces environment, it's always there.

**Claude and ChatGPT** - Chat-based assistants for when you need to have a conversation about your code, understand a concept, or get help with an error message. Both have free tiers:
- [Claude](https://claude.ai) (Anthropic)
- [ChatGPT](https://chat.openai.com) (OpenAI)

### How to Use AI Tools Effectively

1. **Start with a clear question** - "Fix my code" is worse than "Why does this pandas merge produce duplicate rows?"
2. **Provide context** - Paste the relevant code, the error message, and what you expected to happen.
3. **Don't just copy-paste** - Read the explanation. Run the code line by line. Make sure you understand *why* it works.
4. **Verify the output** - AI tools hallucinate. They confidently suggest functions that don't exist and approaches that won't work. Always test.
5. **Use AI to learn, not to avoid learning** - The goal is fluency. If you can't explain what your code does, you don't understand it yet.

### More Resources on AI for Coding

- [Datacamp - ChatGPT prompts for data science](https://www.datacamp.com/cheat-sheet/chatgpt-cheat-sheet-data-science)
- [MIT Sloan - ChatGPT for data analysis](https://mitsloanedtech.mit.edu/ai/tools/data-analysis/how-to-use-chatgpts-advanced-data-analysis-feature/)
- [AI prompts for economists](https://sites.google.com/view/lastunen/ai-for-economists?authuser=0)
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Anthropic's prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Bloomberg Odd Lots: Claude Code](https://www.youtube.com/watch?v=DcZWMQ_UL2o) - A podcast episode discussing Claude Code and agentic AI coding tools.

## Getting Help (The Old-Fashioned Way)

AI tools are great, but sometimes you need other resources:

- **Stack Overflow** - Search for error messages and common problems. Millions of questions already answered.
- **Official documentation** - [Pandas docs](https://pandas.pydata.org/docs/), [NumPy docs](https://numpy.org/doc/), [Matplotlib docs](https://matplotlib.org/stable/contents.html). Learn to read the docs.
- **Your classmates** - Talking through a problem often solves it.
- **Office hours** - When you're truly stuck.

The key to learning to code: go slowly, line by line, and think like a computer. They do exactly what you tell them to do. No more, no less.

## Sources

I have pulled material from many different sources in order to create these notes and I am very grateful that they have made their work available. For example, I include commentary on examples from our book. There are also many other excellent and, often, free guides to using Python, Jupyter notebooks, and VS Code.

For each topic we cover, I'll let you know if I'd like you to read or watch something beyond what's in these notes.

[The Python Tutorial](https://docs.python.org/3/tutorial/index.html). This is the main tutorial from the folks who develop Python. I'll refer to it throughout the text if you want a more in-depth look at something.

[Python for Finance, 2e](https://www.oreilly.com/library/view/python-for-finance/9781492024323/). This is one of the few "python and finance" books, though it jumps from the basics into more advanced material quite quickly. This textbook also has a Github repository that [contains the code used in the book](https://github.com/yhilpisch/py4fi2nd).

There are also many free resources available. The key is being able to find what's helpful - web searches can be hit or miss, so stick to established resources and official documentation. While these guides are not finance-related, *per se*, they cover material that will come up in any sort of data science project. I thank the authors for making these resources available and I use examples from them in my notes.

[Coding for Economists](https://aeturrell.github.io/coding-for-economists/intro.html) is an excellent online book that discusses getting Python set up, importing and exploring your data, as well as more advanced econometrics topics that we won't get into here. But, if you're using STATA in another class, I recommend taking a look at what you can do for free in Python. You might not have that STATA license on the job! He even tells you how to automate your VS Code set-up, if you're into that kind of thing.

[Python Programming for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/README.html) is another great, general resource. You'll find a discussion of the basics, along with a Python style guide for writing readable code, details and about NumPy and Pandas, and tips for data wrangling and cleaning.

[Python for Data Analysis, 3E](https://wesmckinney.com/book/) is also available for free online. The author has just updated to a third edition.

[The StatQuest YouTube Channel](https://www.youtube.com/@statquest) is a good place to see get additional explanation about some of the statistical techniques that we'll see in this class.

[The History of Python](https://www.youtube.com/watch?v=GfH4QL4VqJ0) - A brief history of Python, from its creation by Guido van Rossum in the late 1980s to its rise as one of the most popular programming languages in the world.

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
