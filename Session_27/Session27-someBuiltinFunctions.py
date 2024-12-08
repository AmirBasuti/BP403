# We can change the order of arguments when calling function
def exponent(num1=2, num2=5):
    return num1 ** num2


# we want compute 3^4
# Method 1:
print(exponent(3, 4))
# Method 2:
print(exponent(num1=3, num2=4))
# Method 3:
print(exponent(num2=4, num1=3))

# Remember ALT+SHIFT+F for beautiful code

# Built-in functions

# all: returns True when all items in an iterable are True; returns False otherwise
#      returns True for an empty iterable
# iterable: قابل تکرار : are data type which we can iterate over; >> list, tuple, dictionary, set
# iterate: تکرار کردن: for item in myList:

# Example
numList = [2, 4, 5, -1]  # all(numList): True
print(all(numList))
numList = [2, 4, 5, 0, -1]  # all(numList): False
print(all(numList))
numList = [2, 4, 5, []]  # all(numList): False
print(all(numList))
# Note:
print(all([]))  # True

print("-----------------------")
# Example: check if all items of list are even: if all items are even return True
numList = [2, 4, 9, 8]
print(numList)
numListIsEven = [num % 2 == 0 for num in numList]
print(numListIsEven)
print(all(numListIsEven))

print("----------------------")


# any: returns True if at least one item in an iterable is True, otherwise False
#       if iterable is empty, "any" returns False

print("--------------------")
# Example
numList = [0, 1, 0, 5]  # any(numList): True
print(any(numList))
numList = [0, [], 0, {}, {"Hello": 5}]  # any(numList): True
print(any(numList))
numList = [0, [], 0, {}]  # any(numList): False
print(any(numList))


print("-----------------------")
# Example: check if any items of a list is odd:
numList = [2, 4, 9, 8]
print(numList)
numListIsOdd = [num % 2 != 0 for num in numList]
print(numListIsOdd)
print(any(numListIsOdd))


print("----------------------")
# Note:
print(any([]))  # False

# sorted: sorts items of an iterable
print("--------------------")
# Previously we had .sort()
# Example:
numList = [2, 4, 0, 5, 1, 6]
numListCopy = list(numList)
numListCopy.sort()
print(numList)
print(numListCopy)

print("-----------------")
# اگر نخواهیم لیست اولیه عوض شود
numList = [2, 4, 0, 5, 1, 6]
result = sorted(numList)
print(numList)
print(result)

# sort reversely
result2 = sorted(numList, reverse=True)
print(result2)

print("------------")
# Max: returns largets item in items or returns largest item in an iterable
print(max(3, 4, 7, 0, -5))  # max function has 5 arguments
print(max([3, 4, 7, 0, -5]))  # max function has 1 argument
print(max((3, 4, 7, 0, -5)))  # max function has 1 argument

print(max([7, 4, 0, 20], [7, 5, 10]))
fruitList = ["orange", "apple", "coconut"]
print(max(fruitList))

# Example: find the fruit with the longest name
# Method 1:
fruitList = ["orange", "apple", "coconut"]
print(fruitList)
fruitLen = [len(fruit) for fruit in fruitList]
print(fruitLen)
maxValue = max(fruitLen)
print(maxValue)
maxIndex = fruitLen.index(maxValue)
print(maxIndex)
print(fruitList[maxIndex])


print("---------------")
# Method 2:
fruitList = ["orange", "apple", "coconut"]
print(fruitList)


def lenFunc(input):
    return len(input)

fruit = max(fruitList, key=lenFunc)
maxIndex = fruitList.index(fruit)

# print(max(fruitList, key=lenFunc))

# min: returns smallest item in items or returns smallest item in an iterable
print(min(3, 4, 7, 0))  # min function has 4 arguments
print(min([3, 4, 7, 0, -5]))  # min function has 1 argument
print(min((3, 4, 7, 0, -5)))  # min function has 1 argument

print(min([7, 4, 0], [7, 5, 10]))
fruitList = ["orange", "apple", "coconut"]
print(min(fruitList))

# Example: find the fruit with the longest name
# Method 1:
fruitList = ["orange1", "banana", "coconut"]
print(fruitList)
fruitLen = [len(fruit) for fruit in fruitList]
print(fruitLen)
minValue = min(fruitLen)
print(minValue)
minIndex = fruitLen.index(minValue)
print(minIndex)
print(fruitList[minIndex])


print("---------------")
# Method 2:
fruitList = ["orang", "coconut", "apple"]
print(fruitList)


def lenFunc(input):
    return len(input)


print(min(fruitList, key=lenFunc))

# reversed: reversesinput
numbers = [2, 4, 10, 1]

# previously we had:
numbers.reverse()
print(numbers)

# we do not want to change the original list
numbers = [2, 4, 10, 1]
result = reversed(numbers)
print(numbers)
print(result)

# Example of reversing

myString = "Hello"
# Method 1:
myStringReversed = myString[::-1]
print(myStringReversed)

# Method 2
myStringReversed2 = reversed(myString)
print("".join(myStringReversed2))
