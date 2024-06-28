# t1w9-python-practise

# Python Practise 
In this folder/ repo I will be practising what I am learning in order to understand how Python works and how to code using Python Language. My main focus is to have a deeper understanding of how control flow statements and functions works to be able to deliver my notes-taking application.

# Types of data in Python
INT: Whole numbers
FLOAT: Decimal Numbers
STRING: set of letters, special characters, symbols and even numbers if they are placed between double quotation.
BOOLEAN: Data type that can only have a TRUE or False value, often used with comparisons operands, logical operators.

# Operators

## Comparison Operators 
- Compare two operands and results in boolean value.
== Equality operator 
> Greater than operator 
< Less than operator 
>= Greater than or equals operator
<= Less than or equals operator

## Assignment operators 
- Used to assign values to variables
=	a = 10	a = 10
+=	a += 30	a = a + 30
-=	a -= 15	a = a - 15


# Flow statements
    - Control the flow of the program using flow statements:
    - Conditional Statements(if, elif, else) Command gets executed once one of the statements becomes TRUE.
    - FOR and WHILE Loops = Make sure items can ENTER and EXIT the loop.
    - FOR loop is used to iterate over a sequence (such as a list, tuple, string, or range) and perform actions on each item in that sequence.
    - WHILE loop (While condition is true, block of code keeps being executed). 
    - RANGE() is commonly used with FOR, it iterates over a item in a range. It can also return items in a list if needed using list() function. It can be used with (start, stop, step) or only (stop). When you want to create a sequence, you can start with 1, however if you are trying to fetch an item, you will be working with index and index by default starts at 0.
    - MATCH-CASE 
    - PASS does nothing,it is useful when you want the condition to execute something but you are not sure yet what you want, for the time-being it just passes, allowing the code to flow normally without any bugs.
    - BREAK (Exit the program)


# Local and Global Variables
- Local: it can't be access by other function or by the main program.
- Globally: it can be used in one or more than one function and it can be used in by the main function. To declare a variable global write GLOBAL before variable name.
e.g:
def some (x,y):
    global total 
    total = x + y
print(total)

# AND, OR, NOT Operators
- Logical operators, they are used to combine or invert booleans values. 
- Used with flow control statements IF, WHILE and FOR.
- AND: returns True if both operands are true value, returns False if one operand is true and the other is false, and returns False if both operands are false.
- OR: returns True if one operand is true, returns True if both operands are true, and returns False if both operands are false.
- NOT: it only work with one operand, invert the boolean value, if boolean is false, it returns True, if boolean is true, it returns False.






# Return command
It returns the value or return the function and it ends the function.
