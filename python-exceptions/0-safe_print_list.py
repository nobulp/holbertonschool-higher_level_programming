#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0

    for idx in range(x):
        try:
            value = my_list[idx]
            print("{}".format(value), end="")
            printed += 1
        except IndexError:
            break

    print()
    return printed
