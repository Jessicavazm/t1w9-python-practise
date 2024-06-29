# t1w9-python-practise

# Python Practise 
In this folder/ repo I will be practising what I am learning in order to understand how Python works and how to code using Python Language. My main focus is to have a deeper understanding of how control flow statements and functions works to be able to deliver my notes-taking application.

## Dry Coding
- Don't repeat yourself.

## Basic Data types 
- INT: Whole numbers
- FLOAT: Decimal Numbers
- STRING: set of letters, special characters, symbols and even numbers if they are placed between double quotation.
- BOOLEAN: Data type that can only have a TRUE or False value, often used with comparisons operands, logical operators.

## Advanced data types

### List []
- Syntax: list_name = [item1, item2, item3, ...]
- A list is an ordered collection of items that can be of different types.
- Mutable and it can contain repetitive items.
- Matrix can contains lists inside list = 2 dimensions (nested loops are good for running multi-dimensional lists)

### Tuples ()
- Syntax: list_name = (item1, item2, item3, ...)
- Ordered collection of items that can be of different types similar to lists but IMMUTABLE.

### Dictionary {}
- Syntax: dict_name = {key1: value1, key2: value2, ...}
- Collection of KEY-VALUE pairs. Each key-value is unique.
- Unordered
- Mutable 

### Sets
- Syntax: set_name = {item1, item2, item3, ...}
- Unordered 
- Unique elements
- Mutable
- Sets operations:
    - Union: Add sets together
    - Intersection: Common value
    - Difference: Elements in first set but not in second set.

## Operators

### Comparison Operators 
- Compare two operands and results in boolean value.
== Equality operator 
> Greater than operator 
< Less than operator 
>= Greater than or equals operator
<= Less than or equals operator

### Assignment operators 
- Used to execute operator and assign value back to variable.
=	a = 10	a = 10
+=	a += 30	a = a + 30
-=	a -= 15	a = a - 15

## Flow statements
- Control the flow of the program using flow statements:
- Conditional Statements(if, elif, else) Command gets executed once one of the statements becomes TRUE.
- Nested IFS, check two conditions
- FOR and WHILE Loops = Make sure items can ENTER and EXIT the loop.
- FOR loop is used to iterate over a sequence (such as a list, tuple, string, or range) and perform actions on each item in that sequence. Once it interacts over all elements it automatically exit.
- WHILE loop while condition is true, block of code keeps being executed. You need to make sure the condition becomes false at one point in order to program to exit loop.  
- RANGE() is commonly used with FOR, it iterates over a item in a range. It can also return items in a list if needed using list() function. It can be used with (start, stop, step) or only (stop). When you want to create a sequence, you can start with 1, however if you are trying to fetch an item, you will be working with index and index by default starts at 0.
- MATCH-CASE statement matches a variable to a case
- PASS does nothing,it is useful when you want the condition to execute something but you are not sure yet what you want, for the time-being it just passes, allowing the code to flow normally without any bugs.

## Loop control statements
- BREAK is used to exit the program earlier. It can be used with FOR and WHILE loops.
- CONTINUE is used to skip an interaction without exiting the loop. It can be used with FOR and WHILE loops.

### Difference between IF,ELIF statement and Loops
```
When to use IF:
- IF statement evaluates a condition, IF True do this, IF False do that.
- They are used with conditional statements, it decides whether or not to run a block of code depending on the condition being True or False.
- Use them when you need to make a choice or decision based on something, once program gets to them, it runs the code ONCE.
```

```
When to use LOOPS:
- Loops are used to execute a blocks multiple times
- FOR Loop: Iterates over a sequence (like a list, tuple, string, or range). It interacts over every element of the sequence in the order they appear.
- WHILE Loop: Repeats as long as a condition is true. Continues to execute until condition fails.
- Use loops when you need to perform repetitive tasks, such as iterating over elements in a collection, executing a block of code a certain number of times, or repeating actions while a condition holds true.
```

## Local and Global Variables
- Local: it can't be access by other function or by the main program.
- Globally: it can be used in one or more than one function and it can be used in by the main function. To declare a variable global write GLOBAL before variable name.
e.g:
def some (x,y):
    global total 
    total = x + y
print(total)

## AND, OR, NOT Operators
- Logical operators, they are used to combine or invert booleans values. 
- Used with flow control statements IF, WHILE and FOR.
- AND: returns True if both operands are true value, returns False if one operand is true and the other is false, and returns False if both operands are false.
- OR: returns True if one operand is true, returns True if both operands are true, and returns False if both operands are false.
- NOT: it only work with one operand, invert the boolean value, if boolean is false, it returns True, if boolean is true, it returns False.

## Return command
It returns the value or return the function and it ends the function.

## Print
- F string is used to include multiple expressions or variables in string.
Expressions are combination of values/ variables/ operators or functions that can be evaluated to produce another value.

## Range
- It's pre-saved method in python library that generates a sequence of numbers
- (Start, Stop, Step) (0,you need to define, 1) where 0 and 1 are default arguments for start and step.
- If you want to print in reverse, you can use negative step -1. Start number > stop number to work.

## Functions
- Block of codes that performs a specific task, they can reused. Functions can intake inputs (args), process them and return an output(result).
- They help to keep the code more readable and organised.
- In a function structure you need the main function and inside the main function you have the sub-functions.
- Parameters are used to pass information to function, if a function gets input the parameters will be empty since there's no need to pass information in this case.

## Arguments and Parameters

- Wildcard args (*args and **kwargs) allows functions to accept a x number of args, it's useful when you don't know the amount of the arguments the function will take. Both args accepts any number of arguments.
- *args: these are positional arguments, args are passed in their position order. 
- **kwargs: key and value keys, similar to Dictionary. It collects the KEY-Value pairs into a dictionary under **kwargs.




## Classes
- Classes 

## Pseudo code
- Description of steps in an algorithm or a program, step by step in human language using some code syntaxes. 
- Pseudo code serves as a bridge between human understanding and eventual implementation in a programming language.

## Flow chart
- Diagram that represents a process or an algorithm, it helps to visualize.
    - Oval = Start/ End
    - Parallelogram = Input/ Output
    - Rectangle = Process/ Step
    - Diamond = Decision
    - Arrow = Flow

