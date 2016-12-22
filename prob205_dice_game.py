# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:59:16 2016

@author: Mark
"""

import random

def peter_roll():
    sum = 0
    for dice in range(0,4):
        sum += random.randint(1,4)
    return sum

def colin_roll():
    sum = 0
    for dice in range(0,6):
        sum += random.randint(1,6)
    return sum

peter_wins = 0
for num in xrange(0,100000003):
    if peter_roll() > colin_roll():
        peter_wins += 1
        
print peter_wins / 1000003.0000000