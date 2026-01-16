#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    nb_args = len(argv) - 1

    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nb_args))

    i = 1
    while i <= nb_args:
        print("{}: {}".format(i, argv[i]))
        i = i + 1
