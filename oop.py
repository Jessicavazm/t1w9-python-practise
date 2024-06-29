# Object Oriented Programming

# Define class Person
class Person:
    def __init__(self, name, age): # Initialise class Person (constructor method)
        self.name = name
        self.age = age
    
    def say_hello(self):
        print (f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Create an object
person1 = Person("Jess",30)

# Call the function say_hello using object
person1.say_hello()

# Fetch attributes in object
print(person1.age)
print(person1.name)