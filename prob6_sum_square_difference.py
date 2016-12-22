# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 12:07:38 2016

@author: Mark
"""

sum_of_squares = 0
for num in range(1,101):
    sum_of_squares += num**2

print sum_of_squares - sum(range(1,101))**2