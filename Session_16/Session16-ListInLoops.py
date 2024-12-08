myColors = ["red", "blue", "green", 10.5]

# use list in a for loop
for color in myColors:
    if type(color)==str:
        print(f"This is a color and equal to {color}")
    else:
        print(f"{color} is not a color")

print("---------------------------")

# use list in a while loop
listIndex = 0
while listIndex < len(myColors):
    color = myColors[listIndex]
    if type(color)==str:
        print(f"This is a color and equal to {color}")
    else:
        print(f"{color} is not a color")
    
    listIndex += 1