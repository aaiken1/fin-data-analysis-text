# Regression and supervised machine learning

We've looked at **unsupervised machine learning**, clustering, and dimension reduction. Now we turn to **supervised machine learning**, where we have a target variable that we are trying to predict using a set of features.

We'll start with **linear regression** -- the workhorse of econometrics and finance. If you've taken a statistics course, you've seen this before. The idea is simple: find the best-fitting line through your data. But the details matter, and this chapter covers quite a bit of ground.

```{note}
If you are doing anything even remotely "quant" or data science or analytics for a job, you should know regression really, really well.
```

## What you'll learn

By the end of this chapter, you should be able to:

- Run and interpret **OLS regressions** in Python using `statsmodels`
- Understand how to use **indicator and categorical variables** in regression
- Explain the difference between **explaining** and **predicting**
- Use **Ridge, Lasso, and Elastic Net** regularization to handle many correlated features
- Follow the **machine learning workflow**: split data, standardize, train, validate, and test
- Build **pipelines** in `sklearn` that combine preprocessing and modeling steps
- Think critically about what ML can and cannot do in **financial markets**

## Chapter structure

This chapter is divided into four sections:

| Section | Topic | Key Ideas |
|---------|-------|-----------|
| **OLS Regression** | Running regressions with `statsmodels` | Interpreting output, indicators, categorical variables |
| **Regularization** | Ridge, Lasso, and Elastic Net | Shrinkage, feature selection, hyperparameters |
| **ML Workflow** | The `sklearn` prediction pipeline | Train/test splits, standardization, cross-validation, pipelines |
| **ML and Markets** | Can ML beat the market? | Model horse races, position sizing, practical lessons |

## Two libraries, two perspectives

We run linear regressions two ways in these notes:

- **`statsmodels`**: Traditional regression output. You specify a formula, get a nice table with coefficients, standard errors, t-statistics, and p-values. Very much like Excel's Data Analysis Toolkit or what you'd see in an econometrics class.

- **`sklearn`**: Machine learning style. You create X and y data frames, fit a model object, and focus on prediction rather than interpretation. This is what the Hull textbook uses for Ridge, Lasso, and Elastic Net.

Two libraries, two ways to think about the same underlying math. You should be comfortable reading output from both.

## Hull textbook references

These notes draw from several chapters in Hull:

- **Chapter 1**: Introduction to machine learning, supervised vs. unsupervised learning
- **Chapter 3**: Linear regression, Ridge, Lasso, Elastic Net
- **Chapter 10**: Interpreting regression results

## Other important sources

- [Coding for Economists - Regression](https://aeturrell.github.io/coding-for-economists/econmt-regression.html) covers just about everything you need to know to do basic linear regression in Python
- [Coding for Economists - Diagnostics](https://aeturrell.github.io/coding-for-economists/econmt-diagnostics.html) discusses how to check if your model is doing a good job
- [The Effect](https://theeffectbook.net) is a great book for understanding causality and regression. [Chapter 13](https://theeffectbook.net/ch-StatisticalAdjustment.html) covers regression with R code
- [sklearn linear regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) documentation
- [sklearn coefficient interpretation](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html) guide

## Using AI for regression

Regression is an area where AI tools are incredibly helpful:

- **Interpreting output**: Paste your regression summary into Claude and ask "What do these results mean?"
- **Debugging models**: "Why is my R-squared so low?" or "Why are my coefficients all insignificant?"
- **Choosing between methods**: "Should I use Ridge or Lasso for this problem?"
- **Writing sklearn pipelines**: "Help me create a pipeline that standardizes my data and runs a Lasso with cross-validation"

```{tip}
When asking AI about regression, give it context. Say "I'm predicting housing prices using square footage, bedrooms, and zip code" rather than just "run a regression." The more context you provide, the better the guidance.
```
