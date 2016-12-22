# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:00:35 2016

@author: Mark
"""

def triangle_numbers(n):
    triangle_number = 0
    for number in range(1,n+1):
        triangle_number += number
    return triangle_number

list_of_all_triangle_numbers = []
for num in range(1,1000):
    list_of_all_triangle_numbers.append(triangle_numbers(num))
    
with open('p042_words.txt','rb') as read_file:
    contents = read_file.read().split('","')
    
contents[0] = "A"
contents[-1] = "YOUTH"

def get_word_score(word):
    score = 0
    for letter in word:
        score += ord(letter) - 64
    return score

word_counter = 0
for word in contents:
    if get_word_score(word) > list_of_all_triangle_numbers[-1]:
        print "triangle_numbers not long enough"
    elif get_word_score(word) in list_of_all_triangle_numbers:
        word_counter += 1
print word_counter