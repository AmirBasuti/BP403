# Some list functions (commands)
myColors = ["red", "blue", "green"]

# append: adds an item to the end of the list
myColors.append("pink")
#myColors.append("pink","purple") # leads to error
# myColors.append(["pink","purple"]) # list inside list
print(myColors)

print("-------------------------------")

# extend: adds items to the end of the list
myColors = ["red", "blue", "green"]
#myColors.extend(["pink"])
myColors.extend(["gray", "purple"]) # pay attention to use [] for new items
print(myColors)

print("-------------------------------")

# insert: adds an item to specific position of the list
myColors = ["red", "blue", "green"]
#myColors.insert(1,"pink")
myColors.insert(-1,"pink") # -1 is equivalent to len(myColors)-1
print(myColors)

myColors = ["red", "blue", "green"]
myColors.insert(len(myColors),"pink") # add item to the end of list
print(myColors)

myColors = ["red", "blue", "green"]
myColors.insert(0,["pink","purple"])
print(myColors)

print("-------------------------------")

# change an item of list
myColors = ["red", "blue", "green"]
myColors[0] = "pink"
print(myColors)

print("-------------------------------")

# clear: removes all elements
myColors = ["red", "blue", "green"]
myColors.clear()
print(myColors)

print("-------------------------------")

# pop:
myColors = ["red", "blue", "green"]
item = myColors.pop() # returns last item and removes it from list
print(item)
print(myColors)

print("-------------------------------")

myColors = ["red", "blue", "green"]
item = myColors.pop(1) # returns item with index 1 and removes it from list
print(item)
print(myColors)

print("----------------------------")

# remove: removes an item
myColors = ["red", "blue", "green"]
myColors.remove("green") # remove "green"
print(myColors)

print("----------------------------")

# remove: if we have two equal items
myColors = ["red", "blue", "green", "blue"]
myColors.remove("blue") # removes only the first "blue"
print(myColors)

# myColors.remove("pink") # error, pink is not in the list