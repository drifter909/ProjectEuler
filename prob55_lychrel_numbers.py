# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:59:17 2016

@author: Mark
"""

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False
        
def reverse_and_add(number):
    return number + int(str(number)[::-1])

list_of_non_lychrels = []
for number in xrange(0,10000):
    dummy_number = number
    for i in range(0,50):    
        if is_palindrome(reverse_and_add(dummy_number)) == True:
            list_of_non_lychrels.append(number)
            break
        else:
            dummy_number = reverse_and_add(dummy_number)

print 10000 - len(list_of_non_lychrels)