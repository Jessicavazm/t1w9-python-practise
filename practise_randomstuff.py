#Print using F string and string interpolation 
total_amount = 5
print(f"The total amount is {total_amount}")
print("The total amount is:", total_amount)

#Comparison Operators > >= < <= != == 

a = 5
b = 3
print(a > 3) # True

# Example of how to get input
# first_name = input("Enter your first name: ")
# print("Your first name is", first_name)

# String manipulation 
a = "Jess"
ends_with = a.endswith("ss") # Result = Boolean value 
print(ends_with)

# STR.FORMAT, {} are placeholders for formatted strings
name = "Jess"
age = 30
formatted_string = "{} is {} years old".format(name,age)
print(formatted_string)

# Calculate median using .median
import statistics
numbers = [4,6,3,5,3]

median_of_numbers = statistics.median(numbers)

print(f"Median of numbers is: {median_of_numbers}" )

# Using parameter to pass an argument
def greet (name):
    print(f"Hello", name)

greet("Jess")

def greet(fname, lname):
    print(f"Hello {fname} {lname}, welcome to class!")
greet("Jess","Vaz")

# NOT Logical operator, try to think that the variable is just a name, and then you give the value to it, True or False. The logical operator not inverts the value, if False changes to True, if True changes to False but it doesn't change the variable original value.

blue_nice_colour = True

if not blue_nice_colour:
    print("Yes you are right")
else:
    print("Yellow is better than Blue")

is_raining = True

if not is_raining:
    print("Bring your umbrella")
else:
    print("Don't bring your umbrella")



