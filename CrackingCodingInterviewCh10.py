
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 10 - Sorting and Searching'''

# 10.1 - Sorted Merge
# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
# Write a method to merge B into A in sorted order. 

def sortMergeTwoArrays(arrayA, arrayB): 
    if (arrayA == None): 
        return None
    
    indexA = len(arrayA) - 1
    indexB = len(arrayB) - 1
    mergeIndex = indexA + indexB - 1 

    while (indexB >= 0): 
        #Note end of index A is less than the end of index B 
        if (indexA >= 0) and (arrayA[indexA] > arrayB[indexB]):
            arrayA[mergeIndex] = arrayA[indexA]
            indexA -= 1
        else: 
            #If arrayA < arrayB, copy number from index B 
            arrayA[mergeIndex] = arrayB[indexB]
            indexB -= 1  

        mergeIndex -= 1
        
    return arrayA 

# 10.2 - Group Anagrams
# Write a method to sort an array of strings so that all the anagrams are next to each other. 

def groupAnagrams(stringsList):

    anagramDictionary = {}

    #Go through each item in the array, and sort the characters in string
    for item in stringsList: 
        string = sortString(item)
        
        #If there is already the sorted string in dictionary, add item to existing list (i.e. anagram found)
        if string in anagramDictionary: 
            itemList = anagramDictionary[string]
            itemList.append(item) 
            anagramDictionary[string] = itemList
        else: 
            anagramDictionary[string] = [item] 

    index = 0
    for key in anagramDictionary: 
        itemList = anagramDictionary[key]
        for item in itemList:
            stringsList[index] = item
    
    return stringsList

def sortString(string1): 
    stringSorted = sorted(list(string1))
    string1 = str(stringSorted)

    return string1

# 10.3 - Search in Rotated Array
# Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in an array. 
# You may assume that the array was originally sorted in increasing order. 

# Example: 
# Input: Find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# Output: 8 (Index of number 5 in the array)

def searchRotatedArray(array, number, left, right):
    middle = (left + right) / 2 
    
    if (array[middle] == number):
        return middle
    
    if (right < left):
        return -1
    
    if (array[left] < array[middle]):
        if (number >= array[left]) and (number < array[middle]): 
            searchRotatedArray(array, number, left, middle - 1) 
        else:
            searchRotatedArray(array, number, middle + 1, right)

    elif (array[middle] < array[left]): 
        if (number >= array[middle]) and (number < array[right]): 
            searchRotatedArray(array, number, middle + 1, right)
        else: 
            searchRotatedArray(array, number, left, middle - 1)

    elif (array[left] == array[middle]): 
        if (array[middle] != array[right]):
            searchRotatedArray(array, number, middle + 1, right) 
        else: 
	        #Need to search both halves
            result = searchRotatedArray(array, number, left, middle - 1)
            if not result: 
                return searchRotatedArray(array, number, middle + 1, right) 
            else: 
                return result
    
    return -1 

# 10.4 - Sorted Search, No Size
# You are given an array-like data structure Listy which lacks a size method. 
# It does, however, have an elementAt(i) method that returns the element at index i in O(1) time.
# If i is beyond the bounds of the data structure, it returns -1. For this reason, the data structure only supports positive integers. 
# Give a Listy which contains sorted, positive integers, find the index at which an element x occurs. 
# If x occurs multiple times, you may return any index.  

def searchWithNoSize(list, element): 
	#Double the index by two until reach end of bounds of data structure
	index = 1
	while (list[index] != -1) and (list.elementAt(index) < element) : 
		index *= 2 

	return binarySearchMod1(list, element, index / 2, index)

def binarySearchMod1(list, element, low, high):
    while (low <= high):
        mid = low + high / 2

        if (list[mid] == element): 
            return mid 

        elif (list[mid] < element): 
            low = mid + 1

        elif (list[mid] > element) or (list[mid] == -1): 
            high = mid - 1
    
    return -1

# 10.5 - Sparse Search
# Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string. 

#This assumes the strings in the array follow ASCII order
def sparseSearch(array, string): 
    
    #Edge cases
    if (array == None) or (string == None) or (string == ""): 
        return -1 

    low = 0
    high = len(array) - 1
    mid = low + high / 2 

    while (low < high): 
        #If the midpoint is the given string, return the index
        if (array[mid] == string): 
            return mid 

        #If not, check if the midpoint is an empty string: 
        if (array[mid] == ""):

            #Find the clostest index with a non-empty string.
            left = mid - 1
            right = mid + 1

            while (True): 
                if (left < low) and (right > high): 
                    return -1
                elif (right <= high) and (array[right] != ""): 
                    mid = right
                    break 
                elif (left >= low) and (array[left] != ""): 
                    mid = left
                    break
                
                right += 1
                left -= 1

        if (array[mid] < string):
            low = mid + 1
        else: 
            high = mid - 1
    
    return -1

# 10.6 - Sort Big File
# Imagine you have a 20 GB file with one string per line. 
# Explain how you would sort the file. 

""" Sorting a file of 20 GB would result in possible memory overflow, crashing the program.

The mechanism to sort a big file is to partition the file into chunks of "x" number of memory. 
Each partition would then be sorted separately, using merge sort. Save each file separately into file system.

Using the file system, merge the files - one by one. Use the larger file as a reference spot; sort using the smaller file.

"""

# 10.7 - Missing Int
# Given an input file with four billion non-negative integers, provide an algorithm to generate an integer that is not contained in the file.
# Assume you have 1 GB of memory available for this task. 

# FOLLOW-UP: What if you have only 10 MB of memory. 
# Assume that all the values are distinct and we now have no more than one billion non-negative integers. 

# This solution assumes the numbers are all integers, and some integers may repeat. 


# 10.8 - Find Duplicates
# You have an array with all the numbers from 1 to N, where N is at most 32,000. 
# The array may have duplicate entries, and you do not know what N is. 
# With only 4 KB of memory available, how would you print all duplicates elements in the array? 

# Constraints: N in range 1 - 32,000; duplicates permitted 

def findDuplicates(list): 

    bs = BitVector(len(list))

    for i in range(len(list)): 
        number = list[i] 
        numBit = number - 1  #Recall number N is in range 1-32K; bits start at 0
        if (bs.get(numBit)): 
            print(number) 
        else: 
            bs.set(numBit) 
    

# This solution assumes defining a BitVector class. 
class BitVector: 
    
    def __init__(self, size): 
        self.bitSet = [0] * size
    
    def get(self, pos): 
        wordNumber = (pos >> 5) #Divide by 32
        bitNumber = (pos & 0x1F) #Modular by 32

        return (self.bitSet[wordNumber] and (1 << bitNumber)) != 0

    def set(self, pos): 
        wordNumber = (pos >> 5)
        bitNumber = (pos & 0x1F) 
        self.bitSet[wordNumber] |= 1 << bitNumber

# 10.9 - Sorted Matrix Search
# Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

# 10.10 - Rank from Stream
# Imagine you are reading in a stream of integers. 
# Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x). 
# Implement the data structures and algorithms to support these operations. 
#   - Implement the track(int x) method, which is called when each number is generated. 
#   - Implement the getRankOfNumber(int x) method, which returns the number of values <= x (not including x itself). 

# This solution cannot assume the binary tree will be balanced. If unbalanced, the runtime is O(N). Best case is O(log N) 
class RankNode: 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        self.left_size = 0 
    
    def insert(self, number): 
        if (number < self.data):
            if (self.left != None): 
                self.left.insert(number)
            else: 
                self.left = RankNode(number)
            self.left_size += 1
        else: 
            if (self.right != None): 
                self.right.insert(number) 
            else: 
                self.right = RankNode(number) 
    
    def getRank(self, number):
        if (number == self.data):
            return self.left_size
        elif (number < self.data):
            if (self.left == None): 
                return -1
            return self.left.getRank(number)
        elif (number > self.data):
            if (self.right == None): 
                return -1
            return self.left_size + 1 + self.right.getRank(number) 
            
class BinaryTreeRank: 
    def __init__(self, root = None):
        self.root = root
    
    def insertNum(self, number): 
        if (self.root == None): 
            self.root = RankNode(number)
        else: 
            self.root.insert(number) 

    def getRankOfNumber(self, number):
        return self.root.getRank(number)

    def track(self, number): 
        if (self.root == None): 
            self.root = RankNode(number)
        else: 
            self.root.insert(number)

# 10.11 - Peaks and Valleys
# In an array of integers: 
# A "peak" is an element which is greater than or equal to the adjacen integers. 
# A "valley" is an element which is less than or equal to the adjacent integers. 
# EXAMPLE: In array [5, 8, 6, 2, 3, 4, 6]: {8, 6 (the second)} are peaks, and {5, 2} are valleys. 

# Given an array of integers, sort the array into an alternating sequence of peaks and valleys 