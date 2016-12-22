# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:15:04 2016

@author: Mark
"""
import collections

def is_prime(number, set_of_smaller_primes):
    for entry in set_of_smaller_primes:
        if number % entry == 0:
            return False
    return True

set_of_primes = [2]
counter = 1

while set_of_primes[-1] < 10000:
    if is_prime(set_of_primes[-1] + counter, set_of_primes):
        set_of_primes.append(set_of_primes[-1] + counter)
        counter = 1
    else:
        counter += 1

string_set = []
for entry in set_of_primes:
    string_set.append(''.join(sorted(str(entry))))

duplicates = [item for item, count in collections.Counter(string_set).items() if count > 2]

duplicates_dict = {}
for ind,entry in enumerate(string_set):
    if entry in duplicates:
        duplicates_dict.setdefault(entry,[]).append(ind)

from itertools import izip

def is_arithmetic(seq):
    gen = (i - j for i, j in izip(seq[:-1], seq[1:]))
    diff = next(gen, None)  # get the first element in the generator
    return all(d == diff for d in gen) # check all the others are equal to it

for entry in duplicates_dict.values():
    if is_arithmetic(entry):
        print entry
        