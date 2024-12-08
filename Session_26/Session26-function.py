# Function
# Definition: set of instructions which has a name and
#             the instructions will be executed when calling the name

# def functionName( list of parameters):
#   instructions
#   instructions
#    .
#    .
#    .
# Example: write a function that prints "Hello", then print "Salam"
# Definition:

def sayHello():
    print("Hello")
    print("Salam")
# call the function twice
sayHello()
sayHello()


# Example: define a function that a gets a number and raises it to power 2 and prints it
def mySquare(n):
    result = n ** 2
    print(result)

mySquare(3)

# In function definition, inputs are "parameters"
# In funvtion call, inputs are "arguments"
# n in this example is "parameter"
# 3 in this example is "argument"

# The previous function does not return anything
output = mySquare(6)
print(output)

print("--------------------------------")
x = 10

# for returning output, we use "return"
# Example: define a function that a gets a number and raises it to power 2  and returns result
def mySquare(n):
    x = 12
    result = n ** 2
    return result


output = mySquare(3)
print(output)

# We could define previous function like this:
#def mySquare(n):
#    return  n ** 2

# Example: create a function that gets an integer and returns "even" if
# the number is even and return "odd" if the number is odd
# Method1:
def evenOddFunc(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
# Method2:
def evenOddFunc2(n):
    if n%2==0:
        result = "even"
    else:
        result = "odd"
    return result


output = evenOddFunc(12)
output = evenOddFunc2(15)
print(output)

# function can have more than one output
# Example: write a function that gets a list and returns the sum of odd numbers
#  and sum of even numbers
def evenOddSum(inputList):
    sumEven = 0
    sumOdd = 0
    for num in inputList:
        if num%2==0:
            sumEven += num
        else:
            sumOdd += num
    return sumEven, sumOdd
    sumEven +=100 # unreachable
    return sumEven, sumOdd # unreachable

myList = [1,2,3,4,5,6]
print(evenOddSum(myList)) # sumEven=2+4+6=12, sumOdd=1+3+5=9
s1, s2 = evenOddSum(myList)
# Note: when reaching to first "return", execution of function will terminate

# اگر صرفا به خروجی دوم علاقه مندیم
# Method1
s2 = evenOddSum(myList)[1]
# Method2
result = evenOddSum(myList)
s2 = result[1]
# Method3
_, s2 = evenOddSum(myList)

# Example: write a function that raises number1 to power of number2
def exponent(num1, num2):
    return num1 ** num2

print(exponent(2,3))

print("-----------------------------")
# We can pass fewer arguments with "default parameters"
# print(exponent(2)) # error
# define function with default parameters
def exponent(num1=3, num2=5):
    return num1 ** num2

print(exponent(3,4)) # 3^4 = 81
print(exponent(2)) # 2^5 = 32
print(exponent()) # 3^5 = 243
print(exponent(num1 = 2, num2 = 4)) # 2^4
print(exponent(num1 = 2)) # 2^5
print(exponent(num2 = 4)) # 3^4
print(exponent(num2 = 4, num1 = 3)) # 3^4


# global variable
# without global
z = 10
def testFunc1(x):
    z = 3
    print(f'z: {z}')
    z += 5
    print(f'z: {z}')
    y = x * z
    return y

print(f'z: {z}')
output = testFunc1(6)
print(output)
print(f'z: {z}')

# with global
def testFunc2(x):
    global z
    z += 5
    y = x * z
    return y

print(f'z: {z}')
output = testFunc2(6)
print(output)
print(f'z: {z}')