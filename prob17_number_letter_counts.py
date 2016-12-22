# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 09:43:35 2016

@author: Mark
"""


SINGLE_DIGITS = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
UNIQUE_TEENS = {0:3, 1:6, 2:6, 3:8, 4:8, 5:7, 6:7, 7:9, 8:8, 9:8}
TENS_DIGITS = {0:0, 2:5, 3:6, 4:6, 5:5, 6:5, 7:7, 8:6, 9:6}


def two_digits(number):
    """finds the length of the last two digits of any number"""
    sin_dig = number % 10
    tens_dig = (number / 10) % 10
    num_letters = 0    
    
    if tens_dig == 1:
        num_letters = UNIQUE_TEENS[sin_dig]  #teens, eleven, and twelve
    else:
        num_letters = SINGLE_DIGITS[sin_dig] + TENS_DIGITS[tens_dig]
    return num_letters
    
def third_digit(number):
    """finds the length of the third digist of a number.  Adjusts if the
    word hundred is present or not"""
    num_letters = 0
    number = number / 100
    if number > 0:                          #adds the length of 'hundred'
        num_letters = SINGLE_DIGITS[number] + 7  
    return num_letters

def sum_all_letters(max_num):
    all_letters = 0
    for number in range(0,max_num):
        all_letters += two_digits(number) + third_digit(number)
        if two_digits(number) > 0 and third_digit(number) > 0:
            all_letters += 3                #adds the length of 'and'
    return all_letters

print sum_all_letters(1000) + len("One Thousand") - 1 #-1 to not count space
    
    
    
    