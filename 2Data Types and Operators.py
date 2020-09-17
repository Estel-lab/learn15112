def mod(a, b):
    return a - (a // b) * b


print(41 % 14, mod(41, 14))
print(14 % 41, mod(14, 41))
print(-32 % 9, mod(-32, 9))
print(32 % -9, mod(32, -9))

print("Types Affect Semantics")
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
# print(3 + "def")

print("Precedence")
print(2 + 3 * 4)  # prints 14,not 20
print(5 + 4 % 3)  # prints 6,not 0(% has same precedence as *, /, and //)
print(2**3 *
      4)  # print 32, not 4096(** has higher precedence than *,/,//,and %)

print()

print("Associativity")
print(5 - 4 - 3)  # prints -2, not 4(- associates Left-to-right)
print(4**3**2)  # prints 262144, not 4096(** associates right-to-left)

print("Approximate Values of Floating-Point Numbers")
print(0.1 + 0.1 == 0.2)  # True
print(0.1 + 0.1 + 0.1 == 0.3)  # False
print(0.1 + 0.1 + 0.1 - 0.3)  # 5.551115123125783e-17
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004

print("The Problem...")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)  # False (never use == with floats)

print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon)  # True

print()
print("Once again, using a useful helper function, almostEqual:")


def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)


d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)
print(almostEqual(d1,
                  d2))  # True, and now packaged in a handy reusable function!


def yes():
    return True


def no():
    return False


def crash():
    return 1 / 0  # crashes!


print(no() and crash())  # Works!
print(crash() and no())  # Crashes!
print(
    yes() and crash()
)  # Never runs (due to crash), but would also crash (without short-circuiting)
