# Perform calculator

# Get user input
num1 = float(input("Type the first number: "))
operation = (input("Type the preferred operation (+, -, *, /): "))
num2 = float(input("Type second number: "))

# Perform calculation using IF,ELIF

if operation == "+":
    total = num1 + num2
elif operation == "-":
    total = num1 - num2 
elif operation == "*":
    total = num1 * num2
elif operation == "/":
    if num2 != 0:
        total = num1 / num2 
    else:
        print("Error, division by Zero")
else:
    print("Invalid operation, try again")

print(f"The result of the operation is {total}")