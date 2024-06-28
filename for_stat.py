# For loop used to get length of each word
words = ["Apple", "Avocado", "Zack"]

for each in words:
    print(each,len(each))

# Sum of numbers
numbers = [1,3,45,5,3,2]
total_sum = 0
for each in numbers:
    total_sum += each

print(f"Total sum of numbers are:",total_sum)


school_name = "Coder"
for each in school_name:
    print(each)

# Printing index and item using .enumerating function

fruits = ["Apple", "Banana", "Strawberry"]

for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

colours = ["Red", "Yellow", "Black"]

for index,colour in enumerate(colours):
    print(f"{index}:{colour}")

# Finding the largest number in list
numbers_list = [1,5,3,6,7,24,532,43,2]
largest_number = 1

for number in numbers_list:
    if number > largest_number:
        largest_number = number
print(f"The largest number is {largest_number}")

# Skipping vowels in variable, end=" " prints the output in horizontal line
text = "Coder Academy"
vowels ="A E I O U a e i o u"

for each in text:
    if each in vowels:
        continue
    print(each,end=" ")

