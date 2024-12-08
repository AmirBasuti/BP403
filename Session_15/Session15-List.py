# List

# List is a collection of items and items can be of different types
myList = ["red", "blue", 12, 15.2]

# length of a list
myCourses = ["math", "physics", "chemistry", "sports"]
print(len(myCourses))

# how access list items with indexing
# access 1st item
print(myCourses[0])

# access 3rd item
print(myCourses[2])

# access last item
print(myCourses[-1])

# access second last item
print(myCourses[-2])

# invalid indexing: out of range
#print(myCourses[4])
#print(myCourses[-5])

print("------------------------")
# access a range of indices
# note: start of index range is inclusive, end of index range is exclusive: index1, index2, doesn't include index3
print(myCourses[1:3])

# from index 1 to end
print(myCourses[1:])

# from index 0 to index2
print(myCourses[:3])

# access all items
print(myCourses[:])

# myCourses[start:stop:step]
# list items every two item
print(myCourses[::2])