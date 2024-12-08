# index: find index of an item
myColors = ["red","blue","green", "blue"]
blueIndex = myColors.index("blue") # returns index of first "blue"
print(blueIndex)

# index: range of search
myColors = ["red","blue","red","green","pink","red"]
redIndex = myColors.index("red",1,6) # searches from index=1 to index=6
print(redIndex)

# index is also used in strings
myString = "This is a course about index method"
redIndex = myString.index("about")
print(redIndex)


print("-------------------------------")
# count: counts the number of an item in a list
myColors = ["red","blue","red","green","pink","red"]
numOfRed = myColors.count("red") # 3 times
# numOfPurple = myColors.count("purple") # 0 times
print(numOfRed)

# count is also used in strings
myString = "This is a course about index method"
print(myString.count("is"))


print("---------------------------")
# reverse: reverses the list
myColors = ["red","blue","green"]
output = myColors.reverse() # reverses the list and returns None
print(output) # prints None
print(myColors) # prints reversed list

# another method for reversing
print(myColors[::-1])

print("---------------------------")
# sort: sorting in ascending order
numbers = [3, -1, 4.2, 10, 2]
numbers.sort()
print(numbers)

print("---------------------------")
# sort: sorting in descending order
numbers = [3, -1, 4.2, 10, 2]
numbers.sort(reverse=True)
print(numbers)

print("---------------------------")
# join: puts something between items of list and combines them into a string
myColors = ["red","blue","green"]
myColors2 = "*".join(myColors)
print(myColors2)
print(type(myColors2))

print("----------------------------------")
# note on slicing (indexing)
myColors = ["red","blue","green"]
myColorsCopy = myColors # the same object in memory
print(myColors==myColorsCopy)
print(myColors is myColorsCopy)

# changes to each of myColors or myColorsCopy applies to both
myColors[1] = "pink"
print(myColors)
print(myColorsCopy)

myColors = ["red","blue","green"]
myColorsCopy = myColors[:] # different object in memory
print(myColors==myColorsCopy)
print(myColors is myColorsCopy)
# changes to myColors does not apply to myColorsCopy
myColors[1] = "pink"
print(myColors)
print(myColorsCopy)

myColorsCopy = list(myColors) # different object in memory
print(myColors==myColorsCopy)
print(myColors is myColorsCopy)


print("----------------------------------")
# reversing a list using slicing (indexing)
myColors = ["red","blue","green"]
#myColors.reverse()
#print(myColors)

myColorsReversed = myColors[::-1]
print(myColorsReversed)

myString = "Hello"
print(myString[::-1])


# "find" is similar to "index" and is used for strings, not lists
myString = "This is a course about index method"
blueIndex = myString.find("about") # returns index of "about"
print(blueIndex)

# difference of "index" and "find" for strings
myString = "This is a course about index method"
blueIndex = myString.find("hello") # returns -1
print(blueIndex)
# blueIndex = myString.index("hello") # raises error
# print(blueIndex)
