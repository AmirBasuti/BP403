# list comprehension
# we have a list: [0,1,2,3,4,5]
# we want to have another list: [0^2, 1^2, 2^2, 3^2, 4^2,5^2]
numbers = [0,1,2,3,4,5]
# Method 1
numbers2 = []
for num in numbers:
    numbers2.append(num ** 2)
print(numbers)
print(numbers2)

print("------------------------------")
# Method2: using list comprehension
numbers2 = [x**2 for x in numbers]
print(numbers)
print(numbers2)


# Example: convert string to a list of characters
myString = "Hello"
charList = [char for char in myString]
print(myString)
print(charList)

# Example: convert string to a list of uppercase characters
myString = "Hello"
charList = [char.upper() for char in myString]
print(myString)
print(charList)

print("------------------------")
# More advanced list comprehension
# Example: generate a list of even and pdd numbers from "numbers" list
numbers = [0,1,2,3,4,5,6,7]
evenNumbers = [num for num in numbers if num%2==0]
oddNumbers =  [num for num in numbers if num%2!=0]
print(numbers)
print(evenNumbers)
print(oddNumbers)

print("------------------")
# Example: generate a list of numbers which are even and a multiple of 3
numbers = list(range(0,20))
newNumbers = [num for num in numbers if num%2==0 and num%3==0]
print(numbers)
print(newNumbers)

print("------------------")
# Using "else" in list comprehension
# Example: create a list from numbers for which even numbers are multiplied
# by 3 and odd numbers are divided 5
# input list:  [0, 1, 2, 3,  4,  5,..]
# output list: [0,0.2,6, 0.6,12 ,1]
numbers = list(range(0,20))
newNumbers = [num*3 if num%2==0 else num/5 for num in numbers]
print(numbers)
print(newNumbers)

print("------------------------------------")
# Nested list
numbers = [1,2,3,4,5,6,7,8] # a simple list, similar to vector
nestedNumbers = [[1,2,3,4],[5,6,7,8]] # nested list, simlar to a 2*4 matrix
print(nestedNumbers[0])
print(nestedNumbers[1][1])

# indexing
# for a simple list to access index2:
value = numbers[2] # value=3
print(f"value = {value}")

# for nested list, we have double index
value = nestedNumbers[0][2] # list 0, index 2
print(f"value = {value}")

# Example: print items of a nested list
# Method:
nestedNumbers = [[1,2,3,4],[5,6,7,8]]
for i in nestedNumbers:
    for value1 in i:
        print(value1)

print("-------------------")
# Method2: using list comprehension 
newList = [print(i) for i in nestedNumbers] # prints None

# Method 3: using list comprehension
# newList = [value for value in i for i in nestedNumbers]
newList = [value for i in nestedNumbers for value in i]
print(newList)

# Example: nested list and list comprehension
# we want to create a matrix:
# matrix = [[0,1,2,3],[0,1,2,3]]
matrix = [[value for value in range(4)] for row in range(2)]
print(matrix)
matrix = [value for value in range(4) for row in range(2)]
print(matrix)

print("---------------------")
# convert a matrix to a vector
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# [1 2 3
# 4 5 6
# 7 8 9 ]
# vector = [1,2,3,4,5,6,7,8,9]
# method1:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
vector = []
for row in matrix:
    for value in row:
        vector.append(value)
print(matrix)
print(vector)

print("---------------------")
# method 2: using list comprehension
vector = [value for row in matrix for value in row]
print(matrix)
print(vector)