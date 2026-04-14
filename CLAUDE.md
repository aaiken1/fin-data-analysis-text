# CLAUDE.md - Project Guide for AI Assistants

## Project Overview

This is a **Jupyter Book** for teaching data analysis and Python to undergraduate finance students with **no prior coding background**. The course integrates AI tools (Claude, GitHub Copilot, ChatGPT) throughout, emphasizing that students learn to work *with* AI rather than avoiding it.

**Author**: Prof. Adam Aiken
**Repository**: https://github.com/aaiken1/fin-data-analysis-text
**Live Book**: Built with Jupyter Book and deployed to GitHub Pages

## Core Philosophy

1. **Theory First**: All code should be grounded in financial theory. Students need to understand *why* before *how*.
2. **AI-Integrated Learning**: Students use GitHub Copilot in VS Code/Codespaces, Claude (app and Claude Code), and ChatGPT. They should learn to direct AI tools, not just accept output blindly.
3. **Read and Follow**: Students should be able to read LLM-generated code and understand what it does. They are not expected to write complex code from scratch.
4. **Modern Practices**: Code should reflect what LLMs currently generate - clean, well-documented, using current library APIs.

## Audience

- Undergraduate finance students
- No programming background assumed
- Mixed technical comfort levels
- Goal: Professional data analysis skills for finance careers

## Technology Stack

### Core Libraries
- **pandas** (>=2.0) - Primary data manipulation
- **numpy** (>=1.24) - Numerical computing
- **matplotlib** (>=3.7), **seaborn** (>=0.12), **plotly** (>=5.14) - Visualization
- **scikit-learn** (>=1.2) - Machine learning
- **statsmodels** - Statistical modeling and regression

### Finance-Specific
- **yfinance** - Yahoo Finance data
- **pyportfolioopt** - Portfolio optimization
- **bt**, **ffn** - Backtesting and financial functions
- **fredapi**, **nasdaq-data-link** - Economic/market data APIs

### Development Environment
- **GitHub Codespaces** with VS Code (primary, browser-based)
- Local VS Code with Python virtual environments (alternative)
- Jupyter notebooks for interactive learning

## Book Structure

```
Part 1: Getting Started
├── Chapter 1: Why Python and Finance?
└── Chapter 2: Setup & Environment (Git, Markdown, Packages, Style, AI Tools)

Part 2: The Basics
├── Chapter 3: Computer Science 101 (types, control flow, NumPy)
├── Chapter 4: Working with Data (Pandas, cleaning, EDA, merging, SQL, Polars)
├── Chapter 5: Data Visualization (Seaborn, Matplotlib, Plotly)
├── Chapter 6: Data APIs (FRED, NASDAQ, Databento, WRDS)
└── Chapter 7: Financial Time Series

Part 3: Applications
├── Chapter 8: Portfolio Mathematics
├── Chapter 9: Portfolio Optimization
├── Chapter 10: Unsupervised Learning
├── Chapter 11: Factor Models
├── Chapter 12: Regression Topics
├── Chapter 13: Logit Models & Credit Analysis
├── Chapter 14: Risk Management
├── Chapter 15: Monte Carlo Simulation
├── Chapter 16: Decision Trees
├── Chapter 17: Options
└── Chapter 18: Trading & Backtesting
```

## File Organization

```
fin-data-analysis-text/
├── intro.md                 # Welcome page with course overview
├── _config.yml              # Jupyter Book configuration
├── _toc.yml                 # Table of contents structure
├── requirements.txt         # Python dependencies
├── chapters/                # All chapter content (.ipynb and .md files)
├── data/                    # Sample datasets (CSV files)
├── images/                  # Screenshots, diagrams, charts
└── _build/                  # Generated HTML output (do not edit)
```

## Writing Guidelines

### Content Style
- Start chapters with clear **learning objectives**
- Explain financial concepts and theory *before* showing code
- Use real-world finance examples (stocks, portfolios, credit risk, etc.)
- Keep code cells focused - one concept per cell when possible
- Add markdown explanations between code cells

### Code Style
- Write code that mirrors what LLMs generate (clean, documented, modern APIs)
- Use descriptive variable names (`stock_returns` not `sr`)
- Include inline comments for non-obvious operations
- Avoid deprecated methods - use current pandas/numpy idioms
- Show complete, runnable examples

### AI Tool References
When discussing AI tools, cover:
- **GitHub Copilot**: Autocomplete-style suggestions in VS Code
- **Claude/ChatGPT**: Chat-based assistance for explanation and debugging
- **Claude Code**: Agentic AI for complex, multi-step tasks
- Emphasize *directing* AI (good prompts) and *verifying* output

## Build Commands

```bash
# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the book
jupyter-book build .

# Force complete rebuild (for config/style changes)
jupyter-book build . --all

# Deploy to GitHub Pages
ghp-import -n -p -f _build/html
```

## Common Tasks

### Adding a New Chapter
1. Create `.ipynb` or `.md` file in `chapters/`
2. Add entry to `_toc.yml` in appropriate section
3. Follow naming convention: `{number}_{topic}.ipynb`

### Adding Images
1. Place image files in `images/` directory
2. Reference in markdown: `![description](../images/filename.png)`

### Using Data Files
- Sample data in `data/` directory
- For API data, use `.env` files for API keys (never commit keys)
- Common sources: yfinance, FRED, NASDAQ Data Link

## Key Conventions

### Notebook Naming
- `{chapter}_{section}_{topic}.ipynb` (e.g., `4_2_cleaning_data.ipynb`)
- Intro files use `.md` format (e.g., `4_intro.md`)

### Code Patterns Students Should Recognize
```python
# Data loading
import pandas as pd
df = pd.read_csv('data/file.csv')

# Stock data
import yfinance as yf
data = yf.download('AAPL', start='2020-01-01')

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(figsize=(10, 6))

# Portfolio optimization
from pypfopt import EfficientFrontier, expected_returns, risk_models
```

### Theory Topics to Emphasize
- Returns (simple vs. log)
- Risk measures (volatility, VaR, CVaR)
- Portfolio theory (Markowitz, efficient frontier)
- Factor models (CAPM, Fama-French)
- Regression diagnostics
- Classification metrics (credit risk context)
- Time series concepts (stationarity, autocorrelation)

## Important Notes

- **Execution**: Notebooks are re-executed on each build (timeout: 120 seconds)
- **API Keys**: Use `python-dotenv` and `.env` files for secure key storage
- **Browser Compatibility**: Plotly charts require specific Jupyter Book config (already set)
- **Main Branch**: Repository uses `master` as the main branch

## Related Resources

- **Code Repository**: https://github.com/aaiken1/fin-data-analysis-python
- **Reference Text**: Hull's "Machine Learning in Finance"
- **Video Lectures**: Available on YouTube (linked in intro.md)
