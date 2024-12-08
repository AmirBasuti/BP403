# Tuple, meaning: chandtaii

# list
myList = [0,1,2,3,4,5] # list
# tuple
myTuple = (0,1,2,3,4,5) # tuple

# why use tuple?
# 1- list is mutable but tuple is immutable
# example: we can write myList[2]=10 but we can not write myTuple[2]=10
# immutability makes our code "safer" and avoids "logical errors"
# 2- we can use of tuple in dictionary as key
# 3- tuple is faster than list

# Indexing: similar to list
myTuple = (0,10,20,30,40,50) # tuple
print(myTuple[2])

# "in" and "not in"; similar to list
print(32 in myTuple)

# change tuple items or append()
#myTuple[2] = 100 # error10
# myTuple.append(100) # error

# Another way to create tuple
myTuple2 = tuple([0,10,20,30,40,50])
print(myTuple2)

# Example: z = f(x,y) ; (1,1)>>, (1,2)>>20, (2,1)>>-10, (2,2)>>-20
z = {(1,1): 10, (1,2):20, (2,1):-10, (2,2):-20}
print(z)

# use tuple in for loop
myTuple = (0,10,20,30,40,50)
for num in myTuple:
    print(num)

# count
print("--------------------")
myTuple = (1,2,3,-1,2,5,2)
print(myTuple.count(2))

# index
print("--------------------")
myTuple = (1,2,3,-1,2,5,2)
print(myTuple.index(2))

# nested tuple
numbers = ((1,2),(6,7))
print("--------------------")
print(numbers)
print(numbers[1][0])

# slicing
print("--------------------")
numbers = (1,3,5,6,9,10,12,15,18,20,-5)
print(numbers[1:3])

# tuples are immutable, but if a tuple includes a list, items of 
# list can be changed
myTuple = (1,3,4,[5,6,7])
print(myTuple)
myTuple[3][1] = 60
print(myTuple)
