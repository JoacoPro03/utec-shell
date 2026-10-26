#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    number_printed = 0
    for index in range(x):
        try:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                number_printed += 1
        except IndexError:
            break
    print()
    return number_printed
