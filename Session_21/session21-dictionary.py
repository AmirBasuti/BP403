# Dictionary
# Dictionary = {
#               key1: value1,
#               key2: value2,
#               .
#               .
#               .
#               keyN: valueN,
#               }
# Example: Dictionary of fruits and their price
priceDictionary = {
    "apple": 10000,
    "orange": 15000,
    "banana": 40000
}
print(priceDictionary)

# Another way to create dictionary
priceDictionary2 = dict([
    ["apple", 10000],
    ["orange", 15000],
    ["banana", 40000]
])
print(priceDictionary2)

# Another way to create dictionary
priceDictionary3 = dict([
    ("apple", 10000),
    ("orange", 15000),
    ("banana", 40000)
])
print(priceDictionary3)

# Another way to create dictionary (more limited way)
priceDictionary4 = dict(
    apple = 10000,
    orange = 15000,
    banana = 40000
)
print(priceDictionary4)

# Access to dictionary values
print(priceDictionary["orange"])
#print(priceDictionary["yellow"]) # key "yellow" does not exist; Error

print("--------------------------------")
# Access to dictionary values in loop
for price in priceDictionary.values():
    print(price)
print("----------------------")
print(priceDictionary.values())
print(type(priceDictionary.values()))


print("--------------------------------")
# Access to dictionary keys in loop
for key in priceDictionary.keys():
    print(key)
print("----------------------")
print(priceDictionary.keys())
print(type(priceDictionary.keys()))

# Another way to access to dictionary values in loop
for key in priceDictionary.keys():
    print(priceDictionary[key])

print("----------------------------------")
# Accessing both keys and values in a loop
for item in priceDictionary.items():
    print(item)
print(priceDictionary.items())
print(type(priceDictionary.items()))

print("----------------------------------")
# Another method for accessing both keys and values in a loop
for key,value in priceDictionary.items():
    print(f"The value for key {key} is: {value}")

