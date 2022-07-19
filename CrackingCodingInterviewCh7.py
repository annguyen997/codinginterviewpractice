
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 7 - Object-Oriented Design'''

from abc import abstractmethod, abstractproperty
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

# Assumptions: 
# 1) Parking lot has multiple levels.
# 2) Parking lot can park only motorcycles, cars, and buses
# 3) Parking lot has parking slots for motorcycles, cars, and buses (thus compact and large spots) 
# 4) A motorcycle can park at any spot.
# 5) Cars can park at compact and large spots only. 
# 6) Buses can park at only large spots. 

class VehicleSize(enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3

class Vehicle:
    def __init__(self, spotsNeeded = None, size = None):
        self.parkingSpots = []
        self.licensePlate = None
        self.spotsNeeded = spotsNeeded
        self.size = size

    def getSpotsNeeded(self): 
        return self.spotsNeeded
    
    def getVehicleSize(self):
        return self.size
    
    def parkInSpot(self, parkingSpot): 
        self.parkingSpots.add(parkingSpot)
    
    def clearSpots(self): 
        pass 

    @abstractmethod
    def canFitInSpot(self): 
        pass

class Bus(Vehicle): 
    def __init__(self, spotsNeeded = 5, size = VehicleSize.LARGE):
        super(spotsNeeded, size)
    
    def canFitInSpot(self, parkingSpot): 
        if (parkingSpot.size == VehicleSize.LARGE): 
            return True 
        return False 

class Car(Vehicle):
    def __init__(self, spotsNeeded = 1, size = VehicleSize.COMPACT): 
        super(spotsNeeded, size)
    
    def canFitInSpot(self, parkingSpot): 
        if (parkingSpot.size == VehicleSize.COMPACT): 
            return True 
        return False 

class Motorcycle(Vehicle):
    def __init__(self, spotsNeeded = 1, size = VehicleSize.MOTORCYCLE): 
        super(spotsNeeded, size)
    
    def canFitInSpot(self, parkingSpot): 
        if (parkingSpot.size == VehicleSize.MOTORCYCLE): 
            return True 
        return False 

class ParkingLot: 
    NUM_LEVELS = 5   # Assumption

    def __init__(self):
        levels = [] 
    
    def parkVehicle(vehicle): 
        pass 

class Level: 

    SPOTS_PER_ROW = 10  # Assumption

    def __init__(self, level):
        self.level = level
        self.spots = [] 
        self.availableSpots = 0

    def availableSpots(self): 
        return self.availableSpots
    
    def parkVehicle(self, vehicle): 
        pass 

    def parkVehicleAtSpot(self, vehicle, spot): 
        pass 

    def findAvailableSpots(self, vehicle): 
        pass

    def spotFreed(self): 
        self.availableSpots += 1

class ParkingSpot: 
    def __init__(self, spotSize, row, spotNumber, level): 
        self.spotSize = spotSize
        self.row = row
        self.spotNumber = spotNumber
        self.level = level
        self.vehicle = None
    
    def isAvailable(self): 
        return self.vehicle == None
    
    def canFitVehicle(self, vehicle): 
        pass

    def park(self, vehicle): 
        pass

    def getRow(self):
        return self.row

    def getSpotNumber(self):
        return self.spotNumber

    def removeVehicle(self): 
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle 
    

# 7.5 - Online Book Reader
# Design the data structures for an online book reader system. 

# Assumptions: 
# 1) System has user membership creation/extension; search for books (in database); reading the book; 
# 2) System Constraints: Only one active user at a time; only one active book at a time. 

class User:
    def __init__(self, id, details, accountType): 
        self.userID = id
        self.details = details
        self.accountType = accountType

    def renewMembership(self): 
        pass


class Book:
    def __init__(self, id, details): 
        self.bookId = id
        self.details = details
    
    def getID(self):
        return self.bookId
    
    def setID(self, id): 
        self.bookId = id
    
    def getDetails(self): 
        return self.details

    def setDetails(self, details): 
        self.details = details    

class Library:
    def __init___(self): 
        self.books = {}
    
    def addBook(self, id, details): 
        if (self.books.get(id)): 
            return None 
        
        book = Book(id, details)
        self.books[id] = book
        return book

    def find(self, id): 
        return self.books.get(id) 
    
    def removeBook(self, id): 
        if not (self.books[id]): 
            return False

        book = self.books[id]
        del self.books[id]
        return book
    
    def removeBook(self, book): 
        return self.removeBook(book.getID())

class Display:
    def __init__(self): 
        self.activeBook = None
        self.activeUser = None
        self.__pageNumber = None

    def displayUser(self, user): 
        self.activeUser = user
        self.refreshUsername() 
    
    def displayBook(self, book): 
        self.activeBook = book
        self.__pageNumber = 0

        self.refreshTitle() 
        self.refreshDetails()
        self.refreshPage() 
    
    def turnPageForward(self): 
        self.__pageNumber += 1 
        self.refreshPage()
    
    def turnPageBackward(self): 
        self.__pageNumber -= 1 
        self.refreshPage()

class UserManager: 
    def __init__(self): 
        self.users = {} 

    def addUser(self, id, details, accountType): 
        if (self.users.get(id)): 
            return False
        
        user = User(id, details, accountType)
        self.users[id] = user
        return user
    
    def findUser(self, id): 
        return self.users.get(id) 
    
    def removeUser(self, user):
        return self.removeUser(user.getID())
    
    def removeUser(self, id): 
        if not (self.users.get(id)): 
            return False
        
        user = self.users.get(id)
        del self.users.get(id)
        return user

class OnlineReaderSystem:
    def __init__(self): 
        self.library = Library()
        self.userManager = UserManager() 
        self.display = Display()
        self.activeBook = None
        self.activeUser = None
    
    def getActiveBook(self): 
        return self.activeBook
    
    def setActiveBook(self, book): 
        self.activeBook = book
        self.display.displayBook(book)
    
    def setActiveUser(self, user): 
        self.ActiveUser = user
        self.display.displayUser(user) 
    
# 7.6 - Jigsaw
# Implement an NxN jigsaw puzzle. 
# Design the data structures and explain an algorithm to solve the puzzle. 
# You can assume that you have a fitsWith() method which, when passed two puzzle edges, returns True if the two edges become together. 

# Assumptions
# 1) Use the absolute position (that is, using row and column). 

class Orientation(enum): 
    LEFT = 0 
    TOP = 1
    RIGHT = 2
    BOTTOM = 3

    def getOpposite(self, orientation): 
        if orientation == Orientation.LEFT: 
            return Orientation.RIGHT
        elif orientation == Orientation.RIGHT: 
            return Orientation.LEFT
        elif orientation == Orientation.TOP: 
            return Orientation.BOTTOM
        elif orientation == Orientation.BOTTOM: 
            return Orientation.TOP 
        else: 
            return None

class Shape(enum): 
    INNER = 0 
    OUTER = 1
    FLAT = 2

    def getOpposite(self, orientation): 
        if orientation == Shape.INNER: 
            return Shape.OUTER
        elif orientation == Shape.OUTER: 
            return Shape.INNER 
        else: 
            return None

class Puzzle: 
    

