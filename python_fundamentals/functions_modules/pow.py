#!/usr/bin/env python3
def pow(a, b):
    negative_exponent = b < 0
    if negative_exponent:
        b = -b

    result = 1
    for _ in range(b):
        result *= a

    if negative_exponent:
        return 1 / result
    return result
