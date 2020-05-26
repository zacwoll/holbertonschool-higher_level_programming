#!/usr/bin/python3
def generate_mod_header(modname):
    str = "The \'\'{}\'\' module".format(modname)
    str += '\n' + len(str) * '='
    return str
def generate_fnc_header(modname, fncname):
    str = "Using \'\'{}\'\'".format(fncname)
    str += '\n' + len(str) * '-'
    str += '\n\n\t>>> {0} = __import__(\'{1}\').{0}'.format(fncname, modname)
    str += '\n\nNow use it:'
    return str

