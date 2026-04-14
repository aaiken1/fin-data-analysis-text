# Python set-up <a id='python_set-up'></a>

We are going to start by getting you set-up in [Github](https://github.com) and Codespaces. I'll go through how our assignments are going to work in Github Classroom. These tools mean that you can do all of your coding **in your browser** using what are called [Jupyter notebooks](https://jupyter.org), but in an environment that acts like the common VS Code desktop setup, including [version control](https://ourcodingclub.github.io/tutorials/git/) with git and Github.

Our **Day One Set-Up**:

1. Sign-up for a Github account: <https://github.com/signup>. Use your **Elon email address**.
2. Set-up your personal Github page. You should add your own readme.md file.
3. Linking your Github account to our Github Classroom using the link on Moodle by accepting Lab00.
4. Open a VS Code instance in Github Codespaces. Make sure that we can see files associated with the lab. Learn about the layout of VS Code, including how to install packages.
5. Learn about git. Where are our files when we work in a Codespace? What are repos? How can we move files around and submit assignments? How can you download your work to your local drive?
6. Learn about Jupyter Notebooks. Jupyter Notebooks let you mix Python and Markdown and are what we will do our work in.
7. Set up AI coding assistants. We'll use GitHub Copilot (built into Codespaces), Claude, and Claude Code to help us write and debug code.

See the next few sections for more on each of these topics.


## AI coding assistants

AI tools have transformed how we write code. But not all AI coding tools work the same way. Understanding the difference is crucial for using them effectively.

### The Old Way: Autocomplete

The first wave of AI coding tools — like GitHub Copilot — work like very smart autocomplete. As you type, they suggest what might come next. You're still in control. You're still writing the code. The AI just finishes your sentences.

This is useful. It speeds up typing, helps with syntax you've forgotten, and fills in boilerplate. But fundamentally, **you're still doing the work line by line**.

### The New Way: Agentic Coding

**Agentic AI** is fundamentally different. Instead of suggesting completions, it **takes actions**. You describe what you want in plain English, and the AI:

- Reads your files to understand the project
- Plans what needs to be done
- Writes the code across multiple files
- Runs it to check for errors
- Iterates until it works
- Asks for your approval before saving changes

This is a paradigm shift. You're no longer typing code — you're **directing an AI that writes code for you**. Tools like Claude Code, Cursor, and GitHub Copilot's new Agent Mode work this way.

### Why This Matters

Agentic coding changes what skills are valuable:

| Less Important | More Important |
|----------------|----------------|
| Memorizing syntax | Knowing what to build |
| Typing speed | Evaluating AI output |
| Writing boilerplate | Domain expertise |
| Looking up function arguments | Project management |

The programmer's job is shifting from "person who writes code" to "person who directs AI to write code and verifies the results." This is happening **right now**, and the pace of change is accelerating.

```{tip}
Learning to use agentic AI tools effectively might be the most valuable skill you develop in this course. The students who figure this out early will have a significant advantage — not just in this class, but in their careers.
```

### What We'll Use

In this class, you have access to three AI coding assistants:

| Tool | Style | Where | Best For |
|------|-------|-------|----------|
| **GitHub Copilot** | Autocomplete | Inside Codespaces | Quick suggestions as you type |
| **Claude** (browser) | Conversational | claude.ai | Explaining concepts, planning, debugging |
| **Claude Code** | Agentic | Desktop app | Complex tasks, multi-file projects |

You'll likely use all three. Copilot keeps you productive while typing. Claude in the browser helps you understand concepts and plan your approach. Claude Code handles the big tasks where you'd rather describe what you want than write every line yourself.

These tools can help you write code faster, debug errors, and learn new techniques. But they're not magic — you still need to understand what you're asking for and verify that the output is correct. A human is still responsible for the output, even if a machine wrote every line. 

See the [AI Coding Assistants](2_4_using_ai.ipynb) section for setup instructions, detailed examples, and best practices.



## Other resources and tools

From VS Code, we can also use Jupyter notebooks. I would encourage you to get very comfortable with the Jupyter notebook format and VS Code. We'll go over everything in class as well.

The [Writing Code section from Coding for Economists](https://aeturrell.github.io/coding-for-economists/code-where.html) is a great place to start. His [Code Preliminaries](https://aeturrell.github.io/coding-for-economists/code-preliminaries.html) section also introduces some important ideas, like IDEs, packages, and VS Code.

You can read more about Python and its history in [Chapter 1 of Python for Data Analysis, 3E](https://wesmckinney.com/book/preliminaries.html). [Chapter 2 discusses Python basics](https://wesmckinney.com/book/python-basics.html), like Jupyter notebooks, in detail.

Getting started in Python isn't easy. Even if you're coming from another programming background, like Java, or a statistical language, like R. Data scientist (and [good Twitter follow](https://twitter.com/vboykis)) Vicki Boykis has written about why [getting started in Python can be hard](https://vickiboykis.com/2018/03/12/its-still-hard-for-beginners-to-get-started-with-python/).

This is a [nice article on a modern Python data "stack"](https://www.emilyriederer.com/post/py-rgo/), especially if you're coming from R. Note how she suggests using `seaborn` and `polars`, two newer packages, in place of `matplotlib` and `pandas`.

This course is focused on using Python (and the VS Code IDE, Markdown, etc.) to solve financial problems. However, if you're interested in building a full set of data/analytics tools, you need to know more.

This article, also by Vicki Boykis, outlines the need to learn three additional tools: [Git, SQL, and the command line](https://vickiboykis.com/2022/01/09/git-sql-cli/). I use all three in my day-to-day work, though I'm far from an expert in any of them. **If you are thinking about working with data as a career, you should know these three tools.** Our DataCamps will cover the basics of git and the command line. We'll use both inside of Github Classroom and Codespaces.

Our notes touch on SQL, which is the standard database query language.