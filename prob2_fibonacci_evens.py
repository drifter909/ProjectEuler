# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:31:28 2016

@author: Mark
"""

def fibonacci(number_of_terms):
    term1 = 1
    term2 = 2
    all_terms = [1,2]
    while number_of_terms - 2 > 0:
        all_terms.append(term1 + term2)
        term1, term2 = term2, term1 + term2
        number_of_terms -= 1
    return all_terms

counter = 2
while True:
    if fibonacci(counter)[-1] > 4000000:
        break
    else:
        list_of_terms = fibonacci(counter)
        counter += 1
        
result = 0

for entry in list_of_terms:
    if entry%2 == 0:
        result += entry
print result