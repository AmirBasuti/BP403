myCar = {"color": "black", "maxSpeed":200, "weight":1500}
print(myCar)


# clear
print("-------------------------------------------")
myCar = {"color": "black", "maxSpeed":200, "weight":1500}
print(myCar)
myCar.clear()
print(myCar)

# copy
print("-------------------------------------------")
myCar = {"color": "black", "maxSpeed":200, "weight":1500}
print(myCar)
myCarCopy = myCar.copy() # create a new object or myCarCopy = dict(myCar)
# myCarCopy2 = myCar # point to the same object in memory
print(myCarCopy)
print(myCar == myCarCopy) # True
print(myCar is myCarCopy) # Fale

# fromkeys: generate a dictionary with default values
print("------------------------------------")
myCar2 = dict.fromkeys(["color","maxSpeed","weight"],"unknown")
print(myCar2)

# get: gets the values of a key
print("-------------------------------------------")
myCar = {"color": "black", "maxSpeed":200, "weight":1500}

print(myCar.get("color"))
print(myCar["color"])

print(myCar.get("height")) # does not generate error
#print(myCar["height"]) # returns error

# get key from value
keyList = list(myCar.keys()) # ["color", "maxSpeed", "weight"]
valueList = list(myCar.values()) # ["black", 200, 1500]
ind = valueList.index(1500)
print(keyList[ind])

# Example: check to see if a key exists in dictionary
key = "color"
# Method 1
if key in myCar.keys():
    print(f"{key} exists in dictionary")
# Method 2
if key in myCar:
    print(f"{key} exists in dictionary")
# Method 3
if myCar.get(key) != None:
    print(f"{key} exists in dictionary")

# pop: clears an item with key
print("------------------------")
priceDictionary = {"apple":10000, "orange":15000, "banana":40000}
print(priceDictionary)
output = priceDictionary.pop("orange")
print(f"New dictionary: {priceDictionary}")
print(f"output of pop: {output}")

# popitem: clears the last item added to dictionary
print("------------------------")
priceDictionary = {"apple":10000, "orange":15000, "banana":40000}
print(priceDictionary)
priceDictionary.popitem()
print(priceDictionary)

# update
print("---------------------")
firstDict = {"x":1, "y":2}
secondDict = {"z":5, "w":7, "N":9, "x":100}
print(secondDict)
secondDict.update(firstDict) # adds items and overwrites values for same keys
print(secondDict)

# change a value of dictionary
firstDict = {"x":1, "y":2}
print(firstDict)
firstDict["y"]=10
print(firstDict)

# Dictionary comprehension
# Reminder
# Example: create the list: [0,3,6,9,...,18]
# method 1: with for loop
# method 2: list(range(0,19,3))
# method 3: list comprehension: numbers = [num for num in range(0,19,3)]
# 
print("-----------------------")
# Example: create {"first":1/5, "second":2/5, "third": 3/5}  from {"first":1, "second":2, "third": 3}
firstDict = {"first":1, "second":2, "third": 3}
print(firstDict)
secondDict = {key:value/5 for key,value in firstDict.items()}
print(secondDict)
# for loop equivalent of the above code
for key,value in firstDict.items():
    secondDict[key] = value/5


# Another example: we want to create {1:3, 2:6, 3:9, 4:12}
numbersDict = {num:num*3 for num in range(1,5)}
print(numbersDict)

# Example: dictionary comprehension with if-else
# we want create dictionary: {1:"odd", 2:"even",3:"odd",.....,20:"even"}
numbersDict = {num: "even" if num%2==0 else "odd" for num in range(1,21)}
print(numbersDict)

