
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 16 - Moderate'''

# 16.1 - Number Swapper
# Write a function to swap a number in place (that is, without temporary variables)
def swapNumber(): 
    pass

# 16.2 - Word Frequencies
# Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times? 

# Single query version - O(N)
def getFrequency(book, word): 
    word = word.strip().lower()
    count = 0 

    for w in book:
        if w == word:
            count += 1
    
    return count

# Repetitive query version - O(1) 
def setDictionary(book): 
    table = {}
    for word in book:
        word = word.lower() 
        
        if word.strip() == "": 
            continue 

        if word.strip() in table: 
            table[word] = table.get(word) + 1
        else: 
            table[word] = 1
    
    return table

def getFrequency(table, word):
    if (table == None) or (word == None): 
        return -1
    
    word = word.strip().lower()
    
    if word in table: 
        return table.get(word) 
    
    return 0

# 16.17 - Contiguous Sequences
# You are given an array of integers (both positive and negative). 
# Find the contiguous sequence with the largest sum. Return the sum. 
# 
# EXAMPLE: 
# Input: 2, -8, 3, -2, 4, -10
# Output: 5 (i.e. {3, -2, 4})

def getMaxSum(nums): 
    maxSum = 0 
    sum = 0 

    # Loop through the array to find maximum sum 
    for i in range(len(nums)): 
        sum += nums[i]
        
        # If the updated sum means maxSum < sum
        if (maxSum < sum): 
            maxSum = sum 
        # If adding the number results in a negative number, reset sum to zero
        elif (sum < 0): 
            sum = 0
    
    # If maximum sum is zero, return the highest negative value 
    if (maxSum == 0):
        leastNegative = None
        for i in range(len(nums)): 
            # If least negative number is None or a higher negative value found, report
            if (leastNegative == None) or (leastNegative < nums[i]): 
                leastNegative = nums[i]
        
        return leastNegative
        
    return maxSum 