import decimal

from _decimal import *


def getKthDigit(n, k):
    n = Decimal(n) % Decimal(10**(k + 1))
    n = Decimal(n) // Decimal(10**k)
    n = abs(n)

    return n


def setKthDigit(n, k, d):
    if (n >= 0):
        j = -1
    else:
        j = 1

    n = n + j * getKthDigit(n, k) * (10**k) - j * Decimal(d) * (10**k)
    return n


#################################################
# hw1-spicy functions (for you to write)
#################################################


def handToDice(dice):
    n1 = getKthDigit(dice, 2)
    n2 = getKthDigit(dice, 1)
    n3 = getKthDigit(dice, 0)
    return (n1, n2, n3)


print(handToDice(321))


def diceToOrderedHand(dice):

    (n1, n2, n3) = handToDice(dice)
    n_L = max(n1, n2, n3)
    n_S = min(n1, n2, n3)
    n_M = (n1 + n2 + n3) - (n_L + n_S)
    return (n_L * 100 + n_M * 10 + n_S)

    print(diceToOrderedHand(1, 2, 3))
