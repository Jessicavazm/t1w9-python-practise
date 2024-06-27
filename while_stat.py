# When the condition is "true", the block of codes keeps getting executed, once the condition changes to "false" the loops end. In this case, while the user input was different than the password, it keep asking the user for the correct input, once the user returned the correct input the loop ended. 

# password = 1234
# user_input = 0
# user_input = int(input("Type your numeric password: "))

# while user_input != password:
#     user_input = int(input("Enter your four digit password: "))
#     if user_input == password:
#         print("Access granted!!")
#     else:
#         print("Access denied")

i = 0
while i < 3:
    print(i)
    i += 1
print("Condition has changed to false and loop has ended.")

