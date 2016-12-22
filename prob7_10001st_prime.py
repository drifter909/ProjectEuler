# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 12:13:00 2016

@author: Mark
"""


def is_prime(number, set_of_smaller_primes):
    for entry in set_of_smaller_primes:
        if number % entry == 0:
            return False
    return True

def listing_of_all_primes(number):
    set_of_primes = [2]
    counter = 1
    while len(set_of_primes) < number:
        if is_prime(set_of_primes[-1] + counter, set_of_primes):
            set_of_primes.append(set_of_primes[-1] + counter)
            counter = 1
        else:
            counter += 1
    return set_of_primes
    
print listing_of_all_primes(10001)

