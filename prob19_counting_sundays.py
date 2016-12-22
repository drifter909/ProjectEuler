# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:10:04 2016

@author: Mark
"""
DAYS = {'Mon':1, 'Tue':2, 'Wed':3, 'Thu':4, 'Fri':5, 'Sat':6, 'Sun':0}
MONTHS_LIST = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MONTHS_DICT = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr': 30, 'May': 31, 'Jun':30, 'Jul':31, 
               'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
               

#todays_date = [day_of_week, month, year]
todays_date = [3, 0, 1901]



def is_leap_year(date):
    if date[2]%400 == 0:
        return True
    elif date[2]%100 == 0:
        return False
    elif date[2]%4 == 0:
        return True
    else:
        return False
    
def move_forward_one_month(date):
    if todays_date[1] == 1:
        if is_leap_year(date):
            num_days = 29
        else:
            num_days = 28
    else:
        num_days = MONTHS_DICT[MONTHS_LIST[date[1]]]
    new_day = (date[0] + num_days) % 7
    new_month = (date[1] + 1) % 12
    if new_month == 0:
        new_year = date[2] + 1
    else:
        new_year = date[2]
    new_date = [new_day, new_month, new_year]
    return new_date
    
sunday_counter = 0
for month in range(0,1200):
    if todays_date[0] == 0:
        sunday_counter += 1
    todays_date = move_forward_one_month(todays_date)
print sunday_counter
    

        
        