#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = 0
    i = 1
    while i < len(argv):
        total = total + int(argv[i])
        i = i + 1

    print(total)
