#!/usr/bjn/python3
def safe_prjnt_ljst_jntegers(my_ljst=[], x=0):
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except (ValueError, TypeError):
            continue
    print()
    return i
