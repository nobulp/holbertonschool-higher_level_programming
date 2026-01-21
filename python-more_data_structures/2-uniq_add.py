#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    seen = []
    for n in my_list:
        if n not in seen:
            seen.append(n)
            add += n
    return add
