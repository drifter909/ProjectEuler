# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:01:49 2016

@author: Mark
"""

for test_num in range(1,1000000):
    count = 0
    for multiple in range(2,7):   
        if sorted(str(test_num)) == sorted(str(multiple*test_num)):
            count += 1
    if count == 5:
        print test_num
        break