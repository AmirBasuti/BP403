# A practical project
# Rock-paper-scissors game

import random

# generates a random number between 0 and 2 (including 0 and 2)
randomNumber = random.randint(0,2)
#print(randomNumber)

# PC move
if randomNumber == 0:
    pcMove = "rock"
elif randomNumber == 1:
    pcMove = "paper"
else:
    pcMove = "scissors"

#print(f"PC move: {pcMove}")

# player move
playerMove = input("Please enter your move: ").lower()

print("---------------------------------")
# print player move and pc move
print(f"Your move: {playerMove}")
print(f"PC move: {pcMove}")

# implement game
if playerMove =="rock" and pcMove=="scissors":
    print("Player wins !")
elif playerMove =="scissors" and pcMove=="rock":
    print("PC wins !")
elif playerMove =="rock" and pcMove=="paper":
    print("PC wins !")
elif playerMove =="paper" and pcMove=="rock":
    print("Player wins !")
elif playerMove =="paper" and pcMove=="scissors":
    print("PC wins !")
elif playerMove =="scissors" and pcMove=="paper":
    print("Player wins !")
elif playerMove == pcMove:
    print("This is a tie!")
else:
    print("You did an invalid move!")

print("------------------------------")

# Nested conditional statements; method1
if playerMove==pcMove:
    print("This is a tie!")
elif playerMove=="rock":
    if pcMove=="scissors":
        print("Player wins !")
    elif pcMove=="paper":
        print("PC wins !")
elif playerMove=="paper":
    if pcMove=="scissors":
        print("PC wins !")
    elif pcMove=="rock":
        print("Player wins !")
elif playerMove=="scissors":
    if pcMove=="paper":
        print("Player wins !")
    elif pcMove=="rock":
        print("PC wins !")
else:
    print("You did an invalid move")

# Nested conditional statements; method2
if playerMove==pcMove:
    print("This is a tie!")
elif playerMove=="rock":
    if pcMove=="scissors":
        print("Player wins !")
    else:
        print("PC wins !")
elif playerMove=="paper":
    if pcMove=="scissors":
        print("PC wins !")
    else:
        print("Player wins !")
elif playerMove=="scissors":
    if pcMove=="paper":
        print("Player wins !")
    else:
        print("PC wins !")
else:
    print("You did an invalid move")


# Convert to lowercase or uppercase in strings
myString = "Hello WORLD"
print(myString)
print(myString.lower())
print(myString.upper())