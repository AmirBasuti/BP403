from time import sleep

# # مثال از کاربرد sleep
# روش اول
# from time import sleep
# sleep(2)

# # روش دوم
# import time
# time.sleep(2)




# Object oriented programming (OOP)
# Python is an OOP language. Almost everything in Python is an object.
# Object is a thing that has "methods" and "attributes"
# class: initial design of an object and is similar to object.

# Create a simple class:
class myFirstClass:
    myNum = 10

# Create an object from the above class
myFirstObject = myFirstClass()
mySecondObject = myFirstClass()
print(type(myFirstObject))
print(myFirstObject.myNum)


# All classes have __init__() function. It is executed when the class is initiated.
print("-----------------------------")
class Person:
    myNum = 20 # ,myNum is an attribute
    x = 12 # x is an attribute
    def __init__(self, name, age):
        print("Hi")
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello, my name is "+self.name)
        print("My age is: ", self.age)
        print(self.myNum)
        sleep(1.5)
        # recursive call of a method
        # sayHello() # error
        # self.sayHello() # روش صحیح


person1 = Person("Sara", 60)
person2 = Person("Amin", 50)
# person3 = Person() # error

print(person1.name)
print(person1.age)
person1.sayHello()

# self: is a reference to the current instance (object) of class and is used to reach variables of that class.
# we can any name instead of self: x, xy, x2
# Note: self must be the first parameter of functions of class



# delete a attribute from an object
print(person1.age)
# del person1.age
# print(person1.age)
# del person1.sayHello #خطا میدهد، یک متد را نمیتوان از شیئ پاک کرد
# اما متد یا ویژگی را میتوان از خود کلاس پاک کرد

# pass statement
def myfunc():
    pass

myfunc()

# class definition can not be empty
class simplestClass:
    pass

print("----------------------")
# built-in classes vs our defined classes
numbers = list() # built-in
print(type(numbers))

person2 = Person("Sara", 50)
print(type(person2))


# Example
class car:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color=color
    
    def showCarSpec(self, string1):
        return f"Car name: {self.name}, Car weight: {self.weight}, Car color: {self.color}" + string1

benz = car("Benz", 3000, "Black") # benz object
bmw = car("BMW", 2500, "white")   # bmw object

print(benz.color)
print(benz.weight)
print(benz.name)
print(benz.showCarSpec(", Hi"))

print(bmw.color)