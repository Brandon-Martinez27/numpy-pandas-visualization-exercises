#!/usr/bin/env python
# coding: utf-8

# Use the following code for the questions below:
# 

# In[202]:


import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a


# 1. How many negative numbers are there?

# In[203]:


#array_variable[every element in array, operator, value].shape meaning how many data points there are
a[a < 0].shape


# In[204]:


(a < 0).sum()


# 2. How many positive numbers are there?

# In[205]:


a[a > 0].shape


# In[206]:


(a > 0).sum()


# 3. How many even positive numbers are there?

# In[207]:


a[(a > 0) & (a % 2 == 0)].shape


# In[208]:


((a > 0) & (a % 2 == 0)).sum()


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[209]:


a_plus_three = a + 3


# In[210]:


a_plus_three[(a_plus_three > 0) & (a_plus_three % 2 == 0)].shape


# In[211]:


((a_plus_three > 0) & (a_plus_three % 2 == 0)).sum()


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[212]:


# orginal array
a


# In[213]:


# original mean
a_mean = a.sum() / a.shape
a_mean


# In[214]:


# original st. dev.
a.std()


# In[215]:


# create squared version of array
a_squared = a**2


# In[216]:


# new mean
a_squared_mean = a_squared.sum() / a_squared.shape
a_squared_mean


# In[217]:


# new std. dev.
a_squared.std()


# 6. A common statistical operation on a dataset is **centering**. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

# In[218]:


a


# In[219]:


a_centered = a - a_mean
a_centered


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
#  $Z = \frac{x−μ}{σ}$

# In[220]:


a_z_score = (a - a_mean) / (a.std())
a_z_score


# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# ### Setup 1

# In[221]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[222]:


a = np.array(a)
a


# Use python's built in functionality/operators to determine the following:

# In[223]:


#Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = a.sum()
sum_of_a


# In[224]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()
min_of_a


# In[225]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()
max_of_a


# In[226]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / a.shape
mean_of_a


# In[227]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying 
# all the numbers in the above list together
product_of_a = a.prod()
product_of_a


# In[228]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a**2
squares_of_a


# In[229]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0]
odds_in_a


# In[230]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0]
evens_in_a


# ### Setup 2

# In[231]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and 
# list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)


# In[232]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
    
sum_of_b = b.sum()
sum_of_b


# In[233]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = b.min()
min_of_b


# In[234]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
max_of_b


# In[235]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = sum_of_b / np.prod(b.shape) # <sum(b[1].shape + b[0].shape)> worked as well
mean_of_b


# In[236]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        
product_of_b = b.prod()
product_of_b


# In[237]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
squares_of_b = b**2
squares_of_b


# In[238]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 != 0]
odds_in_b


# In[239]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
            
evens_in_b = b[b % 2 == 0]
evens_in_b


# In[240]:


# Exercise 9 - print out the shape of the array b.

# (rows, columns)
b.shape


# In[241]:


# Exercise 10 - transpose the array b.

np.transpose(b)


# In[242]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

np.reshape(b,np.prod(b.shape)) # hardcoded <np.reshape(b,6)>
# also works <b.reshape(1, 6)>


# In[243]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6, 1)


# ### Setup 3

# In[268]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

c = np.array(c)


# In[245]:


# Exercise 1 - Find the min, max, sum, and product of c.

c_sum = c.sum()
c_sum


# In[246]:


c_min = c.min()
c_min


# In[247]:


c_max = c.max()
c_max


# In[248]:


c_prod = c.prod()
c_prod


# In[249]:


# Exercise 2 - Determine the standard deviation of c.

c_std = c.std()
c_std


# In[250]:


# Exercise 3 - Determine the variance of c.

c_var = c.var()
c_var


# In[267]:


# Exercise 4 - Print out the shape of the array c

#(rows, columns)
shape_of_c = c.shape
shape_of_c


# In[269]:


# Exercise 5 - Transpose c and print out transposed result.

c_transposed = c.transpose()
c_transposed


# In[272]:


# Exercise 6 - Get the dot product of the array c with c.
c_dot_pro = c.dot(c,c)
c_dot_pro


# In[270]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

sum_of_prod_of_c_and_c_transposed = (c * c_transposed).sum()
sum_of_prod_of_c_and_c_transposed


# In[271]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.

prod_of_prod_of_c_and_c_transposed = (c * c_transposed).prod()
prod_of_prod_of_c_and_c_transposed


# ### Setup 4

# In[256]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)


# In[257]:


# Exercise 1 - Find the sine of all the numbers in d

sine_of_d = np.sin(d)
sine_of_d


# In[258]:


# Exercise 2 - Find the cosine of all the numbers in d

cosine_of_d = np.cos(d)
cosine_of_d


# In[259]:


# Exercise 3 - Find the tangent of all the numbers in d

tangent_of_d = np.tan(d)
tangent_of_d


# In[260]:


# Exercise 4 - Find all the negative numbers in d

negatives_in_d = d[d < 0]
negatives_in_d


# In[261]:


# Exercise 5 - Find all the positive numbers in d

positives_in_d = d[d > 0]
positives_in_d


# In[262]:


# Exercise 6 - Return an array of only the unique numbers in d.

unique_numbers_in_d = np.unique(d)
unique_numbers_in_d


# In[263]:


# Exercise 7 - Determine how many unique numbers there are in d.

how_many_unique_d = unique_numbers_in_d.shape
how_many_unique_d


# In[264]:


# Exercise 8 - Print out the shape of d.

shape_of_d = d.shape
shape_of_d


# In[265]:


# Exercise 9 - Transpose and then print out the shape of d.

d_transposed = d.transpose()
print(d_transposed)
print(d_transposed.shape)


# In[266]:


# Exercise 10 - Reshape d into an array of 9 x 2

d_nine_by_two = d.reshape(9, 2)
d_nine_by_two

