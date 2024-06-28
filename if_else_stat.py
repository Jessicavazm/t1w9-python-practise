# FRUIT E.G
favourite_fruit = "Banana"

if favourite_fruit == "Berry":
    print("Good choice, Berry is nice!!")
elif favourite_fruit == "Banana":
    print("Better choice, Banana is the best fruit!!")
else:
    print("All fruits are yummy!!")

# AGE E.G
age = 30

if age >= 70:
    print ("You have seniors discount!!")
if age <= 21:
    print("You have student discount")
else:
    print("You do not have discount, sorry.")

# Calculating the median of a student marks importing statistics and using median function and using IF statements to declare if student has passed or failed.
import statistics

mark1 = 7
mark2 = 8

marks = [mark1, mark2]
median = statistics.median(marks)
print(f"Media score is {median}")

if median > 5 and median < 7:
    print("Congratulations, you have passed, but next time you can do better!")
elif median > 7:
    print("Congratulations you have worked very hard!")
else:
    print("You didn't pass, next time you need to study more!")

# Collecting user input and using it with IF statement, input needs to be converted to INT since we are performing numbers comparison. User input always returns in STR by default. 

# driving_age = int(input("What is your age? ")) # user input is converted to INT

# if driving_age >= 18:
#     print("You can get behind the wheels!!")
# else:
#     print("You are too young my friend!!")

# Nested IFS, checks two conditions

age = 32
has_permission = True

if age >= 18: # first condition
    if has_permission: # second condition
        print("You can drive")
    else: # printed in case if only condition is true
        print("You can't drive")
else: # it goes straight here after first condition is False 
    print("You can't drive")

# Using boolean operator AND , code gets reduced.

if age >= 18 and has_permission:
    print("Access granted")
else:
    print("Access denied")

# Ternary operator, it condenses everything in one line of code.
# Syntax
# result IF condition ELSE result
print("Access granted") if age >= 18 and has_permission else print("Access denied,sorry")
# Another way using string as value, this example assigns a value to a variable (message).
message = "Access granted Mate" if age >=18 and has_permission else "Access Denied Mate"

print(message)