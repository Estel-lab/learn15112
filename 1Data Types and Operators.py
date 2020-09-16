# Data Types and Operators
# Some Builtin Types

import math
a = math.sqrt(4)


def f():
    print("This is a user-defined function")
    return 42


print("some basic types in PYthon:")
print(type(2))  # int
print(type(2.2))  # floot
print(type(2 < 2.2))  # bool(boolean)
print(type(type(42)))  # type

print("#############################")

print("And some other types we may see later in the course...")
print(type("2.2"))  # str (string or text)
print(type([1, 2, 3]))  # list
print(type((1, 2, 3)))  # tuple
print(type({1, 2}))  # set
print(type({1: 42}))  # dict(dictionary or map)
print(type(2 + 3j))  # complex (complex number)

# Some Builtin Constants
print("Some builtin constanta: ")
print(True)
print(False)
print(None)

print("And some more constants in the math module: ")
print(math.pi)
print(math.e)

# Integer Division
print("The / operator does 'nomal' float division ")
print(" 5 / 3 = ", (5 / 3))
print()
print("The // operator does integer division:")
print(" 5 // 3 = ", (5 // 3))
print(" 2 // 3 =", (2 // 3))
print(" -1 // 3 = ", (-1 // 3))
print(" -4 // 3 =", (-4 // 3))

# The Modulus or Remainder Operator (%)

print("6 % 3 =", (6 % 3))
print("5 % 3 =", (5 % 3))
print("2 % 3 =", (2 % 3))
print("0 % 3 =", (0 % 3))
print("-4 % 3 =", (-4 % 3))
print("3 % 0 =", (3 % 0))
