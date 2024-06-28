# Continue example
fruits = ["apple", "banana", "cherry", "date", "fig"]
for fruit in fruits:
    if len(fruit) > 5:
        continue  # Skip fruits with more than 5 characters
    print(fruit)

print("------")
# Break example, it breaks when fruit reaches cherry
fruits = ["apple", "banana", "cherry", "date", "berry"]

for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)