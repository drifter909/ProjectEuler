# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:42:54 2016

@author: Mark
"""


largest_seq = [1]

for num in range(1,1000000):
    print num, "still running"
    collatz_seq = []
    collatz_seq.append(num)
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num + 1
        collatz_seq.append(num)
    if len(collatz_seq) > len(largest_seq):
        largest_seq = collatz_seq
        
print largest_seq