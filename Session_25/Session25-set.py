# Set:
mySet = {1,2,3}
print(mySet)

# repetitive items will not add to set
mySet = {1,2,3,2,1}
print(mySet)

# indexing does not work
# print(mySet[1]) # error


# check if an item exists in a set
print(6 in mySet)

# print items of set
for item in mySet:
    print(item)

# convert a set to list and vide-versa
fruitList = ["apple", "orange", "banana"]
fruitSet = set(fruitList)
print(fruitList)
print(fruitSet)
fruitList2 = list(fruitSet)
print(fruitList2)

# add item to set
mySet = {1,2,3}
mySet.add(10)
print(mySet)
mySet.add(-5)
print(mySet)

# remove item from set
mySet = {1,2,3}
mySet.remove(2)
print(mySet)
# mySet.remove(6) # error
if 6 in mySet: # no error
    mySet.remove(6)
print("----------------------------")
# we can use discard instead of remove, discard is better
mySet = {1,2,3}
mySet.discard(2)
print(mySet)
mySet.discard(6)
print(mySet)

# clear: delets all items
mySet.clear()
print(mySet)

# union of sets اجتماع مجموعه ها
playerSet1 = {"Messi", "Ronaldo","Xavi"}
playerSet2 = {"Pirlo", "Xavi","Neymar","Pedro"}
print(playerSet1 | playerSet2)

# intersection of sets اشتراک مجموعه ها
playerSet1 = {"Messi", "Ronaldo","Xavi"}
playerSet2 = {"Pirlo", "Xavi","Neymar","Pedro"}
print(playerSet1 & playerSet2)

# set comprehension
# example: create set of numbers from 0 to 10 multiplied by 3: {0,3,6,9,..30}
mySet = {3*n for n in range(0,11)}
print(mySet)

# length of set
print(len(mySet))

# items of set must be immutable; list, dictionary, and set can not be items of a set
mySet = {2,45.6,"Hello", (34,5)}

