# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 21:09:11 2016

@author: Mark
"""

import random

num = random.randint(0,1)


all_paths = set()
while len(all_paths) < 75:
    new_seq = ''
    while len(new_seq) < 8:
        h = random.randint(0,1)
        if new_seq.count('R') == 20:
            new_seq += 'D'
        elif new_seq.count('D') == 20:
            new_seq += 'R'
        elif h == 1:
            new_seq += 'R'
        else:
            new_seq += 'D'
    all_paths.add(new_seq)
    print all_paths

