#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            out = chr(ord(c) - (ord('a') - ord('A')))
        else:
            out = c
        print("{}".format(out), end="")
    print()
