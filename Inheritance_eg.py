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

