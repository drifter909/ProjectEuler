# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:56:15 2016

@author: Mark
"""


def get_prime_list():
    prime_list = []
    with open('C:/Users/Mark/Dropbox/ProgrammingFiles/ProjectEuler/primes-to-100k.txt', 'r') as f:
        read_data = f.read().splitlines()
        for entry in read_data:
            prime_list.append(int(entry))
    return prime_list

def prime_factors(number, prime_list):
    result = []
    for prime in prime_list:
        if number%prime == 0:
            result.append(prime)
    return result
    

print prime_factors(600851475143, get_prime_list())