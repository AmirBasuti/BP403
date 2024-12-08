# Why do we use dictionary instead of list?
# Price of fruits
# implement with list
priceList = [["apple",10000],["orange",150000],["banana",40000]]
# implement with dictionary
priceDictionary = {"apple":10000, "orange":150000, "banana":40000}
# reasons: 1- fast access to values in dictionary; 
#          e. g. priceDictionary["orange"],
#          In a list first we should find "orange" in the list >> is slow
# 2- Dictionary is implemented very well in Python
# 3- We deal with key instead of index


# Valid data types for keys and values
# values can have any data type
# keys have 2 limitations:
#           1- keys must be unique
myDict = {"x":1, "y":2,"x":3,"z":10} # not recommended
print(myDict)
#           2- keys must be an immutable type, 
#               so key can not be a list or another dictionary
# myDict = {"x":1, ["y1","y2"]:2,"z":10} # Error
# myDict = {"x":1, {"A":10, "B":20}:2,"z":10} # Error

# invalid keys, error
# x = set([1,2,3])
# myDict = {3:1, x:[2,6,"Hi"], "Hello":10}
# print(myDict)


# check to see if a key is in the dictionary
priceDictionary = {"apple":10000, "orange":150000, "banana":40000}
isInDict = "apple" in priceDictionary.keys() # True
print(isInDict)
isInDict = "Apple" in priceDictionary.keys() # False
print(isInDict)

print("------------------------")
# check to see if a value is in the dictionary
priceDictionary = {"apple":10000, "orange":150000, "banana":40000}
isInDict = 10000 in priceDictionary.values() # True
print(isInDict)
isInDict = 12000 in priceDictionary.values() # False
print(isInDict)

