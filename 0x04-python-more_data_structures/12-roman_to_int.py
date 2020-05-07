#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                   'I': 1}
    roman_int = 0
    prev = 0
    for x in roman_string[::-1]:
        if roman_table[x] >= prev:
            roman_int += roman_table[x]
        else:
            roman_int -= roman_table[x]
        prev = roman_table[x]
    return roman_int
