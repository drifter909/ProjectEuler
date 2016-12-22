# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 09:38:13 2016

@author: Mark
"""

num = 2**1000
sum_digits = 0
while num > 0:
    sum_digits += num%10
    num = num/10
print sum_digits