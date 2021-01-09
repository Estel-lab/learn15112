#################################################
# hw3a.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f20_week3_linter
import string, copy, random

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


import decimal


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# Functions for you to write
#################################################

#################################################
# hw3a-standard
#################################################


def vowelCount(s):
    s = s.lower()
    n = 0
    factor = "aeiou"
    for c in factor:
        n += s.count(c)
    return n


def applyCaesarCipher(message, shift):

    newMessage = ""
    for i in range(len(message)):

        if (ord(message[i]) <= 123 - shift):

            newMessage += chr((ord(message[i]) + shift))
        else:
            newMessage += chr((ord(message[i]) + shift - 26))

    return newMessage


def rotateStringLeft(s, n):
    if (n >= 0):
        s = s[n % len(s):len(s)] + s[:n % len(s)]
    else:
        s = s[len(s) - n % len(s):len(s)] + s[:len(s) - n % len(s)]

    return s


def isRotation(s, t):
    for i in range(len(t)):
        if (t[i] == s[0]):
            for n in range(0, len(t)):
                if (t[(i + n) % len(t)] != s[n]):
                    return False
        else:
            return False
    return True


#################################################
# hw3a-spicy
#################################################


def encodeRightLeftRouteCipher(text, rows):
    free = rows - len(text) % rows
    encode = ""

    for i in range(free):
        text += chr(122 - i)  # 122 is ascii of "z"

    for i in range(0, rows):
        if (i % 2 == 0):
            encode += text[i:len(text):rows]
        else:
            encode += text[len(text) - rows + i:0:-rows]

    encode = "%d" % rows + encode

    return encode


def decodeRightLeftRouteCipher(cipher):
    return 42


def getEvalSteps(expr):
    return 42


#################################################
# Test Functions
#################################################


def testVowelCount():
    print('Testing vowelCount()...', end='')
    assert (vowelCount('abcdefg') == 2)
    assert (vowelCount('ABCDEFG') == 2)
    assert (vowelCount('') == 0)
    assert (vowelCount('This is a test.  12345.') == 4)
    assert (vowelCount(string.ascii_lowercase) == 5)
    assert (vowelCount(string.ascii_lowercase * 100) == 500)
    assert (vowelCount(string.ascii_uppercase) == 5)
    assert (vowelCount(string.punctuation) == 0)
    assert (vowelCount(string.whitespace) == 0)
    print('Passed!')


def testApplyCaesarCipher():
    print('Testing applyCaesarCipher()...', end='')
    assert (applyCaesarCipher('abcdefghijklmnopqrstuvwxyz',
                              3) == 'defghijklmnopqrstuvwxyzabc')
    assert (applyCaesarCipher('We Attack At Dawn', 1) == 'Xf Buubdl Bu Ebxo')
    assert (applyCaesarCipher('1234', 6) == '1234')
    assert (applyCaesarCipher('abcdefghijklmnopqrstuvwxyz',
                              25) == 'zabcdefghijklmnopqrstuvwxy')
    assert (applyCaesarCipher('We Attack At Dawn', 2) == 'Yg Cvvcem Cv Fcyp')
    assert (applyCaesarCipher('We Attack At Dawn', 4) == 'Ai Exxego Ex Hear')
    assert (applyCaesarCipher('We Attack At Dawn', -1) == 'Vd Zsszbj Zs Czvm')
    # And now, the whole point...
    assert (applyCaesarCipher(applyCaesarCipher('This is Great', 25),
                              -25) == 'This is Great')
    print('Passed.')


def testRotateStringLeft():
    print('Testing rotateStringLeft()...', end='')
    assert (rotateStringLeft('abcde', 0) == 'abcde')
    assert (rotateStringLeft('abcde', 1) == 'bcdea')
    assert (rotateStringLeft('abcde', 2) == 'cdeab')
    assert (rotateStringLeft('abcde', 3) == 'deabc')
    assert (rotateStringLeft('abcde', 4) == 'eabcd')
    assert (rotateStringLeft('abcde', 5) == 'abcde')
    assert (rotateStringLeft('abcde', 25) == 'abcde')
    assert (rotateStringLeft('abcde', 28) == 'deabc')
    assert (rotateStringLeft('abcde', -1) == 'eabcd')
    assert (rotateStringLeft('abcde', -24) == 'bcdea')
    assert (rotateStringLeft('abcde', -25) == 'abcde')
    assert (rotateStringLeft('abcde', -26) == 'eabcd')
    print('Passed!')


def testIsRotation():
    print('Testing isRotation()...', end='')
    assert (isRotation('a',
                       'a') == False)  # a string is not a rotation of itself
    assert (isRotation('',
                       '') == False)  # a string is not a rotation of itself
    assert (isRotation('ab', 'ba') == True)
    assert (isRotation('abcd', 'dabc') == True)
    assert (isRotation('abcd', 'cdab') == True)
    assert (isRotation('abcd', 'bcda') == True)
    assert (isRotation('abcd', 'abcd') == False)
    assert (isRotation('abcd', 'bcd') == False)
    assert (isRotation('abcd', 'bcdx') == False)
    print('Passed!')


def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       4) == "4WTAWNTAEACDzyAKT")
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       3) == "3WTCTWNDKTEAAAAz")
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       5) == "5WADACEAKWNATTTz")
    print('Passed!')


def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert (
        decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") == "WEATTACKATDAWN")
    assert (decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") == "WEATTACKATDAWN")
    assert (decodeRightLeftRouteCipher("5WADACEAKWNATTTz") == "WEATTACKATDAWN")
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert (plaintext == text)
    print('Passed!')


def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()


def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert (getEvalSteps("0") == "0 = 0")
    assert (getEvalSteps("2") == "2 = 2")
    assert (getEvalSteps("3+2") == "3+2 = 5")
    assert (getEvalSteps("3-2") == "3-2 = 1")
    assert (getEvalSteps("3**2") == "3**2 = 9")
    assert (getEvalSteps("31%16") == "31%16 = 15")
    assert (getEvalSteps("31*16") == "31*16 = 496")
    assert (getEvalSteps("32//16") == "32//16 = 2")
    assert (getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert (getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert (getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert (getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")


#################################################
# testAll and main
#################################################


def testAll():
    # hw3a-standard
    testVowelCount()
    testApplyCaesarCipher()
    testRotateStringLeft()
    testIsRotation()

    # hw3a-spicy
    testEncodeAndDecodeRightLeftRouteCipher()
    testGetEvalSteps()


def main():
    cs112_f20_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
