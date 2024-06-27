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

# Collecting user input and using it with IF statement, input needs to be converted to INT since we are performing numbers comparison. User input always returns in STR by default.

driving_age = int(input("What is your age? ")) # user input is converted to INT

if driving_age >= 18:
    print("You can get behind the wheels!!")
else:
    print("You are too young my friend!!")

