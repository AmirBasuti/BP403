# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".
# It also has functions for linear algebra, fourier transform, and matrices.
################################################################################

# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called "ndarray", it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.
################################################################################

# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.
################################################################################

# Installation of NumPy
# pip install numpy

# Import NumPy
import numpy as np

# numpy version
print(np.__version__)

# create an ndarray
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 0-D Arrays
arr = np.array(42)
print(arr)

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print("**********")

# 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Check Number of Dimensions?
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# Access Array Elements
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
# Explanation
# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6

# Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print(f'dimension of arr: {arr.ndim}')
arr2 = arr[1, 1:4]
print(arr2)
print(f'dimension of arr2: {arr2.ndim}')

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
print(arr[0, :])

# Checking the Data Type of an Array
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(type(arr))
print(arr.dtype)

# convert type from float to int
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# convert type from int to float
arr = np.array([1, 2, 3])
newarr = arr.astype(float)
print(newarr)
print(newarr.dtype)


# convert type from int to bool
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# Copy vs View
# The main difference between a copy and a view of an array is that
# the copy is a new array, and the view is just a view of the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view('int32')
x[0] = 31
print(arr)
print(x)


# Check if Array Owns it's Data
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)


# Get the Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# NumPy Array Reshaping
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
# Note:
arr[5]=100
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

# error
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)


# Unknown Dimension: use -1 (usable only for one dimension)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, -1, 2)
print(newarr)

# Flattening the arrays: converting a multidimensional array into a 1D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)


# Joining NumPy Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.concatenate((arr1, arr2), axis=0)
arr4 = np.concatenate((arr1, arr2), axis=1)
print(arr3)
print(arr4)

print(10 * '*')

# Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.stack((arr1, arr2), axis=0)
arr4 = np.stack((arr1, arr2), axis=1)
print(f'arr3: {arr3}')
print(f'arr4: {arr4}')

# Stacking Along Rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

# Stacking Along Columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

# Stacking Along Height (depth)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)

# Splitting NumPy Arrays
# Split the array in 3 parts:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6,7,8,9,10,11])
newarr = np.array_split(arr, 4)
print(newarr)
print("***********")

# split 2D array
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=0)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# hsplit()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

# vsplit()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.vsplit(arr, 3)
print(newarr)


# Searching Arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

# Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
ind1 = arr%2 == 0
print(ind1)
ind2 = arr>3
print(ind2)

# x = np.where(ind)
# print(x)

# Sorting Arrays
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


# Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

# Sort a boolean array
arr = np.array([True, False, True])
print(np.sort(arr))

# sorting 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) # sort along axis 1
print(np.sort(arr, axis = 0)) # sort along axis 0
print(np.sort(arr, axis = 1)) # sort along axis 1

# convert from list to numpy ndarray
myList = [1,2,3]
myNpArray = np.array(myList)

# convert from numpy ndarray to list
myNewList = myNpArray.tolist()

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# more real example:
##################################################
arr = np.array([41, 42, 43, 44])
# method 0 for filtering
# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
##################################################

# Creating Filter Directly From Array in above example:
##################################################
arr = np.array([41, 42, 43, 44])
# method 1
filter_arr = arr > 42
newarr = arr[filter_arr]
print(newarr)

# method 2
newarr = arr[arr>42]
print(newarr)

##################################################
print("**********")
# another example of filtering: return only even elements
# from the original array which are greater than 3:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# method 0
newarr1 = arr[arr % 2 == 0]
print(newarr1)

newarr2 = arr[arr>3]
print(newarr2)

condition1 = arr%2 == 0
condition2 = arr>3
condition1 = condition1.tolist()
condition2 = condition2.tolist()
condition4 = []
for i in range(len(condition1)):
  if condition1[i] and condition2[i]:
    condition4.append(True)
  else:
    condition4.append(False)
newarr4 = arr[condition4]

# method 1
newarr3 = arr[np.logical_and(arr%2 == 0, arr>3)]
print(newarr3)

# method 2
condition5 = (arr%2==0) & (arr>3)
newarr5 = arr[condition5]
print(newarr5)

# method 3
newarr6 = arr[(arr%2==0) & (arr>3)]
print(newarr6)


# Generate Random Number
# Example: Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print(x)

# Example: Generate 10 integers in [0,2) 
print(random.randint(2, size=10))

# Example: Generate 10 integers in [0,1) 
print(random.randint(1, size=10))

# Example: Generate a 2 x 4 array of ints between 0 and 4, inclusive:
x = np.random.randint(5, size=(2, 4))
print(x)

# Example: Generate a 2 x 4 array of ints between 3 and 7, inclusive:
x = np.random.randint(3,8, size=(2, 4))
print(x)

# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.

# Example:
x = random.rand()
print(x)

# Example: Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)
print(x)

# Generate Random Number From Array
# The choice() method takes an array as a parameter and randomly returns one of the values.

# Example: Return one of the values in an array:
x = random.choice([3, 5, 7, 9])
print(x)

# Example: Generate a 2-D array that consists of the values in
# the array parameter (3, 5, 7, and 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# Shuffling Arrays
# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

# Example: Randomly shuffle elements of following array:
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# Generating Permutation of Arrays
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

# Note: shuffle changes the original array, permutation does not.

# plot distribution of data
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
# sns.histplot([0, 1, 2, 3, 4, 5])
plt.show()

# plot distribution without histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

# Generate data with normal distribution
# Example: generate a 2by3 matrix of random data with normal distribution
x = random.normal(size=(2, 3))
print(x)

# Example: Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

# Example: show distribution of 300 normally distrubuted numbers (mean=5, std=3)
sns.distplot(random.normal(loc = 5, scale = 0.0003, size=30000), hist=False)
plt.show()



# Generate data with uniform distribution
# Example: generate a 2by3 matrix of random data between 0 and 1 
# with uniform distribution
x = random.uniform(size=(2, 3))
print(x)

# Example: Generate a random uniform distribution of size 2x3 with
# values from 5 to 12:
x = random.uniform(5, 12, size=(2, 3))
print(x)

# Example: show distribution of 3000 uniformly distrubuted numbers with
# values from 5 to 12:
x = random.uniform(5,12, size=300000)
ax = sns.distplot(x, hist=False)
ax.set_title("Approximation of Uniform Distribution")
plt.show()
