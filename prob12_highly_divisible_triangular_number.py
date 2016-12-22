# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:28:42 2016

@author: mharley
"""

def number_of_factors(num):
    counter = 1
    for factor in range(1,num/2 + 1):
        if num%factor == 0:
            counter += 1

    print((num,counter))
    return counter


num = 0
count = 1
while True:
    num += count
    count += 1
    if number_of_factors(num) > 500:
        break