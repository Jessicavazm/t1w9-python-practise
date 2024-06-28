# t1w9-python-practise

# Python Practise 
In this folder/ repo I will be practising what I am learning in order to understand how Python works and how to code using Python Language. My main focus is to have a deeper understanding of how control flow statements and functions works to be able to deliver my notes-taking application.

## Dry Coding
- Don't repeat yourself.

## Types of data in Python
- INT: Whole numbers
- FLOAT: Decimal Numbers
- STRING: set of letters, special characters, symbols and even numbers if they are placed between double quotation.
- BOOLEAN: Data type that can only have a TRUE or False value, often used with comparisons operands, logical operators.

- List can contain different data types in one variable.
- Matrix can contains lists inside lists = 2 dimensions (nested loops are good for running multi-dimensional lists)

## Operators

## Comparison Operators 
- Compare two operands and results in boolean value.
== Equality operator 
> Greater than operator 
< Less than operator 
>= Greater than or equals operator
<= Less than or equals operator

## Assignment operators 
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

