
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 16 - Moderate'''

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