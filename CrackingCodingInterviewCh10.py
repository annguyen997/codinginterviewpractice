
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