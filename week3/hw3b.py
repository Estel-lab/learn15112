#################################################
# hw3b.py
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
# hw3b-standard (no spicy on hw3b)
#################################################


def mastermindScore(target, guess):
    n = 0
    m = 0

    for i in range(len(guess)):
        if (guess[i] == target[i]):
            m += 1
        else:
            for k in range(len(target)):
                if (guess[i] == target[k] and i != k):
                    n += 1

    return


def playPoker(deck, players):
    return 42


#################################################
# hw3b-bonus
#################################################


def topLevelFunctionNames(code):
    return 42


def bonusEncode1(msg):
    return 42


def funDecode1(msg):
    return 42


def bonusEncode2(msg):
    return 42


def funDecode2(msg):
    return 42


def bonusEncode3(msg):
    return 42


def funDecode3(msg):
    return 42


#################################################
# Test Functions
#################################################


def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert (mastermindScore('abcd',
                            'aabd') == '2 exact matches, 1 partial match')
    assert (mastermindScore('efgh', 'abef') == '2 partial matches')
    assert (mastermindScore('efgh', 'efef') == '2 exact matches')
    assert (mastermindScore('ijkl', 'mnop') == 'No matches')
    assert (mastermindScore('cdef', 'cccc') == '1 exact match')
    assert (mastermindScore('cdef', 'bccc') == '1 partial match')
    assert (mastermindScore('wxyz',
                            'wwwx') == '1 exact match, 1 partial match')
    assert (mastermindScore('wxyz', 'wxya') == '3 exact matches')
    assert (mastermindScore('wxyz', 'awxy') == '3 partial matches')
    assert (mastermindScore('wxyz', 'wxyz') == 'You win!!!')
    print("Passed!'")


def testPlayPoker():
    print('Testing playPoker()...', end='')
    assert (playPoker('QD-3S', 1) == 'Player 1 wins with a high card of QD')
    assert (playPoker('QD-QC', 1) == 'Player 1 wins with a pair to QD')
    assert (playPoker('QD-JS', 1) == 'Player 1 wins with a straight to QD')
    assert (playPoker('TD-QD', 1) == 'Player 1 wins with a flush to QD')
    assert (playPoker('QD-JD',
                      1) == 'Player 1 wins with a straight flush to QD')
    assert (playPoker('QD-JD', 2) == 'Not enough cards')

    assert (playPoker('AS-2H-3C-4D',
                      2) == 'Player 2 wins with a high card of 4D')
    assert (playPoker('5S-2H-3C-4D',
                      2) == 'Player 1 wins with a high card of 5S')
    assert (playPoker('AS-2H-3C-2D', 2) == 'Player 2 wins with a pair to 2H')
    assert (playPoker('3S-2H-3C-2D', 2) == 'Player 1 wins with a pair to 3S')
    assert (playPoker('AS-2H-2C-2D',
                      2) == 'Player 1 wins with a straight to 2C')
    assert (playPoker('AS-2H-2C-3D',
                      2) == 'Player 2 wins with a straight to 3D')
    assert (playPoker('AS-2H-4S-3D', 2) == 'Player 1 wins with a flush to 4S')
    assert (playPoker('AS-2H-4S-3H',
                      2) == 'Player 2 wins with a straight flush to 3H')
    assert (playPoker('2S-2H-3S-3H',
                      2) == 'Player 1 wins with a straight flush to 3S')

    assert (playPoker('AS-2D-3C-4C-5H-6D-7S-8D',
                      2) == 'Player 2 wins with a high card of 4C')
    assert (playPoker('AS-2D-3S-4C-5H-6D-7S-8D',
                      4) == 'Player 3 wins with a flush to 7S')
    print('Passed!')


def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert (topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert (topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert (topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert (topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert (topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert (topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert (topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert (topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")


def testFunDecoder(encodeFn, decodeFn):
    s1 = ''
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(' \n\n') + random.choice(string.digits)
    for s in ['a', 'abc', s1]:
        if (decodeFn(encodeFn(s)) != s):
            raise Exception(f'Error in {decodeFn.__name__} on {repr(s)}')
    return True


def testFunDecoders():
    print('Testing funDecoders()...', end='')
    testFunDecoder(bonusEncode1, funDecode1)
    testFunDecoder(bonusEncode2, funDecode2)
    testFunDecoder(bonusEncode3, funDecode3)
    print('Passed!')


#################################################
# testAll and main
#################################################


def testAll():
    # hw3b-standard
    testMastermindScore()
    testPlayPoker()

    # hw3b-bonus
    testTopLevelFunctionNames()
    testFunDecoders()


def main():
    cs112_f20_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
