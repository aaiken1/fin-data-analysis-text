#!/usr/bin/env python
# coding: utf-8

# # The Basics
# 
# This section covers some ideas that I call **CompSci 101**. These are the sorts of topics that come up in any Intro to Computer Science class. Let's cover the basics, so that we can have some idea of what's going on with our data. 
# 
# I can't let you get out of this course without seeing some of this stuff. I'd feel bad. 
# 
# 
# ```{note}
# I am borrowing heavily from [Chapter 1 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter1-basics.html) and [Chapter 3 of Python for Finance, 2e](https://www.oreilly.com/library/view/python-for-finance/9781492024323/).
# ```
# 
# The table below highlights important items that you should look for as you read our text. Also, the author quickly starts to use basic control structures, like `if`, `then`, and `while`. We'll discuss these in more detail, but he does a good job of going line-by-line and demonstrating the logic. Follow along with the examples.
# 
# There are additional resources on Datacamp, as well. Here is a [DataCamp tutorial on Python data structures](https://www.datacamp.com/community/tutorials/data-structures-python) and here is a [DataCamp tutorial on Python strings](https://www.datacamp.com/community/tutorials/python-string-tutorial), or dealing with text. 
# 
# [Chapter 3 of Python for Data Analysis, 3E](https://wesmckinney.com/book/python-builtin.html) also covers data structures and functions.
# 
# You can find more on the basics of Python in the [Python tutorial](https://docs.python.org/3/tutorial/introduction.html).
# 
# Lists, dictionaries, and tuples are also covered in detail in the [Python tutorial](https://docs.python.org/3/tutorial/datastructures.html). 
# 
# Do not feel like you need to look at this stuff and understand everything all at once. The key is to **know that these ideas and tools exist**, try them, get an error message, and iterate. 
# 
# 
# ```{margin}
# ```{tip}
# Want to really learn how computers work? Checkout [Code by Charles Petzold](http://www.charlespetzold.com/code/). It is over 20 years old now, but the basics haven't changed.
# ``````
# 

# ## Data types
# 
# Computers think of data, or a **value**, as a **type**. For example, in Python, there are three types of numbers: integers, floats, and complex. A **variable** is a name that refers to a value. Python let's you create any variable name as long as it begins with a letter or an underscore, so no numbers to start. It should also not be what is called a r[eserved word](https://docs.python.org/3.3/reference/lexical_analysis.html#keywords) in Python such as `for`, `while`, or `class`. All programming languages have special, reserved words that they don't want us using as variable names. It would get confused.
# 
# A common metaphor is to think of a variable as a box that holds some information (like a number, a vector, or a string). We use the **assignment operator** `=` to assign a value to a variable.

# ### Common built-in Python data types and structures
# 
# | English name          | Type name  | Type Category  | Description                                   | Example                                    |
# | :-------------------- | :--------- | :------------- | :-------------------------------------------- | :----------------------------------------- |
# | integer               | `int`      | Numeric Type   | positive/negative whole numbers               | `42`                                       |
# | floating point number | `float`    | Numeric Type   | real number in decimal form                   | `3.14159`                                  |
# | boolean               | `bool`     | Boolean Values | true or false                                 | `True`                                     |
# | string                | `str`      | Sequence Type  | text                                          | `"I Can Has Cheezburger?"`                 |
# | list                  | `list`     | Sequence Type  | a collection of objects - mutable & ordered   | `['Ali', 'Xinyi', 'Miriam']`               |
# | tuple                 | `tuple`    | Sequence Type  | a collection of objects - immutable & ordered | `('Thursday', 6, 9, 2018)`                 |
# | dictionary            | `dict`     | Mapping Type   | mapping of key-value pairs                    | `{'name':'DSCI', 'code':511, 'credits':2}` |
# | none                  | `NoneType` | Null Object    | represents no value                           | `None`          
# 
# Source: [Chapter 1 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter1-basics.html)

# ### Arithmetic operators
# 
# You can do all of the arithmetic that you'd expect.
# 
# | Operator |   Description    |
# | :------: | :--------------: |
# |   `+`    |     addition     |
# |   `-`    |   subtraction    |
# |   `*`    |  multiplication  |
# |   `/`    |     division     |
# |   `**`   |  exponentiation  |
# |   `//`   | integer division / floor division |
# |   `%`    |      modulo      |
# 
# Source: [Chapter 1 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter1-basics.html)

# ### Integers
# 
# We can assign the value 10 to the variable `a` using `=`. We can then use the `type` function to see what data type `a` is. 

# In[1]:


a = 10
type(a)


# Python can be used as a calculator.

# In[2]:


1 / 4


# In[3]:


type(1/4)


# By the way, we just created our first **variable**, `a`.  Variable names even have [rules](https://www.w3schools.com/python/python_variables_names.asp) associated with them. 

# ### Floats

# Floats are the other way Python stores numbers. The book goes into more detail about the way computers represent numbers internally, but just know that you may sometimes need to be aware of **precision**. See below.

# In[4]:


b = 0.35
type(b)


# In[5]:


b + 0.1


# I guess that's close, right? By the way, run cell [7] before cell [6] and get an error. Why? The variable `b` hasn't been defined if you haven't run cell 6. Also, click on **Jupyter: Variables** below. You'll see the types and values for `a` and `b.` 
# 
# You can click **restart** above to clear all of the variables out of memory. 

# Also, operations may change one type to another. For example, an `int` into a `float`. Floor division will round down and retain the `int` type.

# In[6]:


type(2 / 2)


# In[7]:


type(2 // 2)


# The **Modulo** operator gives the remainder.

# In[8]:


5 % 2


# ### Booleans
# 
# Booleans are `True` or `False`. We'll see **relational operators**, like `>`, `<`, `==`, `<=`, `>=`, and `!=`. We can also use `and`, `or`, and `not`. These are all **keywords**, which means that we can't use them as variable names. 
# 
# We can compare objects using comparison operators, and we'll get back a Boolean result:
# 
# | Operator  | Description                          |
# | :-------- | :----------------------------------- |
# | `x == y ` | is `x` equal to `y`?                 |
# | `x != y`  | is `x` not equal to `y`?             |
# | `x > y`   | is `x` greater than `y`?             |
# | `x >= y`  | is `x` greater than or equal to `y`? |
# | `x < y`   | is `x` less than `y`?                |
# | `x <= y`  | is `x` less than or equal to `y`?    |
# | `x is y`  | is `x` the same object as `y`?       |
# 
# **Boolean operators** also evaluate to either `True` or `False`:
# 
# | Operator | Description |
# | :---: | :--- |
# |`x and y`| are `x` and `y` both True? |
# |`x or y` | is at least one of `x` and `y` True? |
# | `not x` | is `x` False? | 
# 
# Source: [Chapter 1 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter1-basics.html)
# 

# In[9]:


42 > 23


# In[10]:


42 >= 42


# In[11]:


42 == 42


# In[12]:


# Nope! Need to use ==. 
# 42 = 42


# In[13]:


# Common way to say "not equal"
42 != 42


# In[14]:


# Can make compound statements too. See why this is true?

(4 == 3) or (2 != 3)


# This is also a good time to point out that Python is **case sensitive**. 

# In[15]:


x = 23
X = 42

print(x)


# In[16]:


print(X)


# In[17]:


# Nope!
# Print(x)


# ### Strings
# 
# Strings are **text**. We could spend half this semester or more just dealing with text, [regular expressions](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial), [natural language programming](https://www.datacamp.com/tracks/natural-language-processing-in-python) (NLP). To start, though, we need to know that strings are a basic and essential data type across all programming languages.
# 
# You can use either `'` or `"` around text. This is helpful when the string has a `'` in it.

# In[18]:


# Define our string. Check the Jupyter:Variables in your VS Code! Note the size.
txt = 'elon university'
print(txt)


# In[19]:


txt2 = "Prof Aiken's Class"
print(txt2)


# There are many different string methods. Being able to deal with text is a crucial part of data wrangling, or cleaning. And, text is usually part of what people refer to as [unstructered data](https://en.wikipedia.org/wiki/Unstructured_data). For example, could you write code to [read 10K filings](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3576098)? Yes! How about using the [news to predict stock returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2944826)? Maybe! Lots of people are trying.

# In[20]:


txt.capitalize()


# In[21]:


txt.split()


# In[22]:


txt.replace(' ', '******')


# ### Casting
# 
# Sometimes we need to explicitly **cast** a value from one type to another. We can do this using functions like `str()`, `int()`, and `float()`. Python tries to do the conversion, or throws an error if it can't.

# ## Data structures
# 
# Our book differentiates between data types and data structures. Of the basic data structures, I think we'll deal with **lists** the most. We'll see arrays and data frames in the next few chapters. We'll use those two and their associated methods all of the time.

# ### Lists 
# Lists allow us to store multiple things ("elements") in a single object. The elements are **ordered**. We'll start with lists. Lists are defined with square brackets `[]`.
# 
# They can both hold different data types. They can even hold other lists.

# In[23]:


my_list = [1, 2, "THREE", 4, "Elon"]


# In[24]:


my_list


# In[25]:


type(my_list)


# We can `append` something to a list, like another list. We can also `extend`, `insert`, and `remove` items.

# In[26]:


my_list.append([4, 3])  
my_list


# In[27]:


my_list.extend([1.0, 1.5, 2.0])  
my_list


# In[28]:


my_list.insert(1, 'insert')  
my_list


# In[29]:


my_list.remove('THREE')  
my_list


# In[30]:


len(my_list)


# We can access values inside a list, tuple, or string using square bracket syntax. Python uses **zero-based indexing**, which means the first element of the list is in position 0, not position 1.
# 

# In[31]:


my_list[0]


# We can use a `:` to **slice** a list. Note that the start of the slice is inclusive and the end is exclusive. So, you start counting at 0... 0, 1, 2 and you get 2. Then, keep going... 3, 4, 5. The 5th element of the list is another list [4,3]. So, the 4th Element, the string "Elon", is the last element sliced.

# In[32]:


my_list[2:5]  


# We can use negative indices to count backwards from the end of the list.

# In[33]:


my_list[-1]


# ### Dictionaries, sets, and tuples
# 
# These are three other data types that we won't use as much, but they do appear in the DataCamp assignments. 
# 
# Python **dictionaries** are key:value pairs. They associate a key with a value, in other words. You can change them and they do not allow you to have duplicate entries. You can create one using brackets, like this:

# In[34]:


d = {
     'Name' : 'Adam Aiken',
     'University' : 'Elon University',
     'Department' : 'Finance',
     'PhD Program' : 'Arizona State'
     }
type(d)


# You can then print items from the dictionary, as well as show the keys and the values. 

# In[35]:


print(d['Name'], d['University'])


# In[36]:


d.keys()


# In[37]:


d.values()


# In[38]:


d.items()


# Python **sets** let you store unordered values in a single variable. There's no relationship between the items and they are **unordered**. You also can't change them, though you can add and delete items.

# In[39]:


adam_set = {"Adam", "Aiken", "Elon", "Arizona State"}
print(adam_set)


# Finally, a Python **tuple** is like a set, except that the order does matter. You define these with `()`, instead of `{}`.

# In[40]:


adam_tuple = ("Adam", "Aiken", "Elon", "Arizona State")


# To summarize, we've seen **four** ways to store data in Python: lists, dictionaries, sets, and tuples. We'll use lists the most. But, we're going to need other ways. This is where we get to `numpy` arrays and `pandas` DataFrames.

# ## Syntax in Python
# Syntax, or the way you write your code, is really important. As mentioned `=` and `==` are not the same thing. Python is case sensitive, as we saw.
# 
# If you're coming from another programming language, you might have also noticed that you don't need a semi-colon `;` to end a line. However, you can use a `;` to separate different statements on the same line.
# 
# You'll see below that we end conditional statements with a `:`.
# 
# Most importantly, **we don't use brackets in Python** to tell our code what statements go with which control structure. Instead, we use **indentation**. Let me show you what I mean.
# 

# ## Control structures

# **Control structures** allow you to determine the flow of your code. We'll start with **conditional statements**. [Conditional statements](https://www.datacamp.com/community/tutorials/elif-statements-python) make it so that only certain blocks of code will run (i.e. get executed), depending, or **conditional**, on the state of the code at that time (i.e. what is true). This is where `if`, `elif`, and `else` come in. You've probably used something like this in Excel.
# 
# We will also see two types of **loops**. You can create [a loop using `for`](https://www.datacamp.com/community/tutorials/for-loop-python) that will run the code included in the loop only for values contained in a list. There are also [`while` loops](https://www.datacamp.com/community/tutorials/loops-python-tutorial), where the loop will run until a certain criteria, specified by the code, is met. There are subtle differences between the two. `While` loops need to check boolean conditions to see if a condition is `True` or `False` in order to keep going. `For` loops go until the end range is reached. This makes `for` loops faster than `while` loops -- the Python compiler doesn't have to work as hard. 
# 
# In general, loops can slow down your code. **Functional programming** can speed things up. The book mentions this. We will get to it later.
# 
# You can find more on control structures in the [Python tutorial](https://docs.python.org/3/tutorial/controlflow.html).
# 
# Let's start with conditional statements and the humble `if`.
# 
# **Conditional statements** introduce *if/then/else-style* logic. The main points to notice:
# - Use keywords `if`, `elif` and `else`
# - As with `for` and `while`, a colon `:` ends each conditional expression
# - Indentation (by 4 empty space) defines code blocks. **Very important!**
# - In an `if` statement, the first block whose conditional statement returns `True` is executed and the program exits the `if` block
# - `if` statements don't necessarily need `elif` or `else`
# - `elif` lets us check several conditions
# - `else` lets us evaluate a default block if all other conditions are `False`
# - the end of the entire `if` statement is where the indentation returns to the same level as the first `if` keyword
# 
# Let's check if some numbers are even or odd. The modulo operator `%` gives us the remainder from division. We'll check and see if 7 is even or odd.

# In[41]:


i = 7

if i % 2 == 0:
    print("%d is even" % i)
else:
    print("%d is odd" % i)


# This the basic set-up for if/else. Note the format - you need those `:` and the indentation. Check out the text for string replacement to see what the `print("%d is even" % i)` code is doing. In short, the code is substituting `i` into the string for `%d`. Our text does this all of the time. Also note how there is no condition after the `else`. You do this when the logic above is `false`. 
# 
# 
# ```{note}
# When creating more complicated control structures, I suggest going step-by-step on a piece of paper. What does the computer "know" at any point in the sequence? What are the values of your variables? What will it do? Does it do what you expect it to do?
# ```

# Let's turn to **loops**. We'll also put some `if`, `elif`, and `else` logic inside of a loop.
# 
# 
# ```{figure} ../images/03-loop.png
# ---
# name: 03-loop.png
# align: center
# ---
# The difference between a `for` loop and a `while` loop. They do very similar things, but the logic is different. Try to follow the logic of each.
# ```
# 
# Each line of code has some logic. For example, we are using `for element in num_list[0:3]:` below in our first example. Let's parse that:
# 
# - `for` means that Python is going to work across a certain number of elements from something, like a `list`. 
# - `element` is going to represent an item from the `list`, like a single integer. But, it doesn't have to be an integer.
# - `num_list` is our list. In this case, we are `slicing` to only use three elements: 0, 1, and 2. Remember, slicing is inclusive of the first element and exclusive of the last.
# - We then end the line of logic with a `:`. This is **really important**. `for`, `while`, `if`, `elif`, and `else` all need to end with a `:`. 
# - **Indentation matters in Python**. To do the indentation, you want to hit **tab**. The indentation tells Python which lines of code go with which lines of logic. See our examples below and in the text. 
# 
# ```{note}
# You can find more on loops and functions in [Chapter 2 of Python Programming for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter2-loops-functions.html).
# ```

# In[42]:


num_list = [1,2,3,4,5]
num_list


# Here's a basic `for` loop. Note the indexing on the list. It starts at the 0th element (the 1st item) and goes up to the 3rd element (the 4th item), but doesn't include it, and stops.

# In[43]:


for element in num_list[0:3]:
    print(element ** 2)


# Each item in the list gets put into the variable *element*. That number is then squared and printed. The `for` loop then moves on to the next item in the list. The loop will **exit** when the last item in the list is reached.
# 
# As noted above, you can use `elif` to test multiple conditions. This example, from Chapter 3 of [Python for Finance, 2e](https://www.oreilly.com/library/view/python-for-finance/9781492024323/), uses a `range` function to create the numbers 1 through 9 (not 10 though!) and then test two conditions and ending with the `else`. The `range` acts like a loop that we have now combined with if/else statements.
# 

# In[44]:


for i in range(1, 10):
    if i % 2 == 0:  
        print("%d is even" % i)
    elif i % 3 == 0:
        print("%d is multiple of 3" % i)
    else:
        print("%d is odd" % i)


# Again, note the `:` to end each line **control structure**, as well as the four-space indentation. Try deleting the indentation before the first `if` and running this code. What happens?
# 
# `for` loops are one type of look. We can also use `while` loops. These are slightly different in their logic -- check out the graphic above.
# 
# Here's a simple example of a `while` loop.

# In[45]:


i = 0 
while i < 4:
    print(i)
    i += 1


# The variable *i* starts at 0, gets printed, and then has 1 added to it. The loop then returns to the top and is evaluated again. The loop will **exit** when i = 4. 

# 
# Let's look at a while loop and some if-else logic together. We again see the use of the `print` function. I am taking the integer number and **casting** it as a string to be included in the `print` output. The `+` operator with strings means [concatenation in Python](https://www.freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable/).

# In[46]:


# Take user input
number = 2 

# Condition of the while loop
while number < 5:  
    # Find the mod of 2
    if number%2 == 0:  
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")
    # Increment `number` by 1
    number = number + 1


# I will again point out the `:` and the indentation. If you're control structures are getting your error messages, those are the first two things to check.

# ## Functions and functional programming
# 
# I just want to introduce the idea of functions and **functional programming**. You can, of course, write your own functions in Python. Functions take input and give you an output.
# 
# See the example below for the basic syntax. You **call** the function with `function()`. In the example, I define a function `square` that takes an argument, or input, `x` and raises it to the power of 2. 
# 
# Always pick a good name for you functions!
# 
# 
# ```{note}
# This is just a first look at writing functions. We'll do more later.
# ```
# 
# Like with control structures we have a `:` after the first line defining the function. We then have ** four-space indentation** to indicate what code is part of the function.
# 
# You can again find more at this [DataCamp tutorial](https://www.datacamp.com/community/tutorials/functions-python-tutorial).
# 

# In[47]:


def square(x):
    return x ** 2
square(2)


# We can also print the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) up to some term `n`, which can be an input into your function.

# In[48]:


def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)


# [Functional programming](https://realpython.com/python-functional-programming/) is a way of telling the computer what to do in an efficient manner. This is the world of **lambda functions**, and `map()`, `filter()`, `reduce()`. 
# 
# [Excel can even use lambda functions now](https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67).

# ## Printing and formatting
# 
# We've used the `print` function a few times now. Something like this:

# In[49]:


i = 3
print("%d is odd" % i)


# This code is printing text inside of the quotes. The `%` is a placeholder for a variable. What variable? The one that comes after the `%` inside of the `print` function. In this case, that variable is called *i*.
# 
# What is the `d` doing next to the `%`? This is **not** a variable. This is telling Python how to **format** the variable inside of the string. `d` stands for **integer**. We can also format numbers as **floats** and specify decimal places. For example, 

# In[50]:


i = 42.23456
print("%.2f is a float" % i)


# The [Python tutorial](https://docs.python.org/3/tutorial/inputoutput.html) has much more on how to format output. 
