
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 7 - Object-Oriented Design'''

import enum

# 7.1 - Deck of Cards
# Design the data structures for a generic deck of cards. 
# Explain how you would subclass the data structures to implement blackjack. 

# For this problem, this card deck assumes a 52-card standard deck. 
class Suit(enum.Enum): 
    Club = 0 
    Diamond = 1
    Heart = 2
    Spade = 3

    def __init__(self, value): 
        self.value = value

    def getValue(self):
        return self.value
    


class Card: 
    def __init__(self, suit, value): 
        self.suit = suit
        self.value = value #Ace, 2-10, Jack, Queen, King
        self.__availability = True 
    
    @abstractmethod 
    def getValue(self): pass
    
    def getSuit(self): 
        return self.suit 
    
    def isAvailable(self): 
        return self.__availability
    
    def markUnavailable(self): 
        self.__availability = False
    
    def markAvailable(self):
        self.__availability = True

class Deck(Card): 
    def __init__(self): 
        super.__init__()
        self.deck = []
        self.__dealtIndex = 0 

    def setDeckOfCards(self): pass

    def shuffle(self): pass

    def remainingCards(self):
        return len(self.deck) - self.__dealtIndex

    def dealHand(self): pass

    def dealCard(self): pass 


class Hand(Card): 
    def __init(self): 
        super.__init__()
        self.cards = []
    
    def score(self): 
        score = 0 
        for card in self.cards: 
            score += card.getValue() 
        
        return score 
    
    def addCard(self, card): 
        self.cards.add(card) 

class BlackJackCard(Card): 

    def __init__(self, suit, value): 
        super.__init__(suit, value) 

    def getValue(self): 
        if self.isAce(): 
            return 1
        elif (self.isFaceCard()): 
            return 10
        else: 
            return self.value
    
    def minValue(self): 
        if self.isAce(): 
            return 1
        return self.getValue() 
    
    def maxValue(self):
        if self.isAce(): 
            return 11
        return self.getValue() 

    def isAce(self):
        return self.value == 1 
    
    def isFaceCard(self):
        return self.value >= 11 and self.value <= 13

class BlackJackHand(Hand): 
    def score(self): 
        scores





