# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:57:08 2016

@author: Mark
"""
ODD_DIGITS = ['1','3','5','7','9']


def is_reversible(number):
    sum_value = str(number + int(str(number)[::-1]))
    for char in sum_value:
        if char not in ODD_DIGITS:
            return False
    if str(number)[0] == '0' or str(number)[-1] == '0':
        return False
#    elif sum_value[0] == '0' or sum_value[-1] == '0':
#        return False
    return True


reversible_list_count = 0
for num in xrange(0,1000000000):
    if is_reversible(num) == True:
        reversible_list_count += 1

print reversible_list_count