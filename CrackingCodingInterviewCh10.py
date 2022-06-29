
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

    

        
    
