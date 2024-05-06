"""
chapter 2, page 47
exercise 2.1-5
"""
from typing import List

def add_binary_integers(a: List, b: List, n: int):
    c = [0 for _ in range(n + 1)]
    carry = 0
    for i in range(n):
        bit_sum = a[i] + b[i] + carry
        if bit_sum == 3:
            carry = 1
            c[i] = 1
        elif bit_sum == 2:
            carry = 1
            c[i] = 0
        else:
            carry = 0
            c[i] = bit_sum
    c[n] = carry
    return c

if __name__ == "__main__":
    import random
    for n in range(1, 1000):
        a, b = [], []
        a_int, b_int = 0, 0
        for _ in range(n):
            a.append(random.choice([0, 1]))
            b.append(random.choice([0, 1]))
            a_int += a[-1] * (2 ** (len(a) - 1))
            b_int += b[-1] * (2 ** (len(b) - 1))
        c = add_binary_integers(a, b, n)
        # print(a, len(a))
        # print(b, len(b))
        # print(c, len(c))
        assert len(c) == n + 1

        c_int = 0
        for i in range(n + 1):
            c_int += c[i] * (2 ** i)
        assert c_int == a_int + b_int, "the two values are NOT equal: {}, {}".format(c_int, a_int + b_int)
