# Data Analysis in Finance

**Course Notes by Prof. Adam Aiken**

This repository contains the online notes and code examples for a course on data analysis in finance using Python. Built with [Jupyter Book](https://jupyterbook.org/).

## About This Course

This is an introductory finance and data analysis course. Roughly half the students will have Python and SQL coding experience, while the other half will not. The goal is to introduce students to as many ideas as possible. This means Python, but also essential "glue skills" like:

- **Bash/Terminal** - Command line navigation and scripting
- **Git & GitHub** - Version control and collaboration via GitHub Classroom
- **VS Code** - Modern IDE and development environment
- **AI Tools** - Claude Code, GitHub Copilot, and ChatGPT for coding assistance

No programming background is required.

## Repository Structure

```
fin-data-analysis-text/
├── intro.md                 # Welcome page and course overview
├── _config.yml              # Jupyter Book configuration
├── _toc.yml                 # Table of contents
├── requirements.txt         # Python dependencies
├── chapters/                # Course content (notebooks and markdown)
├── images/                  # Figures and screenshots
├── data/                    # Sample datasets
└── _build/                  # Generated HTML output
```

## Course Content

### Part 1: Getting Started
- **Chapter 1**: Finance and Python overview
- **Chapter 2**: Development environment setup
  - Git and GitHub Classroom
  - Markdown basics
  - Python packages
  - Code style
  - Using AI tools (ChatGPT, Copilot)

### Part 2: The Basics
- **Chapter 3**: Python fundamentals
  - Computer science basics
  - NumPy arrays
- **Chapter 4**: Working with data
  - DataFrames
  - Pandas
  - Data cleaning
  - Exploratory data analysis
  - Merging and reshaping
  - SQL basics
  - Polars
- **Chapter 5**: Visualization
  - Seaborn
  - Matplotlib
  - Plotly
- **Chapter 6**: APIs (Nasdaq Data Link)
- **Chapter 7**: Financial time series

### Part 3: Applications
- **Chapter 8**: Portfolio mathematics
- **Chapter 9**: Portfolio optimization
- **Chapter 10**: Unsupervised learning (clustering)
- **Chapter 11**: Factor models
- **Chapter 12**: Regression topics
- **Chapter 13**: Logit models and credit analysis
- **Chapter 14**: Risk management
- **Chapter 15**: Monte Carlo simulation
- **Chapter 16**: Decision trees
- **Chapter 17**: Options
- **Chapter 18**: Trading and backtesting

## Data Files

The `data/` folder contains sample datasets used in the course:
- `ncbreweries.csv` - NC breweries dataset
- `ratios_2016.csv` - Financial ratios data
- `ratios_gics.csv` - GICS sector ratios
- `tr_eikon_eod_data.csv` - End-of-day market data

## Building the Book

```bash
# Install dependencies
pip install -r requirements.txt

# Build the HTML version
jupyter-book build .
```

The generated site will be in `_build/html/`.

## Updating the Online Textbook

To update the live site after making changes:

```bash
# 1. Full rebuild (use --all to force rebuild of all pages)
jb build fin-data-analysis-text --all

# 2. Navigate into the main folder
cd fin-data-analysis-text

# 3. Deploy to GitHub Pages
ghp-import -n -p -f _build/html
```

The `--all` flag forces a complete rebuild, which is useful when you've made changes to styling or configuration that affect all pages.

## Resources

- [Course GitHub Repository](https://github.com/aaiken1/fin-data-analysis-python) - Code and data
- [Course YouTube Playlist](https://www.youtube.com/playlist?list=PLo4Q9ijN3eTG6t2-Lwzf7KlOooypFQak8)
- Textbook: [Machine Learning in Finance (Hull)](https://www-2.rotman.utoronto.ca/~hull/MLThirdEditionFiles/index3rdEd.html)

---

*Last updated: January 2025*
