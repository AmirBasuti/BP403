# Modules in Python ماژول در پایتون

# Examples:

# random module
import random
print(random.randint(1,10))
fruitList = ["apple","orange","banana"]
print(random.choice(fruitList))


# Alias: نام مستعار
# import moduleName as alias

# Example:
import random as rd
print(rd.randint(1,10))
fruitList = ["apple","orange","banana"]
print(rd.choice(fruitList))

# import specific functions from a moule
# Example:
from random import randint, choice
print(randint(1,10))
fruitList = ["apple","orange","banana"]
print(choice(fruitList))

# import all functions from a moule
# Example:
from random import *
print(randint(1,10))
fruitList = ["apple","orange","banana"]
print(choice(fruitList))

# import functions with alias
# Example:
from random import randint as rt, choice as ce
print(rt(1,10))
fruitList = ["apple","orange","banana"]
print(ce(fruitList))


# use our own module
# Example:
import circle as cr
print(f"Area: {cr.area(3)}")
print(f"Perimeter: {cr.perimeter(3)}")
print(f"x = {cr.x}")


# list functions of a module
# dir(moduleName)

# example
import random
print(dir(random))