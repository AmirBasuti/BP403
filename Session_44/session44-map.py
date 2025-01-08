# The map() function applies a function to each item of
# an iterable like list and tuple and returns an iterator.
# Example:
numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)


# A lambda function in python has the following syntax:
#           lambda arguments: expression
# Example:
myDouble = lambda x: x * 2
print(myDouble(5))

# Example: use lambda function with map()
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to list
numbersSquare = list(result)
print(numbersSquare)

# Example: Passing Multiple Iterators to map() Using Lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = map(lambda n1, n2: n1*n2, num1, num2)
print(list(result))
