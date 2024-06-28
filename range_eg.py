# Syntax using for and range:
# for variable in range():
#     block of codes

# Sum using FOR and RANGE s = (1,4,7,10,13,16,19) 
s = 0
for each in range(1,20,3):
    s = s + each
print(s)

# Sum of even numbers
total_sum = 0
for each in range(2,11,2):
    total_sum += each
print(f"Total sum of even numbers is: {total_sum}")

# Loop FOR = getting index of fruits and printing items + index

fruits = ['Apple', 'Banana', 'Berry']

for index in range(len(fruits)):
    print(f'Index: {index}, Fruit: {fruits[index]}')

# another e.g

names = ["Jessica", "Luke", "Zack"]
for index in range(len(names)):
    print(f"{index}:{names[index]}")

list = ["Apple", "Banana", "Strawberry"]

for index in range (len(list)):
    print(index)

for each in range(1,3,1):
    print(each)

# Range in reverse, start number needs to be > than stop number.
for each in range(10,5,-1):
    print(each)

# Using for and range to calculate the total, initialised total to 0 is necessary to ensure the variable total starts at a know stage.
total = 0
for each in range(1,5,1):
    total += each
print(total)
