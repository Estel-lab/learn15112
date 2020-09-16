print("Hello World!")
#  This is a comment
# print "What will this line do?"

# You can seperate multiple values with commas
print("Carpe", "diem")
print("Carpe")
print("diem")
# You can also use end="" to stay on the same line
print("Carpe ", end="")
print("diem")

x = 42
y = 99
# Place variable names in {squiggly braces} to print their values, like so:
print(f'Did you know that {x} + {y} is {x+y}?')

import math
print(math.factorial(20))

print("Uh oh!)  # ERROR!  missing close-quote

# Python output:
#   SyntaxError: EOL while scanning string literal

print(1/0)  # ERROR!  Division by zero!

# Python output:
#   ZeroDivisionError: integer division or modulo by zero

print("2+2=5")  # ERROR!  Untrue!!!

# Python output:
#   2+2=5

name = input("enter your name: ")
print("your name is:", name)
