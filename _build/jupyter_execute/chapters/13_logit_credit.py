#!/usr/bin/env python
# coding: utf-8

# # Logit models
# 
# Linear regressions ((ordinary least squares, or OLS)) tells us about the association between a **dependent**, or Y variable, and a set of **independent**, or X variables. Regression does not tell us anything about one variable causing another or if the correlations we find have any real meaning. It is simply a [statistical technique](https://www.statology.org/linear-regression-assumptions/) for finding a linear relationship between two variables. The meaning of that relationship is up to us and the ideas that we are working with. In finance, we usually have an economic model in mind, such as the CAPM, that gives meaning to the relationship that we find.
# 
# A **logit regression** does something similar, except that it was developed for when our dependent variable is **binary**, a Yes or No. Logistic regression is a regression model where the response variable Y is **categorical**, as opposed to **continuous**. These types of models are used for **classification**. Why do we need a new model? We want a model that can give us **probabilities** for an event. Regular regression isn't set up to do this
# 
# We will look at a type of data that is commonly used with logit models in finance: credit card default data. This data set has a **binary outcome**. Did the credit card user default? Yes or No? 1 or 0?
# 
# This data is from the DataCamp module on credit risk analysis.
# 
# We'll start with some usual set-up, bringing the data in, and taking a peak.
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Include this to have plots show up in your Jupyter notebook.
get_ipython().run_line_magic('matplotlib', 'inline')

loans = pd.read_csv('https://raw.githubusercontent.com/aaiken1/fin-data-analysis-python/main/data/loan_data.csv', index_col=0)  


# There are no dates in this data, so no dates to parse. The first column is simply the row number, so I'll make that my index.

# ## Cleaning our data
# 
# Let's get started by just looking at what we have.

# In[2]:


loans.info()


# We are interested in explaining the *loan_status* variable. In this data set, *loan_status = 1* means that the credit card holder has defaulted on their loan. What explains the defaults? The loan amount? Their income? Employment status? Their age?

# In[3]:


loans.describe()


# Note the units. Loan amount appears to be in dollars. The max of \$35,000 reflects the general limit on credit card borrowing - these aren't mortgages. Interest rate is in percents. The median credit card rate in this sample is 10.99%. Employment length is in years, as is age. Annual income is in dollars. Note the max values for *annual_inc* and *age*!
# 
# Home ownership and grade do not appear, since they are text variables, not numeric. Grade is some kind of overall measure of loan quality.
# 
# Let's convert the two object variables to [categorical variables](https://www.tutorialspoint.com/python_pandas/python_pandas_categorical_data.htm) so that we can deal with them. This code puts all of the **object** columns into a list and then loops through that list to change those columsn to type **category**. 

# In[4]:


list_str_obj_cols = loans.columns[loans.dtypes == 'object'].tolist()
for str_obj_col in list_str_obj_cols:
    loans[str_obj_col] = loans[str_obj_col].astype('category')

loans.dtypes


# Looks good! I'm now going to add `include='all'` to `describe` to give more information about these categorical variables.
# 

# In[5]:


loans.describe(include='all')


# This doesn't show us all of the possible values, but at least we can see the number of values that aren't missing, as well as a count of unique values. Let's get a list of possible values for each categorical variable.

# In[6]:


loans['grade'].value_counts()


# In[7]:


loans['home_ownership'].value_counts()


# 
# We can use `sns.pairplot` from the `seaborn` library to get a nice visualization of the relationships between our variables. The diagonal plots show the **denisity plots** for that one variable, but split between *loan_status*. The off-diagonal plots show the relationship between two of the explanatory (X) variables, but with each observation color-coded based on a third variable, their default status. 
# 
# Orange means that the person has defaulted. 

# In[8]:


sns.pairplot(loans, hue='loan_status')


# What jumps out to you? First I see some outliers in age. Someone is over 140 years old in the data! We should drop that observation.
# 
# There's also one individual with a really large annual income. We could also drop that one observation. Outlier observations can overly influence our regression results, though there are techniques for dealing with that. 
# 
# We can also visually see some of the relationships. Look up and down the *int_rate* column. Generally, there are more orange dots when the interest rate is higher. Look at the second row, second column. The mean of the smaller density is to the right of the larger one. The smaller one has an orange border and shows the distribution of interest rates on the loans that defaulted.
# 
# Look at the third row, second column. There are more orange dots in the higher interest rate, shorter employment length part of the distribution. Look at the fifth row, second column. Loans that defaulted tended to be younger and with higher interest rates.

# I am going to clean up two of the outliers - the one for annual income and the one for age. I'll also drop any row with a missing value. 
# 
# When done, I'll re-check my data.

# In[9]:


loans = loans[loans['annual_inc'] < 6000000]
loans = loans[loans['age'] < 144]

loans = loans.dropna()

loans.describe(include='all')


# That seems better. Note that each variable now has the same count. Only rows with all of the information are included. This isn't necessarily best practices when it comes to data. You want to know why your data are missing. You can sometimes fill in the missing data using a variety of methods, as well. 
# 
# We can also use the basic `pd.crosstabs` function from `pandas` to look at variables across our categorical data.
# 

# In[10]:


pd.crosstab(loans['loan_status'], loans['home_ownership'])


# We can **normalize** these counts as well, either over all values, by row, or by column. 

# In[11]:


pd.crosstab(loans['loan_status'], loans['home_ownership'], normalize = 'all')


# This tells us that about 6% of our sample are renters who defaulted. We can try normalizing by column, too.

# In[12]:


pd.crosstab(loans['loan_status'], loans['home_ownership'], normalize = 'columns')


# Now, each column adds up to 1. 11.9% of all renters in the sample defaulted. 
# 
# Finally, we can look at the **margins**. These add up values by row and column. 

# In[13]:


pd.crosstab(loans['loan_status'], loans['home_ownership'], normalize = 'all', margins = True)


# So, 10.9% of the full sample defaulted on their loans. About 51% are the full sample are renters. And, about 6% of renters defaulted. 
# 
# You can play around with the options to get the counts or percents that you want.

# ## Linear regression with a binary outcome
# 
# Now, let's run a regular linear regression to see what the relationship between loan status (default = 1) and annual income is. 

# In[14]:


results_ols = smf.ols("loan_status ~ annual_inc", data=loans).fit()
print(results_ols.summary())


# In[15]:


fig, ax = plt.subplots()
ax.scatter(loans["annual_inc"], loans["loan_status"])
sm.graphics.abline_plot(model_results=results_ols, ax=ax, color="red", label="OLS", alpha=0.5, ls="--")
ax.legend()
ax.set_xlabel("annual_inc")
ax.set_ylabel("loan_status")
ax.set_ylim(0, None)
plt.show()


# Well, that sure looks strange! Linear regression shows loan status going negative!
# 
# Let's do the same thing with `seaborn`. It's very easy to add a regression line, like you would in Excel. 

# In[16]:


sns.regplot(x="annual_inc", y="loan_status", data=loans);


# Yeah, that really doesn't make sense. `seaborn` lets us also add the fit from a logistic regression, though. 

# In[17]:


sns.regplot(x="annual_inc", y="loan_status", data=loans, logistic=True, y_jitter=.03)
plt.ylabel("Probability of default");


# OK, that still looks a bit strange, but at least loan status is never below 0!

# ### Categorical variables, again
# 
# We'll add the other variables to the regression, for completeness. To do this, though, I'm going to take my categorical variables and create new **dummy/indicator variables**. This will take the categories and create new columns. These new columns will take the value of 1 or 0, depending on whether or not that observation is in that category.
# 
# I'll use [pd.get_dummies](https://www.sharpsightlabs.com/blog/pandas-get-dummies/) to do this. I then concatenate, or combine, this new set of indicator variables to my original data. The `prefix=` helps me name the new variables.
# 

# In[18]:


loans= pd.concat((loans, pd.get_dummies(loans['grade'], prefix='loan_grade')), axis = 1)
loans= pd.concat((loans, pd.get_dummies(loans['home_ownership'], prefix='home')), axis = 1)


# You don't have to create the numeric indicator variables for the regression models. However, when dealing with indicators, you need to drop one of them from the model. For example, for home ownership, you can't include *home_mortgage*, *home_rent*, *home_own*, and *home_other*. You always have to drop one category, or the regression won't work. This is because the four variables together are [perfectly multicollinear](https://www.dummies.com/article/business-careers-money/business/economics/perfect-multicollinearity-and-your-econometric-model-156469/).  
# 
# I find it easier sometimes to manipulate the model when I have a distinct indicator variable for my categorical variables. You can also use the `treatment=` option when specifying a variable as categorical directly in the model.
# 
# For example, let me run the OLS model with *home_ownership* included as a categorical variable. 

# In[19]:


results_ols = smf.ols("loan_status ~ annual_inc + home_ownership", data=loans).fit()
print(results_ols.summary())


# That worked just fine. But, notice how *home_ownership[T.Mortgage]* is missing? The model automatically dropped it. So, the other *home_ownership* values are relative to having a mortgage. This may be just fine, of course! We can interpret the coefficient for renting, for example, as meaning that renters are more likely to default than those that have a mortgage. 
# 
# Here, I'll use my indicator variables and run a fully-specified model.

# In[20]:


loans.info()


# I will exclude the top rated A loan indicator and the indicator for renting. Therefore, the other indicator variables will be relative to the excluded one.

# In[21]:


results_ols = smf.ols("loan_status ~ loan_amnt + int_rate + emp_length + annual_inc + age + loan_grade_B + loan_grade_C + loan_grade_D + loan_grade_E + loan_grade_F + loan_grade_G + home_MORTGAGE + home_OWN + home_OTHER", data=loans).fit()
print(results_ols.summary())


# The interpretation of the signs on the coefficients is relatively straightforward. Larger credit card loans are less likely to default. Why? Lending is **endogenous** - it is chosen by the credit card company. They are more likely to allow larger balances for people less likely to default, all other things equal. Similarily, higher interest rates are related to more defaults. Larger annual incomes are associated with a smaller default rate. Lower loan grades, relative to A, are associated with more defaults. Finally, mortgage vs. renting doesn't seem to be that different, once you include all of these other variables.

# ## Logit models
# 
# OK, so let's look at a [logit model](https://www.andrewvillazon.com/logistic-regression-python-statsmodels/#fitting-a-logistic-regression). We can look at the signs of the coefficients from the OLS model, but we can't really interpret much else. Those coefficients are not probabilities. 
# 
# The true probability of defaulting must fall between 0 and 1. A **logit function**, show below, will satisfy this requirement. 
# 
# \begin{align}
# {\displaystyle \mathbb{P}(Y=1\mid X) = \frac{1}{1 + e^{-X'\beta}}}
# \end{align}
# 
# The left-hand side is the probability that Y = 1, or, in our case, that a loan is in default, **conditional** on the X variables, or the variables that we are using to predict loan status. The right-hand side is the function that **links** our X variables to the probability that Y = 1.
# 
# We will use `smf.logit` to estimate our logit model. This is an example of using a **generalized linear model (GLM)**, a class of models that includes logistic regression. You will also see logits described as **binomial** model. 
# 
# In the background, GLM uses **maximum likelihood** to fit the model. The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: 
# 
# We seek estimates for $\beta_0$ an $\beta_1$ that get us a predicted probability of default for each individual, $p(x_i)$, that corresponds as closely as possible to the individual’s actual observed default status. In other words, we plug in beta estimates until we get numbers "close" to 1 for those that default and "close" to zero for those that do not. This is done using what is called a **liklihood function**.
# 
# Ordinary least squares regression (OLS) actually works in a similar manner, where betas are chosen to minimize the sum of squared residuals (errors).
# 
# Essentially, we pick a model that we think can explain our data. This could be OLS, logit, or something else. Then, we find the parameters to plug into that model that give us the best possible predicted values based on minimizing some kind of error function.
# 
# Let's look at a logit with a discrete variable and a continuous X variable separately, in order to better understand how to interpret the output. 

# ### Logit with a discrete variable
# 
# We can start simply, again. This time, I'm going to just use the indicator for whether or not the person rents.

# In[22]:


results_logit = smf.logit("loan_status ~ home_RENT", data = loans).fit()
print(results_logit.summary())


# We didn't include renting in the linear model above, as it was the omitted indicator. But, here we can see that renting is associated with higher probability of default **relative to all of the other possibilities** and when not including any other variables in the model. 
# 
# Also note that we don't have *t*-statistics. With logit, you can *z*-scores. You can look at the p-values to see how you should interpret the score. The hypothesis is the same as in linear regression: can we reject the null hypothesis that this coefficient is zero?
# 
# The output from the logit regression is still hard to interpret, though. What does the coefficient on home_RENT of 0.2114 mean? This is a **log odds ratio**. Let's convert this to an **odds ratio**, which is easier to think about.
# 
# An odds ratio is defined as: 
# 
# \begin{align}
# {\displaystyle \text{odds(success)} = \frac{p}{1-p}}
# \end{align}
# 
# 
# where p = probability of the event happening. So, an 80% chance of happening = .8/.2 = 4:1 odds. 1:1 odds is a 50/50 chance. The logit model gives us the log of this number. So, we can use the inverse of the log, the natural number e, to "undo" the log and get us the odds.

# In[23]:


odds_ratios = pd.DataFrame(
    {
        "OR": results_logit.params,
        "Lower CI": results_logit.conf_int()[0],
        "Upper CI": results_logit.conf_int()[1],
    }
)
odds_ratios = np.exp(odds_ratios)
print(odds_ratios)


# What do these numbers mean? If someone rents, this increases the odds of default by about 1.24 versus all other options.
# 
# For more about interpreting odds, see [here](https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-how-do-i-interpret-odds-ratios-in-logistic-regression/).

# Odds ratios are **not probabilities**. Let's calculate the change in the probability of default as you from 0 to 1 for home_ownership_RENT. The [.get_margeff](https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.DiscreteResults.get_margeff.html) function finds **marginal effects** and let's us move from odds ratios to probabilities.
# 
# Things get a bit complicated here. We have to find the marginal effect **at some point**, like the mean of the variable. This is like in economics, when you find [price elasticity](https://en.wikipedia.org/wiki/Price_elasticity_of_demand). I'm specifying that I have a dummy variable that I want to change and that I want the proportional change in *loan_status* for a change in *home_RENT*. This is the `eydx` specification.

# In[24]:


p_marg_effect = results_logit.get_margeff(at='mean', method="eydx", dummy=True)
p_marg_effect.summary()


# You can interpret this as "going from not renting to renting is associated with an 18.84% increase *loan_status*." You can also specify `dydx`, which is the default.

# In[25]:


p_marg_effect = results_logit.get_margeff(at='mean', method="dydx", dummy=True)
p_marg_effect.summary()


# You can interpret this as "going from not renting to renting is associated with an 0.0205 increase in *loan_status* from the mean of *loan_status*."

# ### Logit with a continuous variable
# 
# We can also look at a continuous variable, like annual income.

# In[26]:


results_logit = smf.logit("loan_status ~ annual_inc", data = loans).fit()
print(results_logit.summary())


# Let's find our odds ratio for annual income. However, if we do that math exactly like above, we'll find the incremental odds change for a dollar more in annual income. That's going to be small! However, it is easy to change the increment for our continuous variable. 

# In[27]:


increment = 10000

odds_ratios = pd.DataFrame(
    {
        "OR": results_logit.params * increment,
        "Lower CI": results_logit.conf_int()[0]* increment,
        "Upper CI": results_logit.conf_int()[1]* increment,
    }
)
odds_ratios = np.exp(odds_ratios)
print(odds_ratios)


# We can read this number as "Increasing income by $10,000 reduces the odds of default by 1-0.948, or 0.052 (5.2%)."
# 
# We can also do marginal probabilities. I'll use the `eyex` method which tells us: If annual income increases by 1% from the mean value, what is the percentage change in the probability of default?

# In[28]:


p_marg_effect = results_logit.get_margeff(at='mean', method="eyex")
p_marg_effect.summary()


# If annual income, starting at the mean value, increases by 1%, then the probability of default drops by 0.32%. 

# ### Combining variables in a logit
# 
# Let's look at both annual income and renting together. It's good to get a feel for how to deal with both discrete and continuous variables.
# 
# I'm going to use the `C` categorical method and specify the "treatment", or omitted, indicator. This is instead of using my dummy variables that I created above. I just want to show you the different ways of doing the same thing.

# In[29]:


results_logit = smf.logit("loan_status ~ loan_amnt + int_rate + emp_length + annual_inc + age + C(home_ownership, Treatment('MORTGAGE')) + C(grade, Treatment('A'))", data = loans).fit()
print(results_logit.summary())


# Interpretation is similar. With all of the other variables included, renting doesn't seem to matter much for the probability of default vs. having a mortgage, since that coefficient is not significant. Remember, having a mortgage is the omitted indicator, so everything is relative to that. Notice how as you move down in loan grade that the probability of default increases, relative to being in the top category, "A", which was the omitted indicator. Annual income is again very significant and negative.

# In[30]:


p_marg_effect = results_logit.get_margeff(at='overall', method="dydx")
p_marg_effect.summary()

