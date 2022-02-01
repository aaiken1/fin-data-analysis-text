#!/usr/bin/env python
# coding: utf-8

# # Numpy and arrays
# 
# It is time for our first Python library! **Chapter 4** of our text covers the [NumPy](https://numpy.org) library and `arrays`. Arrays can hold many different values, which you then reference or perform operations on. For example, a **matrix** is a two-dimensional array of numbers. However, arrays themselves can have any number *n* dimensions. 
# 
# Why do we need arrays? Math stuff. Linear algebra. They allow us to perform mathematical operations on numbers, like stock prices and returns. Arrays are also necessary for machine learning, image recognition, and anything else that requires computation. In short, you really can't do much with arrays and matrices.
# 
# ```{note}
# We are covering the basics of Chapter 4. I am also borrowing heavily from [Chapter 5 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter5-numpy.html) and [Chapter 4 of Python for Data Analysis](https://wesmckinney.com/book/numpy-basics.html)
# ```
# 
# You may have already seen [arrays in Excel](https://support.microsoft.com/en-us/office/guidelines-and-examples-of-array-formulas-7d94a64e-3ff3-4686-9372-ecfd5caa57c7)!
# 
# Check out this [DataCamp tutorial on arrays in Python](https://www.datacamp.com/community/tutorials/python-arrays) for more. 
# 
# ```{margin} Our textbook calls this numerical computing.
# Numerical computing and numerical methods are an entire field of computer science and mathematics. And the whole world is basically linear algebra.
# ```
# 
# This set of [notes from W3](https://www.w3schools.com/python/numpy/default.asp) is also a good resource.
# 
# 
# ## Chapter Four Highlights
# 
# | Topic         | Pages  |
# | :-------------------------------------------------------------------------------------- | :--------- | 
# | **Numpy arrays basics**. Lists and arrays are built-in to Python, but we really want **numpy arrays**. This section covers basic math with them.           | 90 - 97   | 
# | **Reshaping and resizing**. Arrays have dimensions, like n x k. How can we change their shape? | 97 - 101    | 
# | **Vectorization**. We saw loops in the last chapter. They can be slow. **Vectorization** is a way of doing loop-like things, but without the speed penalty. We will also talk a bit about **broadcasting**. | 106 - 110   | 

# NumPy stands for **Numerical Python** and is a crucial package for data work in Python. The `numpy` array object is used in essentially all data work, so we need to understand their propoerties and how to manipulate them. Arrays are “n-dimensional” data structures that can contain all the basic Python data types, e.g., floats, integers, strings, etc. However, we are going to use them mainly for **numerical data**. NumPy arrays (“ndarrays”) are homogenous, which means that items in the array should be of the same type - no mixing of integers and strings, for example.
# 
# ```{figure} ../images/03-numpy_arrays.png
# ---
# name: 03-numpy_arrays.png
# align: center
# ---
# A graphical representation of arrays. You're probably most familiar with the two-dimensional version, a matrix. Source: [Chapter 5 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter5-numpy.html)
# ```
# 
# We need to import the `numpy` package in order to use `narrays`. Here's the syntax for bringing in a package to our code. We're going to type this at the start of basically all of our code. We are going to use the _np_ part to tell Python where to look for a function/method in the `numpy` package. This is important, as `numpy` contains functions like `min` or `max` that are also built-in the standard Python. If you just write `max(x)`, Python is going to wonder what `max` you mean!

# In[1]:


import numpy as np


# ## Creating Arrays
# 
# We can create our own arrays using data we input ourselves.

# In[2]:


my_array = np.array([1, 2, 3, 4, 5])
type(my_array)


# We we talk about arrays, we talk about **dimensions**. A **vector** just has one dimension, _n_. A **matrix** has _n_ **rows** and _k_ **columns**. We write this as n $\times$ k. You can have an array with as many dimensions as you want. Vectors, matrices, cubes, _n_-dimensions, etc. 
# 
# In Python, we talk about the **axis** of an array. A 1-D array has only one axis, axis-0. A 2-D array, or matrix, has axis-0 (rows) and axis-1 (columns). See the graphic above.
# 
# We can also create random numbers. In VS Code, can hold your cursor over the `randn` part of the function below to see what it is doing. In fact, you can do that on any of the code below! Even the `my_random_array` object being created by the code.

# In[3]:


my_random_array = np.random.randn(2, 3)
my_random_array


# Notice the `[` and `]`. Each row gets its own set of brackets, while the entire array is also in brackets.
# 
# There are also many built-in methods for creating specific array types.

# In[4]:


np.arange(1, 5)  # from 1 inclusive to 5 exclusive


# In[5]:


np.arange(0, 11, 2)  # step by 2 from 1 to 11


# In[6]:


np.linspace(0, 10, 5)  # 5 equally spaced points between 0 and 10


# In[7]:


np.ones((2, 2))  # an array of ones with size 2 x 2


# Any many others. See Chapter 5 of Python for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter5-numpy.html).
# 
# `numpy` has several functions for looking at the **shapes** of our arrays. Let's create another matrix of random numbers from the [standard normal distribution](https://online.stat.psu.edu/stat500/lesson/3/3.3/3.3.2). We will then use `.ndim()`, `.shape()`, and `.size()`. 

# In[8]:


x = np.random.randn(10, 5)
x


# In[9]:


x.ndim


# There are two dimensions, axis-0 and axis-1, rows and columns.

# In[10]:


x.shape


# 10 elements along axis-0 and 5 along axis-1. For a 2-D array, this corresponds to rows and columns.

# In[11]:


x.size


# There are 10 * 5 = 50 total elements in that array.

# ## Array Math
# 
# We'll start with **element-by-element** operations. You've likely seen these in a math class somewhere. We'll start by creating a 1-D array of ones. You'd be surprised how often you just need a bunch of ones in linear algebra!

# In[12]:


x = np.ones(4)
x


# In[13]:


y = x + 1
y


# In[14]:


x - y


# Those both make sense. You're simply adding or subtracting an element from one with the corresponding element from the other. How about multiplication (*), raising to an exponent (**), and division? Same thing!

# In[15]:


x * y


# In[16]:


x ** y


# In[17]:


x / y


# ## Reshaping and Resizing

# You can also **reshape** your arrays. This means rearranging the different axis. Let's create 1-D array with 8 elements to play with. We can again see the shape attribute with `.shape()`.

# In[18]:


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x.shape 


# Let's use `.reshape()` to change the dimensions of this array. `.reshape()` lets you go from, say, 1-D to 2-D, using the same data. We'll a 2 $\times$ 4 2-D array.

# In[19]:


x.reshape(2,4)


# Note that the resulting array needs to have the same number of elements, so 2 * 4 = 8. 
# 
# If you've taken a math class that deals with matrices, then you've seen **transposition**.
# 
# Let's create an array of random numbers between 0 and 1 using `.rand()`, different from `.randn()`, that is a 5 $\times$ 2 matrix. Then, we'll `.transpose()` the array object. This means that we will flip the rows and columns, such that the first row becomes the first column, the second row becomes the second column, and so on. This will result in a 2 $\times$ 5 matrix.

# In[20]:


x = np.random.rand(5, 2)
x


# 5 rows and 2 columns. OK, let's transpose this. We'll use the `.transpose()` function.

# In[21]:


x.transpose()


# Now we have 2 rows and 5 columns. 
# 
# See how reshape and transpose are doing different things? We can reshape a 2-D array to make this clearer. How about going from 6 $\times$ 2 to 3 $\times$ 4? That requires a `.reshape()`. If we instead use `.transpose()`, we go from 6 $\times$ 2 to 2 $\times$ 6. No need to specify any rows or columns with transpose.

# In[22]:


x = np.random.rand(6, 2)
x


# In[23]:


x.reshape(3,4)


# In[24]:


x.transpose()


# Finally, let's look at `.resize()`. `.reshape()` had to have the same number of elements. `.resize()` does not. Let's create another random array.

# In[25]:


x = np.random.rand(6, 2)
x


# Let's pick out the first row and then just the first two columns from that.

# In[26]:


np.resize(x,(1,2))


# Or, how about we make this array bigger? This will add six rows, But, with what numbers? It just repeats the numbers from above to fill in the additional 12 items (6 rows and 2 columns). 

# In[27]:


np.resize(x,(12,2))


# Why do we need to do any of this? Matrix math sometimes requires our data to be in a certain shape.
# 
# But, wait... I just wrote my code differently. There's an `x` inside the `.resize()`, rather than just writing `x.resize()`! And, why are there parentheses around the dimensions? What's going on?

# ### An Aside: Functions, Methods and Objects
# 
# Let's look at two lines of code from above.

# In[28]:


x = np.random.rand(6, 2)
x


# This code is saying: Use the **function** `.rand()` from the collection of .`random()` functions found in the `numpy` package, which we have abbreviated as `np.`. This creates a new object called `x` that is a `narray`, or `numpy` array.
# 
# Objects are things. Like an array that stores our data. Objects come with **methods** that let us do things to them. They also come with **attributes** that let us learn more about them.
# 
# `x.shape()` gets the shape **attribute** of x.
# 
# `x.reshape()` calls the `.reshape()` **method** on object x. 
# 
# We'll do a bit more on this later, but I wanted to point out why the code sometimes has `np.`, sometimes has `x.`, and sometimes has `x = `. Note that you could use a method on an object and then save the result, even over the original object.

# In[29]:


x.reshape(3,4)


# I could have also written the code another way, which let's us see the `np.`. I am including `x` as an argument to my method. I then have to put `()` around my new dimensions. This creates a `tuple` for our dimensions.

# In[30]:


np.reshape(x, (3, 4))


# Why do it this way? It lets us use the `np.` pre-fix, which means that Python won't get confused. For example there's a `np.resize()` method and a regular `.resize()` method. You also need the `np.` pre-fix in order to be able to put your cursor over the code to get help in VS Code.
# 
# ```{note}
# Our textbook tends to write the code this way.
# ```

# In[31]:


x.resize(1, 2)


# See the error message? It is telling us to use the `np.resize()` function.

# In[226]:


np.resize(x, (1,2))


# Much better! 
# 
# You'll see code written a variety of ways when looking for help online or looking at different books. While this stuff can be confusing at first, it's helpful to kind of understand what's going on, so that you can see the subtle differences in syntax and why they matter.

# ## Indexing and Slicing
# 
# We've seen indexing and slicing already. Let's look at how we can pull a particular number, row, or column out of an array. Let's create a simple 1-D array to start, the numbers 0 - 9. Remember how Python starts indexing at 0?

# In[227]:


x = np.arange(10)
x


# We can then pull just pieces of that array. Note that we're using brackets and not parentheses now. Item 3 is the 4th number when you have zero indexing. 

# In[228]:


x[3] 


# In[229]:


x[2:] # Starting on the third item


# In[230]:


x[:3] # Up until the 4th item, exclusive.


# In[231]:


x[2:5] # Start on the third item, go up until the 6th item, exclusive. 


# In[232]:


x[-1] # Start counting backwards


# We do similar things for 2-D arrays. Let's create a 4 $\times$ 6 matrix out of random integers from 0 to 9 (0 to 10, exclusive).

# In[233]:


x = np.random.randint(10, size=(4, 6))
x


# We can then pick out the row $\times$ column that we want. Using [3,4] gets us the 4th row and the 5th column, since, again, we have zero indexing. We need to start just referring to these as the 3rd row and 4th column and assuming that we start at zero.

# In[234]:


x[3,4]


# We can pick out just the 3rd row:

# In[235]:


x[3]


# We can pick out just the 4th column using `:` and `,` together. This means choose all rows, just the 4th column.

# In[236]:


x[:,4]


# We can select multiple rows and columns, also using `:` and `,` together.

# In[237]:


x[0:2] # Choose the first two rows.


# How about the first two columns? The first `:` means "all rows". Then, we separate the rows and columns with `,`. Finally, we select the two columns with `0:2`.

# In[238]:


x[:,0:2]


# Finally, you can change a number in an array. 

# In[239]:


x[1,1] = 1000
x


# ##  Vectorization

# Vectorization let's us avoid slow, inefficient loops. Let's look at example. 

# In[240]:


array = np.array(range(1000000))
for i, element in enumerate(array):
    array[i] = element ** 2


# In[241]:


array = np.array(range(1000000))
array **= 2 


# The two code blocks above do the **exact same thing**. They create an array with 1,000,000 numbers, from 1 to 1,000,000. Then, the square each of these. The second code block is 4x faster though!
# 
# The first block is a `for` loop. For each element (number) in the array, that that element and square it.
# 
# The second block is *vectorized**. Python is doing everything at once, in a sense. The `**=` means take each number in the array and square it. It is a short-cut way to write the loop, but, even better than that, it is faster to run.
# 
# By the way, you'll see the "operation"= thing a lot in code. It means take the thing on the left-hand side, do the operation, in this case "**2", or square the number, and replace the original array with all of the squared terms. Here's another example:
# 

# In[242]:


x = 10
x += 1
x


# We can compare the two methods from above directly. We'll just do five numbers here, so that the comparison doesn't take forever.

# In[243]:


# loop method
array = np.array(range(5))
time_loop = get_ipython().run_line_magic('timeit', '-q -o -r 3 for i, element in enumerate(array): array[i] = element ** 2')
# vectorized method
array = np.array(range(5))
time_vec = get_ipython().run_line_magic('timeit', '-q -o -r 3 array ** 2')
print(f"Vectorized operation is {time_loop.average / time_vec.average:.2f}x faster than looping here.")


# ## Broadcasting

# We'll end with **broadcasting**. Arrays of different dimensions can't be directly used in arithmetic, element-by-element, operations. For example, let's create two arrays of different sizes and try adding them together.

# In[244]:


a = np.ones((2, 2))
b = np.ones((3, 3))
a + b


# We can't add a 2 $\times$ 2 matrix to a 3 $\times$ 3 matrix. It just doesn't work! So, we need some rules for doing element-by-element operations on our arrays.
# 
#  Let's create a 1-D array of prices for three different products: $10, $15, and $20. 1-D arrays can be confusing, as they can actually have [several different types of shapes](https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter5-numpy.html#d-arrays).

# In[245]:


price = np.array([10, 15, 20])
price


# Let's also create an array of quantity sold for the three products. They need to be in the same order as the prices above.

# In[246]:


sales = np.array([100, 150, 200])
sales


# We can multiply the two matrices together to get **total revenue by product**. 

# In[247]:


sales * price


# We can also do something called the [dot product](https://towardsdatascience.com/linear-algebra-basics-dot-product-and-matrix-multiplication-2a7624942810) using `np.dot()`. This takes the first element from price and multiplies it by the first element from sales and then adds this to the second item from price times the second item from sales, etc. This results in the **total revenue across all products**.

# In[248]:


np.dot(sales, price)


# OK, but what if we have three days of sales across the three products. Now, each row is a different product and each column is a different day.

# In[249]:


sales = np.array([[100, 120, 130], [150, 110, 125], [200, 150, 190]])
sales


# Let's look at our shapes for `price` and `sales`. 

# In[250]:


price.shape # A 1-D array, with 3 numbers along axis-0.


# In[251]:


sales.shape # A 3-D array, with 3 numbers along each axis.


# Let's just multiply these together and see what we get.

# In[252]:


price * sales


# This isn't right! Each row is a different product, so the first row is all the same item with the same price. Each number in the first row needs to be multiplied by 10. The second row by 15. And the third row by 20. 
# 
# We can use `.reshape()` to fix this. 

# In[253]:


price = price.reshape(3,1)
price


# See how the numbers are going up and down? OK, now let's `np.repeat()` price to get all 10's in the first row, etc. The syntax is saying to repeat each item three times across the first axis (the columns). 

# In[254]:


price = np.repeat(price, 3, axis = 1)
price


# Now, let's try multiplying.

# In[255]:


price * sales


# This looks good! But, there has to be an easier way, right? Yeah. Let'e set up our original prices again and reshape it, all in one step.

# In[256]:


price = np.array([10, 15, 20]).reshape(3,1)
price


# See how we can "chain" functions and methods together? This creates the object, uses a method, and saves it, all in one line. OK, now just multiply.

# In[257]:


price * sales


# Python is **broadcasting**, which means that it is doing that `.repeat()` for us to get the multiplication to work out. We now have the correct revenue for each product by day!
# 
# We'll go over [matrix multiplication in Python](https://www.datacamp.com/community/tutorials/python-scipy-tutorial#linear) more when we get to some portfolio mathematics and using [SciPy](https://www.datacamp.com/community/blog/python-scipy-cheat-sheet). 
