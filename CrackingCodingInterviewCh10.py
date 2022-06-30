
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

