# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:38:36 2016

@author: Mark
"""


def check_palindrome(number):
    """takes a number as a string and checks if it is a palindrome"""
    if len(number) == 0 or len(number) == 1:
        return True
    elif number[0] == number[-1]:
        print number[1:-1]
        return check_palindrome(number[1:-1])
    else:
        return False
    
    

result = []

for num in range(0,1000):
    for num2 in range(0,1000):
        if check_palindrome(str(num*num2)):
            result.append(num*num2)
print max(result)