# Class: Attributes + Methods

# Instance (object) attribute versus class attribute
# Example: "color" and "model" are instance attribute (depend on the instance(object) )
class Car:
    def __init__(self, inputColor, inputModel):
        self.color = inputColor
        self.model = inputModel

Benz = Car("black",2010)
BMW = Car("white", 2012)
print(Benz.color)
print(BMW.color)
# print(Car.color)  # error

print("-----------------------------")
# Example: "wheels" is class attribute
class newCar:
    wheels = 4

    def __init__(self, inputColor, inputModel):
        self.color = inputColor
        self.model = inputModel
        # self.wheels2 = 4

    def sayHello(self):
        print("Hello")


Benz = newCar("black",2010)
BMW = newCar("white", 2012)
print(Benz.color)
print(BMW.color)
print(Benz.wheels)
print(BMW.wheels)
# print(newCar.color) # Error
print(newCar.wheels)

Benz.sayHello()
# newCar.sayHello("x") #this works but is not recommended