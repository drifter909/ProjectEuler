# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:39:47 2016

@author: Mark
"""

for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print a, b, c
                break