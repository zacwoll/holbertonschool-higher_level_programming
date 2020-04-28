#!/usr/bin/python3
for i in range(26):
    if i % 2 != 0:
        i = chr(ord('z') - i - 32)
    else:
        i = chr(ord('z') - i)
    print(i, end='')
