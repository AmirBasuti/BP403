# Trueness or falseness of numbers, strings, lists

# Non-zero numners: True, zero: false
if -5.6:
    print("This is true")
else:
    print("This is false")

print("------------------------")
# Empty strings: false, Non-empty: true
if "":
    print("This is true")
else:
    print("This is false")

# example
car = input("Enter your favorite car name: ")
if car:
   print(f"Your favorite car is {car}")

# Falseness: Empty objects, 0, Empty lists, Empty strings, ...
# Trueness: Non-empty objects, Non-zero numners,Non-empty lists, Non-empty strings, ...


print("--------------------------")
# Comparison operators: <, >, <=, >=, ==, !=

# ==
# checks if number1 is equal to number2
number1 = 5
number2 = 2
print(f"{number1} == {number2}: {number1 == number2}")

# !=
# checks if number1 is not equal to number2
print(f"{number1} != {number2}: {number1 != number2}")

# >
# checks if number1 is greater than number2
print(f"{number1} > {number2}: {number1 > number2}")

# <
# checks if number1 is less than number2
print(f"{number1} < {number2}: {number1 < number2}")

# ">=" means ">" or "=="
# checks if number1 is equal or greater than number2
print(f"{number1} >= {number2}: {number1 >= number2}")

# "<=" means "<" or "=="
# checks if number1 is equal or less than number2
print(f"{number1} <= {number2}: {number1 <= number2}")

# example
age = 12
if age<14:
    print("You are not allowed to watch this film")

print("----------------------------")

# Logical operators: and, or, not
# and:
# if film is newer than 2010 and is science-fiction, then I like to watch the film
productionYear = 2020
genre = "science-fiction"
if productionYear>2010 and genre=="science-fiction":
    print("I like to watch the film")

print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")

print("------------------------------")
# or:
# if film is older than 1950 or is silent, then I don't like to watch the film
productionYear = 1960
silent = True
if productionYear<1950 or silent:
    print("I don't like to watch the film")

print(f"True or True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"False or False: {False or False}")

print("---------------------------")
# not:
# if film is not popular, I  will not watch the film
filmIsPopular = False
if not filmIsPopular:
    print("I  will not watch the film")

print(f"not True: {not True}")
print(f"not False: {not False}")

# example: cinema ticket price
# age<2 or age>=100: free
# 2<=age<8 or 65<=age<100: ticket price = 5 $
# 8<=age<65: ticket price = 10 $


# method 1
age = 7

if age<2 or age>=100:
    print("Your ticket is free of charge")
elif (age>=2 and age<8) or (age>=65 and age<100):
    print("Your ticket fee is 5 $")
else:
    print("Your ticket fee is 10 $")

# method 2
condition1 = age<2 or age>=100
condition2 = (age>=2 and age<8) or (age>=65 and age<100)
if condition1:
    print("Your ticket is free of charge")
elif condition2:
    print("Your ticket fee is 5 $")
else:
    print("Your ticket fee is 10 $")

# method 3: not preferred method
condition3 = not (condition1 or condition2) # (not condition1) and (not condition2)
if condition1:
    print("Your ticket is free of charge")
elif condition2:
    print("Your ticket fee is 5 $")
elif condition3:
    print("Your ticket fee is 10 $")

# not of not: cancel each other
print( f"not (not True): {not (not True)}")
print( f"not (not False): {not (not False)}")

# check if a variable lies in an interval, e. g. 5<x<=10
x = 9
# Method 1:
if 5<x and x<=10:
    print("Hi")

# Method 2: better
if 5< x <=10: # equivalent to if x>5 and x<10:
    print("Hi")


# 
farsiText = "متن فارسی"
print(farsiText)
import arabic_reshaper
from bidi.algorithm import get_display
reshaped_text = arabic_reshaper.reshape(farsiText)
bidi_text = get_display(reshaped_text)
print(bidi_text)

# To install arabic_reshaper enter the following in Anaconda prompt:
# pip install --upgrade arabic-reshaper
# To install bidi enter the following in Anaconda prompt:
# pip install python-bidi