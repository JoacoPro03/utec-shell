#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        code = ord(char)
        if ord('a') <= code <= ord('z'):
            result += chr(code - 32)
        else:
            result += char
    print("{}".format(result))
