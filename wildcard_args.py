# Example of *args (positional arguments)
def args_addition(*args):
    total = 0
    for each in args:
        total += each
    return total

print(args_addition(2,4,5,2))

# Example of **kwargs (you can change the order you pass kwargs it doesn't change final outcome). 
def print_info(**kwargs):
    for key, value in kwargs.items(): #use .items to go inside of kwargs "dictionary" and fetch each pair
        print(f"{key}: {value}")

print_info(name="Jess", age=30, city="Melbourne")