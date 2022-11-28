#!/usr/bin/env python3
# cards.py
# Collection of tools for simulating a deck of cards
import random

def createDeck():
    """ Create a new standard deck and return it.
    
    TODO:

     * Add arguments allowing non-standard decks
    """
    deck=[]

    # Suits and numbers to iterate over
    suits=["♥","♠","♦","♣"]
    numbers=["A","2","3","4","5","6","7","8","9","10","11","J","Q","K"]

    
    for suit in suits:
        for number in numbers:
            deck.append(number+suit)
    return deck



# Note the addition of a type in the argument list below. It is not
# used by the interpreter, but is good documentation and can be used
# by source analysis tools.

def shuffle(deck:list):
    """ Creates and returns a shuffled equivalent of the given deck 

    Arguments:

     * deck: a list of cards

    """
    newDeck=deck.copy()
    random.shuffle(newDeck)
    return newDeck

def deal(deck:list, handSize:int):
    """ Take the top cards from the deck and return them as a "hand". The deck is modified by this function. 

    Arguments:

     - deck: the deck to draw from
     - handSize: number of cards to draw into the returned hand
    """
    
    hand=[]
    while len(hand)<handSize:
        hand.append(deck.pop(0))
    return hand
def flip(deck:list):
    c = deal(deck,1)
    return c[0]
d=cards.flip(d)
    print("Deck contains:", d)
    print()

    
# Challenge: Create a new function called "flip" that returns the top
# card from a deck. The deck should be modified by this action. Make
# sure to document your function!
