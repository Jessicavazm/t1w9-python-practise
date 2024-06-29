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

print("------")

# Function checks if a number is ODD or even. Example of main function containing sub functions.
def is_even(num): # first function to check if the number is even or not
    return num % 2 == 0 # % gets the remainder of the division, and returns result back to function

# Empty parameters since the main feature is to get input from user.
def get_number(): # This get number from the user and coverts to integer and sends it back to function
    return int(input("Enter a number: ")) # input by default is string, here INT converts string to whole number.

def main(): # Main function
    print("Odd or Even checker") # First message to print when function runs
    number = get_number() # because this is a function, you need the parameters. Number is a variable that stores the user input.
    if is_even(number): # checking if the condition is true with IF
        print(f"{number} is even!!")
    else: # if the IF condition is not true, print this.
        print(f"{number} is Odd!!")

main() # call function outside function body and give no arguments since we are getting input from user.


