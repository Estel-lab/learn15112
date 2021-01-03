#################################################
# hw2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f20_week2_linter
import math

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


import decimal

from _decimal import *


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# Functions for you to write
#################################################

############################
# hw2-standard
############################


def getKthDigit(n, k):
    n = Decimal(n) % Decimal(10**(k + 1))
    n = Decimal(n) // Decimal(10**k)
    n = abs(n)

    return n


def isPalindromicNumber(n):
    i = 0
    j = 0
    k = 1
    n2 = 0
    while (k != 0):
        i += 1
        k = n // 10**i

    for j in range(i):
        n2 += getKthDigit(n, j) * (10**(i - j - 1))

    if (n2 == n):
        return True
    else:
        return False


def IsPrime(n):
    if (n < 2):
        return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True


def nthPalindromicPrime(n):
    i = -1
    factor = 0

    while (i != n):
        factor += 1
        while (not IsPrime(factor) or not isPalindromicNumber(factor)):
            factor += 1
            # print(factor)
        if (IsPrime(factor) and isPalindromicNumber(factor)):
            i += 1

            # print(i)

    return factor


def hasConsecutiveDigits(n):
    n_abs = abs(n)

    i = 0
    k = 1
    while (k != 0):
        i += 1
        k = n_abs // 10**i
    if i == 1:
        return False
    for j in range(i):
        if (getKthDigit(n, j) == getKthDigit(n, j + 1)):
            return True

    return False


def carrylessAdd(x1, x2):
    k = 1
    i = 0
    n = 0
    if (x1 > x2):
        n1 = x1
    else:
        n1 = x2

    while (k != 0):
        i += 1
        k = n1 // 10**i

    for j in range(i):
        nj = getKthDigit(x1, j) + getKthDigit(x2, j)

        n += getKthDigit(nj, 0) * 10**j

    return n


def longestDigitRun(n):
    n_abs = abs(n)

    i = 0  # i为n的长度
    cur_time = 0  # cur_time为现在遍历数字的频度
    cur_time_n = 0  # cur_time_n为现在遍历的数字
    max_time = 0  # 定义出现的最大频度
    max_time_n = 0  # 定义最大频度的数字

    k = 1
    while (k != 0):
        i += 1
        k = n_abs // 10**i
    if i == 1:
        return n
    for j in range(i):
        if (getKthDigit(n, j) == getKthDigit(n, j + 1)):
            cur_time_n = getKthDigit(n, j)
            cur_time += 1
        else:
            if (max_time == cur_time):
                if (max_time_n > cur_time_n):
                    max_time_n = cur_time_n
            elif (max_time < cur_time):
                max_time = cur_time
                max_time_n = cur_time_n

            cur_time = 0

    return max_time_n


############################
# hw2-bonus
############################


def nthSmithNumber(n):

    i = 0  # i为n的长度
    n1 = 0  # n1表示位数之和
    n_2 = 0  # n2表示因数之和

    k = 1
    while (k != 0):
        i += 1
        k = n // 10**i

    for j in range(i):
        n1 += getKthDigit(n, j)  # n1表示位数之和

    nx = n  # 定义计算时中间值
    factor = 2

    while (nx != 0 and factor < nx + 1):

        while (nx % factor != 0):
            factor += 1
        nx /= factor
        n_2 += factor

    if (n1 == n_2):
        return True
    else:
        return False


def carrylessMultiply(x1, x2):
    # hint: find each digit in one's column, add them mod 10,
    # then each digit in the 10's column, add them mod 10,
    # and so on...
    k1 = 1
    k2 = 1
    i1 = 0
    i2 = 0
    n_count2_count1 = 0
    n_count2 = 0  # i1,i2 is the length of x1,x2
    n = 0
    count22 = 0

    count11 = 0

    while (k1 != 0):  # slove i1
        i1 += 1
        k1 = x1 // 10**i1

    while (k2 != 0):  # slove i2
        i2 += 1
        k2 = x2 // 10**i2

    for count2 in range(i2):
        n_count2 = 0
        for count1 in range(i1):
            n_count2_count1 = getKthDigit(x1, count1) * getKthDigit(x2, count2)
            n_count2 += getKthDigit(n_count2_count1, 0) * 10**count1
        count11 = count22
        count22 = n_count2 * 10**count2
        n = carrylessAdd(count11, count22)
        print(n)

    return n


def nthKaprekarNumber(n):
    nx = 0
    i = 0
    k = 1
    nx = n**2
    n1 = 0
    n2 = 0

    while (k != 0):
        i += 1
        k = nx // 10**i

    for count in range(i):
        n1 = nx % 10**count
        n2 = nx // 10**count
        if (n1 + n2 == n):
            return True
    return False


############################
# hw2-spicy
############################

############################
# play112()
############################


def play112(game):
    return 42


############################
# integerDataStructures
############################
def count_n(n):
    k = 1
    count = 0
    while (k != 0):
        count += 1
        k = n // 10**count
    return (count)


def lengthEncode(n):
    sign_digit = 0
    if (n >= 0):
        sign_digit = 1
    else:
        sign_digit = 2
    count0 = count_n(n)
    count1 = count_n(count0)
    count2 = count_n(count1)

    n += count0 * 10**count0 + count1 * 10**(
        count0 + count1) + sign_digit * 10**(count0 + count1 + count2)

    return n


def lengthDecodeLeftmostValue(n):

    l1 = count_n(n)
    sign_digit1 = n // 10**(l1 - 1)
    count1 = n // 10**(l1 - 2) - sign_digit1 * 10
    count0 = n // 10**(l1 - 2 - count1) % 10**count1

    n1 = (n // 10**(l1 - 2 - count1 - count0)) % 10**(count0)
    if sign_digit1 == 2:
        n1 = -n1

    n2 = n % 10**(l1 - 2 - count1 - count0)
    return (n1, n2)


def newIntList():
    L = list()
    return L

def intListLen(L):
    


def encodeString(s):

    return 42


def decodeString(intList):
    return 42


#################################################
# Test Functions
# ignore_rest (tell autograder to ignore everything below here)
#################################################


def testIsPalindromicNumber():
    print('Testing isPalindromicNumber()...', end='')
    assert isPalindromicNumber(0) == True
    assert isPalindromicNumber(4) == True
    assert isPalindromicNumber(10) == False
    assert isPalindromicNumber(101) == True
    assert isPalindromicNumber(1001) == True
    assert isPalindromicNumber(10010) == False
    print('Passed.')


def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')


def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert (hasConsecutiveDigits(0) == False)
    assert (hasConsecutiveDigits(123456789) == False)
    assert (hasConsecutiveDigits(1212) == False)
    assert (hasConsecutiveDigits(1212111212) == True)
    assert (hasConsecutiveDigits(33) == True)
    assert (hasConsecutiveDigits(-1212111212) == True)
    print('Passed.')


def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert (carrylessAdd(785, 376) == 51)
    assert (carrylessAdd(0, 376) == 376)
    assert (carrylessAdd(785, 0) == 785)
    assert (carrylessAdd(30, 376) == 306)
    assert (carrylessAdd(785, 30) == 715)
    assert (carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')


def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert (longestDigitRun(117773732) == 7)
    assert (longestDigitRun(-677886) == 7)
    assert (longestDigitRun(5544) == 4)
    assert (longestDigitRun(1) == 1)
    assert (longestDigitRun(0) == 0)
    assert (longestDigitRun(22222) == 2)
    assert (longestDigitRun(111222111) == 1)
    print('Passed.')


def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert (nthSmithNumber(0) == 4)
    assert (nthSmithNumber(1) == 22)
    assert (nthSmithNumber(2) == 27)
    assert (nthSmithNumber(3) == 58)
    assert (nthSmithNumber(4) == 85)
    assert (nthSmithNumber(5) == 94)
    print('Passed.')


def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert (carrylessMultiply(643, 59) == 417)
    assert (carrylessMultiply(6412, 387) == 807234)
    print("Passed!")


def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert (nthKaprekarNumber(0) == 1)
    assert (nthKaprekarNumber(1) == 9)
    assert (nthKaprekarNumber(2) == 45)
    assert (nthKaprekarNumber(3) == 55)
    assert (nthKaprekarNumber(4) == 99)
    assert (nthKaprekarNumber(5) == 297)
    assert (nthKaprekarNumber(6) == 703)
    assert (nthKaprekarNumber(7) == 999)
    print('Passed.')


def testPlay112():
    print("Testing play112()... ", end="")
    assert (play112(5) == "88888: Unfinished!")
    assert (play112(521) == "81888: Unfinished!")
    assert (play112(52112) == "21888: Unfinished!")
    assert (play112(5211231) == "21188: Unfinished!")
    assert (play112(521123142) == "21128: Player 2 wins!")
    assert (play112(521123151) == "21181: Unfinished!")
    assert (play112(52112315142) == "21121: Player 1 wins!")
    assert (play112(523) == "88888: Player 1: move must be 1 or 2!")
    assert (play112(51223) == "28888: Player 2: move must be 1 or 2!")
    assert (play112(51211) == "28888: Player 2: occupied!")
    assert (play112(5122221) == "22888: Player 1: occupied!")
    assert (play112(51261) == "28888: Player 2: offboard!")
    assert (play112(51122324152) == "12212: Tie!")
    print("Passed!")


def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert (lengthEncode(789) == 113789)
    assert (lengthEncode(-789) == 213789)
    assert (lengthEncode(1234512345) == 12101234512345)
    assert (lengthEncode(-1234512345) == 22101234512345)
    assert (lengthEncode(0) == 1110)
    print('Passed!')


def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert (lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert (lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert (lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert (lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')


def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert (lengthDecode(113789) == 789)
    assert (lengthDecode(213789) == -789)
    assert (lengthDecode(12101234512345) == 1234512345)
    assert (lengthDecode(22101234512345) == -1234512345)
    assert (lengthDecode(1110) == 0)
    print('Passed!')


def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert (a1 == 1110)  # length-encoded 0
    assert (intListLen(a1) == 0)
    assert (intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert (a1 == 111111242)  # [1, 42]
    assert (intListLen(a1) == 1)
    assert (intListGet(a1, 0) == 42)
    assert (intListGet(a1, 1) == 'index out of range')
    assert (intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert (a1 == 1111113567)  # [1, 567]
    assert (intListLen(a1) == 1)
    assert (intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert (a1 == 111211191148888)  # [1, 9, 8888]
    assert (intListLen(a1) == 2)
    assert (intListGet(a1, 0) == 9)
    assert (intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert (poppedValue == 8888)
    assert (a1 == 11111119)  # [1, 9]
    assert (intListLen(a1) == 1)
    assert (intListGet(a1, 0) == 9)
    assert (intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert (a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert (a2 == 111211101110)
    print('Passed!')


def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert (s == 1110)  # [ 0 ]
    assert (intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert (s == 111111242)  # [ 1, 42]
    assert (intSetContains(s, 42) == True)
    s = intSetAdd(s, 42)  # multiple adds --> still just one
    assert (s == 111111242)  # [ 1, 42]
    assert (intSetContains(s, 42) == True)
    print('Passed!')


def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert (m == 1110)  # [ 0 ]
    assert (intMapContains(m, 42) == False)
    assert (intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert (m == 11121124211273)  # [ 2, 42, 73 ]
    assert (intMapContains(m, 42) == True)
    assert (intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert (m == 11121124211598765)  # [ 2, 42, 98765 ]
    assert (intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert (m == 11141124211598765112991110)  # [ 4, 42, 98765, 99, 0 ]
    assert (intMapGet(m, 42) == 98765)
    assert (intMapGet(m, 99) == 0)
    print('Passed!')


def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert (fsm == 111211411101141110
            )  # [ empty stateMap, empty startStateSet ]
    assert (isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert (fsm == 1112114111011811111111)
    assert (isAcceptingState(fsm, 1) == True)

    assert (getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert (fsm == 1112122411121114121211121115111611811111111)
    assert (getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert (getTransition(fsm, 4, 5) == 6)
    assert (getTransition(fsm, 4, 7) == 8)
    assert (getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert (fsm == 111211411101141110
            )  # [ empty stateMap, empty startStateSet ]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert (fsm == 111212241112111012121112111511161141110)
    assert (getTransition(fsm, 0, 5) == 6)

    print('Passed!')


def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1)  # 6* -> 1
    fsm = setTransition(fsm, 1, 7, 2)  # 7 -> 2
    fsm = setTransition(fsm, 2, 7, 2)  # 7* -> 2
    fsm = setTransition(fsm, 2, 8, 3)  # 7* -> 3
    assert (accepts(fsm, 78) == True)
    assert (states(fsm, 78) == 1113111111121113)  # [1,2,3]
    assert (accepts(fsm, 678) == True)
    assert (states(fsm, 678) == 11141111111111121113)  # [1,1,2,3]

    assert (accepts(fsm, 5) == False)
    assert (accepts(fsm, 788) == False)
    assert (accepts(fsm, 67) == False)
    assert (accepts(fsm, 666678) == True)
    assert (accepts(fsm, 66667777777777778) == True)
    assert (accepts(fsm, 7777777777778) == True)
    assert (accepts(fsm, 666677777777777788) == False)
    assert (accepts(fsm, 77777777777788) == False)
    assert (accepts(fsm, 7777777777778) == True)
    assert (accepts(fsm, 67777777777778) == True)
    print('Passed!')


def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert (encodeString('A') == 111111265)  # [1, 65]
    assert (encodeString('f') == 1111113102)  # [1, 102]
    assert (encodeString('3') == 111111251)  # [1, 51]
    assert (encodeString('!') == 111111233)  # [1, 33]
    assert (encodeString('Af3!') == 1114112651131021125111233
            )  # [4,65,102,51,33]
    assert (decodeString(111111265) == 'A')
    assert (decodeString(1114112651131021125111233) == 'Af3!')
    assert (decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')


def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
    testEncodeDecodeStrings()


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!

    # hw2-standard
    testIsPalindromicNumber()
    testNthPalindromicPrime()
    testHasConsecutiveDigits()
    testCarrylessAdd()
    testLongestDigitRun()

    # hw2-spicy
    testIntegerDataStructures()
    testPlay112()

    # hw2-bonus
    testNthSmithNumber()
    testCarrylessMultiply()
    testNthKaprekarNumber()


def main():
    cs112_f20_week2_linter.lint()
    testAll()


if __name__ == '__main__':
    main()