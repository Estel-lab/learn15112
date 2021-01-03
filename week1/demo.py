import decimal

from _decimal import *


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def getKthDigit(n, k):
    n = Decimal(n) % Decimal(10**(k + 1))
    n = Decimal(n) // Decimal(10**k)
    n = abs(n)

    return n


def isPalindromicNumber(n):
    i = 0
    j = 0
    k = 0
    while (k != 0):
        k = n // 10**i
        i += 1
    for j in range(roundHalfUp((i + 1) / 2)):
        if (getKthDigit(n, j) != getKthDigit(n, i - j)):
            return False
    return True


print(isPalindromicNumber(1221))
