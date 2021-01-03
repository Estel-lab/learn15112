def count_n(n):
    k = 1
    count = 0
    while (k != 0):
        count += 1
        k = n // 10**count
    return (count)


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


print(lengthDecodeLeftmostValue(11101110))
