#!/usr/bin/env python3

# demo.py
# Demonstrate some of the uses of the cards module
import cards

if __name__=="__main__":
    #Create a deck
    d=cards.createDeck()

    #Shuffle it
    d=cards.shuffle(d)
    print("Deck contains:", d)
    print()
    
    #Draw a five-card hand
    h=cards.deal(d,5)
    print("Deck now contains: ",d)
    print()
    print("Hand contains: ",h)
    
    
