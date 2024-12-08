# range() creats a sequence of numbers
# Example: A sequence of numbers from 1 to 10: [1,2,....,10]
# Method 1: This method is not good !
myList = [1,2,3,4,5,6,7,8,9,10]
# Method 2: Using range()
myNumbers = range(1,11) #[1,2,3,...,10]
#print(myNumbers) # does not print numbers
print( list(myNumbers) ) # First convert to list, then print

print("--------------------")
# The default start is 0
print( list(range(20))) # is equivalent print( list(range(0,20,1)))

# change step
print( list(range(1,10,3))) # [1,4,7]

# Negative step
print( list(range(10,2,-3))) # [10,7,4]

print("------------------")
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

print("------------------------------")

# Method 1:
for numberOfStars in range(1,11):
    print("*" * numberOfStars)

print("------------------------------")

# Method 2:
for numberOfStars in range(1,11):
    myString = "" # Empty string
    for num in range(1,numberOfStars+1):
        myString = myString + "*"
    print(myString)

# print without going to the next line
print("Hello", end=" ")
print("bye")

print("---------------------------------")
# Example: print the following pattern (10 periods of abs(sinus) wave)
# *
# **
# ***
# ****
# ***
# **
# *
# **
# ***
# ****
# ***
# **
# .
# .
# .
for number in range(0,20):
    if number % 2 == 0: # if number is even
        for num in range(1,5):
            print("*" * num)
    else:               # if number is odd
        for num in range(3,1,-1):
            print("*" * num)

print("number = ", number)
