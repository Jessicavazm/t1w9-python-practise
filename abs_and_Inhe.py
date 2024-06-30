class Mug:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.status = "Full"

    def drink(self):
        self.status = "Empty"
        return f"I'm drinking from the {self.name}."

    def fill(self):
        self.status = "Full"
        return f"I'm filling the {self.name}"

# class Kmart(Mug):
#     def __init__(self):
#         super().__init__("Kmart mug", "purple")

#     def extras(self):
#         return f"This mug comes with small gift"
    
# class Target(Mug):
#     def __init__(self):
#         super().__init__("Target mug", "yellow")
#     def extras(self):
#         return f"This mug comes a sample of Brazilian coffee beans"

# kmart_mug = Kmart()

# print(kmart_mug.extras())   

mug1 = Mug("Kmart mug", "white")
mug2 = Mug("Target mug", "pink")


mug1.drink()
mug1.fill()

mug2.drink()

print(f"The {mug1.name} is currently {mug1.status}")
print(f"The {mug2.name} is currently {mug2.status}")

print(mug1.drink())

print("------")

# Second example of Inheritance 

class Animals: # Create a new class
    def __init__(self, name, age): # Construct the class with init, adding name and age attributes
        self.name = name #self. allows you to access instance's attributes
        self.age = age

    def eat(self): # creates a function of the instance
        return f"{self.name} is eating"
    
    def sleep(self): # creates a function of the instance
        return f"{self.name} is sleeping"
    
class Dog(Animals): # Creates a derived/ subclass that inherits attributes and methods from base class.
    def __init__(self, name, age): # this constructor for the subclass, you need this in case you want to add more attributes/ methods to the class Dog, without this, Dog inherits attributes/method from base class.
        super().__init__(name, age) # this calls the constructor from the base class (super class).

dog1 = Dog("Biel", 3) # Created a new object for class Dog, and used attributes and methods from base class.

# Accessing dog1 attributes
print(dog1.name) # prints Biel
print(dog1.age) # gets dog age

# Accessing dog1 methods
print(dog1.sleep()) # prints Biel is sleeping, since this is a method it needs()
print(dog1.eat()) # prints Biel is eating, since this is a method it needs()


