# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:26:13 2016

@author: Mark
"""

with open('p089_roman.txt', 'rb') as read_file:
    numbers = read_file.read().split()

digits_saved = 0
for number in numbers:
    if 'IIII' in number:
        if 'VIIII' in number:
            digits_saved += 3
        else:
            digits_saved += 2
    if 'XXXX' in number:
        if 'LXXXX' in number:
            digits_saved += 3
        else:
            digits_saved += 2
    if 'CCCC' in number:
        if 'DCCCC' in number:
            digits_saved += 3
        else:
            digits_saved += 2
print digits_saved