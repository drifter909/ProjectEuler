# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:12:12 2016

@author: Mark
"""

def triangle_numbers(n):
    triangle_number = 0
    for number in range(1,n+1):
        triangle_number += number
    return triangle_number

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

#prime_numbers = listing_of_all_primes(100)   
#prime_divisors = []
#count = 1
#while len(prime_divisors) < 5:
#    prime_divisors = []
#    test_num = triangle_numbers(count)
#    for prime in prime_numbers:
#        if test_num < prime:
#            break
#        elif test_num % prime == 0:
#            prime_divisors.append(prime)
#    count += 1
#    print test_num, prime_divisors
            
#prime_numbers = listing_of_all_primes(100)   
divisors = []
count = 1
while len(divisors) < 500:
    divisors = []
    test_num = triangle_numbers(count)
    for number in range(1,test_num + 1):
        if test_num % number == 0:
            divisors.append(number)
    count += 1
    print test_num, len(divisors)