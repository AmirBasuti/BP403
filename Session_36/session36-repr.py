# Representation: __repr__

class User:
    activeUsersCount = 0 # class attribute
    allowedUsers = ["Leo", "Bob", "Alex"]
    loggedInUserNames= []

    def __init__(self, name, family):
        if name not in User.allowedUsers: # check allowed users
            raise ValueError(f"{name} is not allowed to log in")
        self.name = name # instance attribute
        self.family = family # instance attribute
        User.activeUsersCount += 1
        print(f"{self.name} logged in")
        User.loggedInUserNames.append(name)

    def __repr__(self): # def __str__(self):
        return f"Name: {self.name}, family: {self.family}"

# Messi = User("Leo1", "Messi") # raises error
Messi = User("Leo", "Messi") # raises error
print("--------------------------")
print(Messi)

# Try printing Messi after commenting __repr__

# repr vs str: both are for representation of an object with different formats
# str representation is for customer
# repr representation is for developer

print("-----------------------")
import datetime
today = datetime.datetime.now()
  
# Prints readable format for date-time object
print (str(today))
  
# prints the official format of date-time object
print (repr(today))

# change time with timedelta (1 day and 2 hours and 5 minutes later)
tomorrow = today + datetime.timedelta(days=1, hours=2, minutes=5)
print(tomorrow)

# change behavior of print
# Example:
x = list(range(10))
print(x)

for item in x:
    print(item) # print items in new lines

for item in x:
    print(item, end = "\t") # print item, insert tab
print('')

for item in x:
    print(item, end = 7*" ") # print item, insert n spaces