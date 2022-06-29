
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

def groupAnagrams(array): 
    pass    


def sortString(string1): 
    stringSorted = sorted(list(string1))
    string1 = str(stringSorted)

    return string1

# 10.3 - Search in Rotated Array
# Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in an array. 
# You may assume that the array was originally sorted in increasing order. 

# 10.4 - Sorted Search, No Size

