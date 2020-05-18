#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: " + str(e), file=sys.stderr)
def my_div(a, b):
    return a / b
