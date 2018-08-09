'''
Exercise05 - DeckOfCards Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import random

deck = []
for i in range(0, 52):
    deck.append(i)
random.shuffle(deck)
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for i in range(5):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print(suit, rank)
