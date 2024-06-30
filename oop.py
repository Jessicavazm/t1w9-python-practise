# Object Oriented Programming

# Define class Person
class Person:
    def __init__(self, name, age): # Initialise class Person (constructor method).
        self.name = name
        self.age = age
    
    def say_hello(self): # Function to introduce it's self.
        print (f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Create an object
person1 = Person("Jess",30)

# Call the function say_hello using object
person1.say_hello()

# Fetch attributes in object, first you need the object_name + dot + attribute.
print(person1.age)
print(person1.name)

# Exercise from ED
class Pokemon():
    def __init__(self, name, pokedexNumber, type):
        self.name = name
        self.pokedexNumber = pokedexNumber
        self.type = type

    def introduction(self):
        print(f"Hello, my name is {self.name} and my type is {self.type}")

pikachu = Pokemon("Pikachu", 25, "Electric")
print(pikachu.name)
print(pikachu.pokedexNumber)
print(pikachu.type)

pikachu.introduction()



