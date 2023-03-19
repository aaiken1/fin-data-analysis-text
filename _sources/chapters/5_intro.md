# Data visualization

Data visualization and design play important roles in finance. We are often looking at **time series** data, such as plots of stock returns. We are comparing different firms at the same point in time using **cross-sectional** data. We also follow a set of firms through time using **panel** data. 

Some data work is **exploratory**, where you want to see what you have, look for outliers, mistakes, etc. Other graphics will make it into a final presentation or client report. Python can do all of this.

This section follows Chapter 7 of [Python for Finance, 2e](https://www.oreilly.com/library/view/python-for-finance/9781492024323/) and discusses using [matplotlib](https://matplotlib.org) to create graphics in Python. 

However, there are many, more modern plotting libraries available for Python, such as `plotly`, `seaborn`, `bokeh`, and `altair`. Some of these, like [plotly](https://plotly.com) and [bokeh](https://bokeh.org), let you build interactive graphics. We'll look a little bit at [plotly](https://plotly.com/python/) and [seaborn](https://seaborn.pydata.org).

We'll focus on financial data and the basic building blocks of creating plots, but just be aware that these packages can do a lot more.

The [Intro to Data Visualisation](https://aeturrell.github.io/coding-for-economists/vis-intro.html) for *Coding for Economists* covers some basic design principles. His section [Narrative Data Visualisation](https://aeturrell.github.io/coding-for-economists/vis-narrative.html) expands on these ideas. He discusses the "anatomy" of figures and how to choose the best plot for your data.

Another [concise guide](https://www.mit.edu/~amidi/teaching/data-science-tools/study-guide/data-visualization-with-python/), this time for data viz. Note the use of `seaborn`.


```{figure} ../images/05-softbank.jpeg
---
name: 05-softbank.jpeg
align: center
---
Our goal: Make figures that are more informative than this. Source: <https://nymag.com/intelligencer/2019/11/softbanks-insane-presentation-on-how-it-will-fix-wework.html>.
```
