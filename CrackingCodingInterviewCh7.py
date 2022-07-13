
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 7 - Object-Oriented Design'''

from abc import abstractmethod
import enum
from os import system
from this import d

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
        scores = possibleScores() 
        maxUnder = system.min
        minOver = system.max 

        for score in scores: 
            if (score > 21 and score < minOver): 
                minOver = score
            elif (score <= 21 and score > maxUnder): 
                maxUnder = score
        
        return minOver if maxUnder == system.min else maxUnder


# 7.2 - Call Center
# Imagine you have a call center with three levels of employees: respondent, manager, and director. 
#
# An incoming telephone call must be first allocated to a respondent who is free. 
# If the respondent cannot handle the call, he/she must escalate the call to a manager. 
# If the manager is not free or not able to handle it, then the cal should be escalated to a director. 
#
# Design the classes and data structures for this problem. 
# Implement a method dispatchCall() which assigns a call to the first available employee. 

class Employee:
    #This class is an abstract class
    
    def __init__(self, rank, name): 
        self.rank = rank
        self.name = name
        self.currentCall = None
        self.available = True

    def setAvailable(self): 
        self.available = True
    
    def setUnavailable(self):
        self.available = False 
    
    def getRank(self): 
        return self.rank 

    # Check if the employee is available to take a call 
    def isFree(self): 
        return self.available

    # Start the conversation
    @abstractmethod
    def receiveCall(self, call):
        self.currentCall = call
    
    # End the conversation; end the call
    @abstractmethod
    def endCall(self): 
        self.currentCall = None

    # Issue not yet resolved, escalate call and assign new call to employee if any
    @abstractmethod
    def escalateCall(self): 
        pass

    # Assign a new call to an employee if employee is free
    @abstractmethod
    def assignNewCall(self):
        pass

class Respondent(Employee):
    def __init__(self, rank, name, manager):
        self.super(rank, name) 
        self.manager = manager
    
    def escalateCall(self):
        if self.manager.isFree(): 
            self.manager.assignNewCall()

class Manager(Employee): 
    def __init__(self, rank, name, director): 
        self.super(rank, name)
        self.director = director 

class Director(Employee): 
    def __init__(self, rank, name): 
        self.super(rank, name)

class Call: 
    def __init__(self, caller): 
        self.caller = caller    # Name of the person who is calling
        self.handler = None     # Name of employee who can respond to the call
        self.rank = None        # Get the rank of the employee who is handling the call
    
    def setEmployee(self, employee):
        self.handler = employee
    
    def reply(self, message): 
        pass

    def getRank(self):
        return self.rank
     
    def setRank(self, rank):
        self.rank = rank 

    def incrementRank(self):
        pass

    def disconnect(self):
        self.handler.endCall()
        self.handler = None
        self.rank = None

class CallHandler: 
    LEVELS = 3

    NUM_RESPONDENTS = 10
    NUM_MANAGERS = 5
    NUM_DIRECTORS = 2

    def __init__(self):
        self.employeeLevels = [
            [0]*CallHandler.NUM_RESPONDENTS,
            [0]*CallHandler.NUM_MANAGERS,
            [0]*CallHandler.NUM_DIRECTORS 
        ]
        self.callQueue = [] 

    def dispatchCall(self, caller): 
        call = caller
        self.dispatchCall(call) 
    
    def dispatchCall(self, call):
        # Route call to employee with minimal rank 
        callerFound = False 

        for employee in self.employeeLevels[0]: 
            if (employee != None) and (employee.isFree()):
                employee.receiveCall(call)
                call.setEmployee(employee)
                callerFound = True
        
        if not callerFound: 
            self.callerQueue.append(call)
    
    def assignCall(self, employee): 
        pass

# 7.3 - Jukebox
# Design a musical jukebox using object-oriented principles.      

# Assume this jukebox is virtual, but has the components that you will find in a physical jukebox. 
# Assume this jukebox is free to use; no payment required. No currencies or change required. 

class Jukebox: 
    def __init__(self): 
        self.cdPlayer = None
        self.user = None
        self.cdCollection = [] 
        self.songSelector = None

    def getCurrentSong(self):
        return self.songSelector.getcurrentSong()
    
    def setUser(self, user):
        self.user = user
    
    def setCDPlayer(self, cdPlayer):
        self.cdPlayer = cdPlayer
    
class CDPlayer: 
    def __init__(self, playlist = None, cd = None): 
        self.cd = cd
        self.playlist = playlist
    
    def setPlaylist(self, playlist):
        self.playlist = playlist
    
    def setCD(self, cd):
        self.cd = cd
    
    def getPlaylist(self): 
        return self.playlist
    
    def getCD(self):
        return self.cd 
    
    def playSong(song):
        pass 

class Playlist: 
    def __init__(self): 
        self.songsQueue = [] 
        self.song = None
    
    def getNextSongToPlay(self): 
        return self.songsQueue.peek() 
    
    def queueUpSong(self, song): 
        self.songsQueue.add(song)

class Song: 
    def getArtist(self): 
        pass

    def getSongName(self):
        pass

class CD:
    pass

class JukePlayer: 
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

# 7.4 - Parking Lot
# Design a parking lot using object-oriented principles. 




