# How to define an function

# def function_name(parameters):
#     block of code
#     return value 

# function_name(pass_parameters) call function and pass parameters

def greet (name): # greet is the function name / name is the variable parameter
    print(f"Hello", name) # block of code that gets executed once function is called

greet("Jess") # function is called outside function body and passed argument = Jess

def greet(fname, lname):
    print(f"Hello {fname} {lname}, welcome to class!")
greet("Jess","Vaz")

# Function addition
def addition(num1,num2): # created function that takes two parameters
    sum = num1 + num2 # store addition in variable sum
    return sum # returns sum once function is called
print(addition(4,5)) # function is called outside function body and given arguments 
