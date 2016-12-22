# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:45:06 2016

@author: Mark
"""

#very inefficient

def is_prime(number, set_of_smaller_primes):
    for entry in set_of_smaller_primes:
        if number % entry == 0:
            return False
    return True

set_of_primes = [2]
counter = 1

while set_of_primes[-1] <2000000:
    if is_prime(set_of_primes[-1] + counter, set_of_primes):
        set_of_primes.append(set_of_primes[-1] + counter)
        counter = 1
    else:
        counter += 1
print sum(set_of_primes[:-1])
