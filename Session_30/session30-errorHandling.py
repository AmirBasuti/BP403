# Error handling
# try except:
# try block: lets you test a block of code for errors
# except block: lets you handle the error

# خطا اجرای برنامه را متوقف میکند ولی با هندل کردن خطا میتوان با وجود خطا برنامه را ادامه داد

# Example:
# print(myNum) # NameError

# print(myNum)
try:
    print('try to print myNum')
    print(myNum)
    print('everything is OK')
except:
    print("The variable has not been defined")

print("-----------------------")
# Method2
try:
    print(myNum)
except NameError:
    print("The variable has not been defined")

print("--------------------------")

# else in error handling
try:
    print(myNum)
except:
    print("The variable has not been defined")
    print("Define variable, first !")
else:
    print("Everything is OK")

print("--------------------------")
# else: executes when there is no error in try block
myNum = 5
try:
    print(myNum)
except:
    print("The variable has not been defined")
    print("Define variable, first !")
else:
    print("Everything is OK")

# finally in error handling: this block always exceutes
print("--------------------------")
try:
    print(myNum1)
except:
    print("The variable has not been defined")
    print("Define variable, first !")
else:
    print("Everything is OK")
finally:
    print("try except has finished")


# finally in error handling: this block always exceutes
print("--------------------------")
myNum1 = 10
try:
    print(myNum1)
except:
    print("The variable has not been defined")
    print("Define variable, first !")
else:
    print("Everything is OK")
finally:
    print("try except has finished")

print("----------------------")

# Example
# def myDivide(num1, num2):
#     return num1/num2
# print(myDivide(5, 0))

def myDivide(num1, num2):
    try:
        return num1/num2
    except:
        return "There is an error!"

print(myDivide(5,2))
print(myDivide(5, "2"))
print(myDivide(5, 0))

def myDivide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Error: division by zero!"
    except TypeError:
        return "Error: type error!"

print(myDivide(5, 0))
print(myDivide(5, "H"))


