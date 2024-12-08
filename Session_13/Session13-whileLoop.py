# While loop

# Pseudo code:
# while expression:
#    body

# # Example: password check
# # Method 1
# password = input("Enter your password: ")
# # incorrectCounter = 0
# while password != "25": # Correct password is 25
#     # if incorrectCounter == 3:
#     #     break
#     # incorrectCounter += 1
#     print("Incorrect password !")
#     password = input("Enter your password: ")

# Method 2
# password = int(input("Enter your password: "))
# while password != 25: # Correct password is 25
#     print("Incorrect password !")
#     password = int(input("Enter your password: "))


print("----------------------------")
# Example: input password should be a 2-digit number
password = int(input("Enter your password: "))
while (password<10) or (password>=100):
    print("Incorrect password !")
    password = int(input("Enter your password: "))

# Example: print numbers from 1 to 30
# Method 1 with "for"
for number in range(1,31):
    print(number)

# for printing numbers from 30 to 1, we can change range(1,31) to range(30,0,-1)

# Method 2 with "while"
number = 1
while number<=30:
    print(number)
    number += 1 # number = number + 1

# Example: print numbers from 1 to 30 with step = 2
number = 1
while number<=30:
    print(number)
    number += 2 # number = number + 2



# break: breaks the loop
# Example: print numbers from 1 to 30; if we reach to the number that user entered, print it  and break the loop
# Method 1
userInput = int(input("Enter an integer between 1 to 30: "))
number = 1
while number<=30:
    print(number)
    if number == userInput:
        break
    number += 1

# Method 2
userInput = int(input("Enter an integer between 1 to 30: "))
for number in range(1,31):
    print(number)
    if number == userInput:
        break

# Syntax Error
# break must be inside loop
# x = 2
# if x == 6:
#     break
# else:
#     x +=1



# else in for loop

# previously we had if, elif, else structure
# if Expression:
#     body
# elif Expression2:
#     body2
# else:
#     body3

# we can have else in loops:
# Example 1: print numbers from 1 to 5
for i in range(1,6):
    print(i)
else:
    print("For finished successfully")

# equivaqlent to the code below:
for i in range(1,6):
    print(i)
print("For finished successfully")

# Example 2: print numbers from 1 to 5 and stop printing if number equals user input, body of else is not executed
userInput = int(input("Enter an integer between 1 to 5: "))
for number in range(1,6):
    print(number)
    if number == userInput:
        break
else:
    print("For finished successfully")


# clear terminal
import os
os.system("cls" if os.name=="nt" else "clear")
os.system("cls") # simpler version
