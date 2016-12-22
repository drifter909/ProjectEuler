# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:51:27 2016

@author: Mark
"""
        
result = 340
test_numbers = range(1,21)
test_bools = [False]*20


def is_factor(number, multiple):
    if number % multiple == 0:
        return True
    else:
        return False

while False in test_bools:
    for entry in test_numbers:       
        test_bools[entry - 1] = is_factor(result, entry)
    print result,test_bools
    result += 340



