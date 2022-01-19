# Installation

Let's go through our two installs: [Anaconda](https://www.anaconda.com/products/individual) and [VS Code](https://code.visualstudio.com).

## Anaconda

You want to start by installing [Anaconda](https://www.anaconda.com/products/individual). Anaconda gives you the latest version of Python, as well as automatically installs many different Python libraries. Libraries extend what Python can do and include [numpy](https://numpy.org) and [pandas](https://pandas.pydata.org), two libraries that are critical for dealing with data.

```{margin} Python on Elon's Computers
You'll find the Anaconda Navigator on Elon computers across campus. This let's you use Jupyter notebooks when you don't have your machine. You can also use this install in our lab.
```

Anaconda will handle all of the set-up for us. Download and install the version that is appropriate for your machine. The process is fairly straightforward.

```{figure} ../images/02-anaconda.png
---
name: 02-anaconda.png
align: center
class: with-border
---
The Anaconda Individual install page. Note that you can see the Python version that you are installing. You want 64-bit for either Mac or Windows. The webpage will detect the version best for you. 
```

Anaconda also gives us the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/index.html). This let's you see what Anaconda has installed. You find the Navigator on your machine, installed as an application. 

```{figure} ../images/02-anaconda-nav.png
---
name: 02-anaconda-nav.png
align: center
class: with-border
---
My Anaconda Navigator layout when I open it. See the Jupyter Notebook button? This is what you'll want. Your layout will likely look a bit different from mine.
```



## VS Code

Once you have Anaconda installed, you should install [VS Code](https://code.visualstudio.com/Download).

Click the big buttons on the page that correspond to your operating system.

And that's about it. We'll cover how to use Jupyter notebooks and VS Code next.

```{figure} ../images/02-vs-code.png
---
name: 02-vs-code.png
align: center
class: with-border
---
My Anaconda Navigator layout when I open it. See the Jupyter Notebook button? This is what you'll want. Your layout will likely look a bit different from mine.
```

## An Aside: Files and file paths

We'll go over absolute and relative file paths in class. You can see the notebook `1-file-paths.ipynb` on our Github page for some examples.

```{margin} Know where you stuff is!
It is very important that you use a consistent organization and structure. Files, folders, and paths are very important. **If you are using the lab computers, bring your own USB Drive**.
```

My layout is simple. A folder for this class. Then, inside that folder, I have the following sub-folders: data, output, images, and code. 

```{figure} ../images/02-my-files.png
---
name: 02-my-files.png
align: center
class: with-border
---
My class folder, **fin-data-analysis-python** and sub-folders. You won't have the readme.md file. That is generating the Read Me text on Github. You also probably don't have hidden files and folders visible on your machine.
```

When I open up Jupyter or VS Code, I open up that class folder. Then, I can see my folder structure. I then use **relative file paths** to open and save files. 


