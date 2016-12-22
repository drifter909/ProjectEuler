# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:25:28 2016

@author: Mark
"""

def get_digits_in_list(number):
    dig_list = []
    while number > 0:
        dig_list.append(number%10)
        number = number / 10
    return dig_list

def sum_fifth_powers(number):
    dig_list = get_digits_in_list(number)
    result = 0
    for entry in dig_list:
        result += entry**5
    return result

sum_correct_vals = 0
for number in range(2,1000000):
    if sum_fifth_powers(number) == number:
        sum_correct_vals += number

print sum_correct_vals
        