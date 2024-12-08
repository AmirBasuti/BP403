# Example: Generate matrix [[0,1^2,2^2,3^2,...,9^2],[0,1^2,2^2,3^2,...,9^2]]
matrix = []
for row in range(2):
    rowVal = []
    for col in range(10):
        colVal = col ** 2
        rowVal.append(colVal)
    matrix.append(rowVal)
print(matrix)

matrix1 = [[col**2 for col in range(10)] for row in range(2)]
print(matrix1)

print("---------------------------------")
# Example: implement if-elif-else with list comprehension
# [0,1,2,...8,9,10*2,11*2,12*2,13*2,14*2,15*3,16*3,17*3,18*3,19*3]
firstList = list(range(20))
print(f"First list: {firstList}")
secondList = []
for val in firstList:
    if val < 10:
        secondList.append(val)
    elif val >= 10 and val < 15:
        secondList.append(2*val)
    else:
        secondList.append(val*3)
print(f"Second list: {secondList}")

thirdList = [val if val < 10 else val * 2 if (val >= 10 and val < 15) else val*3 for val in firstList]
print(f"Third list: {thirdList}")

