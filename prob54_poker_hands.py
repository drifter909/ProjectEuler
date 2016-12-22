# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:14:14 2016

@author: Mark
"""

SUITS = ['H', 'C', 'S', 'D']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
RANKED_HANDS = {'straight flush':100, 'four of a kind':90, 'full house':80, 'flush':70, 'straight':60, 'three of a kind':50, 'two pairs':40, 'one pair':30, 'high card':20}

with open('p054_poker.txt', 'rb') as read_file:
    contents = read_file.read().split('\n')
    
del contents[-1] #last row imported as empty string

player1_hands = []
player2_hands = []
for entry in contents:
    player1_hands.append(entry[:14])
    player2_hands.append(entry[15:])
    
    
def get_values(hand):
    hand_values = []
    for char in hand:
        if char in VALUES[0:8]:
            hand_values.append(int(char))
        elif char == 'T':
            hand_values.append(10)
        elif char == 'J':
            hand_values.append(11)
        elif char == 'Q':
            hand_values.append(12)
        elif char == 'K':
            hand_values.append(13)
        elif char == 'A':
            hand_values.append(14)
        sorted_hand = sorted(hand_values)
    return sorted_hand   

def check_for_flush(hand):
    for entry in SUITS:
        if hand.count(entry) == 5:
            return True
    return False
    
def check_for_straight(hand):
    sorted_hand = get_values(hand)
    if sorted_hand[0] == sorted_hand[1] - 1:
        if sorted_hand[1] == sorted_hand[2] - 1:
            if sorted_hand[2] == sorted_hand[3] - 1:
                if sorted_hand[3] == sorted_hand[4] - 1:
                    return True
    return False
    
def check_for_duplicates(hand):
    sorted_hand = get_values(hand)
    paired_vals = []
    alone_vals = []
    for entry in sorted_hand:
        if sorted_hand.count(entry) == 1:
            alone_vals.append(entry)
        else:
            paired_vals.append(entry)
    
    # for four of a kind, returns a tuple with 4-count card followed by high card
    if len(paired_vals) == 4 and paired_vals[0] == paired_vals[3]:
        return ('four of a kind', [paired_vals[0]], alone_vals)
    
    # for two pairs, returns a tuple of each pair and high card
    elif len(paired_vals) == 4:
        return ('two pairs', [max(paired_vals)], [min(paired_vals)], alone_vals)
    
    # for full house, returns a tuple with 3-count card then 2-count card
    elif len(paired_vals) == 5:
        if paired_vals[2] == paired_vals[0]:
            return ('full house', [paired_vals[2]], paired_vals[4])
        else:
            return ('full house', [paired_vals[2]], paired_vals[0])
            
    # for three of a kind, return a tuple with 3-count cards, then high cards
    elif len(paired_vals) == 3:
        alone_vals.reverse()
        return ('three of a kind', [paired_vals[0]], alone_vals)
    
    # for one pair, returns a tuple with paired value then descending cards
    elif len(paired_vals) == 2:
        alone_vals.reverse()
        return ('one pair', [paired_vals[0]], alone_vals)
    
    # for high card, returns cards in a list in descending order
    else:
        alone_vals.reverse()
        return ('high card', alone_vals)


def hand_value(hand):
    if check_for_flush(hand) == True and check_for_straight(hand) == True:
        return ('straight flush', max(get_values(hand)))
    elif check_for_duplicates(hand)[0] == 'four of a kind':
        return check_for_duplicates(hand)
    elif check_for_duplicates(hand)[0] == 'full house':
        return check_for_duplicates(hand)
    elif check_for_flush(hand) == True:
        sorted_hand = get_values(hand)
        sorted_hand.reverse()
        return ('flush', sorted_hand)
    elif check_for_straight(hand) == True:
        sorted_hand = get_values(hand)
        sorted_hand.reverse()
        return ('straight', sorted_hand)
    else:
        return check_for_duplicates(hand)
        
player1_win_counter = 0
player2_win_counter = 0
tie_breakers = 0
for ind in range(0,len(player1_hands)):
    #checks hand values without tie-breakers first
    if RANKED_HANDS[hand_value(player1_hands[ind])[0]] > RANKED_HANDS[hand_value(player2_hands[ind])[0]]:
        player1_win_counter += 1
    elif RANKED_HANDS[hand_value(player2_hands[ind])[0]] > RANKED_HANDS[hand_value(player1_hands[ind])[0]]:
        player2_win_counter += 1
    else: 
    #checks the second value in the hand_value function, either high card for a straight or paired value for a duplicate
        if hand_value(player1_hands[ind])[1][0] > hand_value(player2_hands[ind])[1][0]:
            player1_win_counter += 1
        elif hand_value(player2_hands[ind])[1][0] > hand_value(player1_hands[ind])[1][0]:
            player2_win_counter += 1
        else: 
    #checks the third value in the hand_value function, looking for high card not part of a pair or straight
            if hand_value(player1_hands[ind])[2][0] > hand_value(player2_hands[ind])[2][0]:
                player1_win_counter += 1
            else:
                player2_win_counter += 1

print player1_win_counter
print player2_win_counter
print tie_breakers






    
    
    
    
    
    
    