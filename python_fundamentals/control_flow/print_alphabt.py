#!/usr/bin/env python3
for number in range(ord('a'), ord('z') + 1):
    if number != ord('e') and number != ord('q'):
        print(
            "{:c}".format(number),
            end=""
        )
