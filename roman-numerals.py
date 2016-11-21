#!/usr/bin/python

import math

def checkio(num):
    digits = [];
    while num > 0:
        digits.append(num % 10)
        num = int(math.floor(num / 10))

    numerals = [
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['M', 'MM', 'MMM']
    ]

    roman = []
    i = 0
    for d in digits:
        if d > 0:
            roman.append(numerals[i][d - 1])
        i = i + 1
    return ''.join(reversed(roman))

print checkio(3999) # MMMCMXCIX
