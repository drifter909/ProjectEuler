# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:05:56 2016

@author: Mark
"""

fib_seq = [1,1]

while fib_seq[-1] / (10**999) < 1:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

print len(fib_seq)