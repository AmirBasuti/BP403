# A practical project
# More advanced Rock-paper-scissors game

import random

winScore = 3
playerScore = 0
pcScore = 0

# Method 1
while (playerScore < winScore) and (pcScore < winScore):
    
    # generates a random number between 0 and 2 (including 0 and 2)
    randomNumber = random.randint(0,2)

    # PC move
    if randomNumber == 0:
        pcMove = "rock"
    elif randomNumber == 1:
        pcMove = "paper"
    else:
        pcMove = "scissors"


    # player move
    playerMove = input("Please enter your move: ").lower()

    # print player move and pc move
    print(f"Your move: {playerMove}")
    print(f"PC move: {pcMove}")

    # implement game
    if playerMove =="rock" and pcMove=="scissors":
        playerScore += 1
    elif playerMove =="scissors" and pcMove=="rock":
        pcScore += 1
    elif playerMove =="rock" and pcMove=="paper":
        pcScore += 1
    elif playerMove =="paper" and pcMove=="rock":
        playerScore += 1
    elif playerMove =="paper" and pcMove=="scissors":
        pcScore += 1
    elif playerMove =="scissors" and pcMove=="paper":
        playerScore += 1
    #elif playerMove == pcMove:   
    elif playerMove != "rock" and playerMove != "paper" and playerMove != "scissors":
        print("You did an invalid move!")

if playerScore>pcScore:
    print("Player wins !")
else:
    print("PC wins !")

print(f"Player score = {playerScore}")
print(f"PC score = {pcScore}")

# Method 2 using "break"
playerScore = 0
pcScore = 0

while True:
    
    if (pcScore >= winScore) or (playerScore >= winScore):
        break
    
    # generates a random number between 0 and 2 (including 0 and 2)
    randomNumber = random.randint(0,2)

    # PC move
    if randomNumber == 0:
        pcMove = "rock"
    elif randomNumber == 1:
        pcMove = "paper"
    else:
        pcMove = "scissors"


    # player move
    playerMove = input("Please enter your move: ").lower()

    # print player move and pc move
    print(f"Your move: {playerMove}")
    print(f"PC move: {pcMove}")

    # implement game
    if playerMove =="rock" and pcMove=="scissors":
        playerScore += 1
    elif playerMove =="scissors" and pcMove=="rock":
        pcScore += 1
    elif playerMove =="rock" and pcMove=="paper":
        pcScore += 1
    elif playerMove =="paper" and pcMove=="rock":
        playerScore += 1
    elif playerMove =="paper" and pcMove=="scissors":
        pcScore += 1
    elif playerMove =="scissors" and pcMove=="paper":
        playerScore += 1
    #elif playerMove == pcMove:   
    elif playerMove != "rock" and playerMove != "paper" and playerMove != "scissors":
        print("You did an invalid move!")


if playerScore>pcScore:
    print("Player wins !")
else:
    print("PC wins !")

print(f"Player score = {playerScore}")
print(f"PC score = {pcScore}")
