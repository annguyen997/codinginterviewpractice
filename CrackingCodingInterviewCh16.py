
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 16 - Moderate'''

# 16.1 - Number Swapper
# Write a function to swap a number in place (that is, without temporary variables)
from telnetlib import XASCII


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

# 16.3 - Intersection 
# Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any. 
class Point: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y 
    
    def setLocation(self, x, y): 
        self.x = x
        self.y = y

class Line: 
    def __init__(self, start, end): 
        deltaY = end.y - start.y
        deltaX = end.x - start.x

        self.slope = deltaY / deltaX   #If deltaX == 0, this will be infinity not zero 
        self.yIntercept = end.y - (self.slope * end.x)

def checkIntersection(start1, end1, start2, end2): 
    # Rearrange these so that, in order of x values, start is before end and point 1 is before point 2, if needed for easier logic. 
    if (start1.x > end1.x): 
        swap(start1, end1)
    if (start2.x > end2.x): 
        swap(start2, end2)
    if (start1.x > start2.x): 
        swap(start1, start2)
        swap(end1, end2)

    # Compute the lines to calculate y-intercept and slope
    line1 = Line(start1, end1)
    line2 = Line(start2, end2) 

    # If lines 1 and 2 have the same slope
    if (line1.slope == line2.slope): 

        # If the lines have the same y intercept (i.e. same line) and coordinate of start2 is between start1 and end1 (i.e. line 2 begins somewhere on line 1)
        if (line1.yIntercept == line2.yIntercept and isBetween(start1, start2, end1)): 
            return start2

        # The lines do not intersect at a common point at any time
        return None 
    
    # If lines 1 and 2 have different slopes
    x = (line2.yIntercept - line1.yIntercept) / (line1.slope - line2.slope)
    y = (x * line1.slope + line1.yIntercept)

    intersection = Point(x, y)

    # Check if the intersection point is within line segment range of the two lines
    if (isBetweenPoints(start1, intersection, end1) and isBetweenPoints(start2, intersection, end2)): 
        return intersection
    else: 
        return None  # Invalid intersection 

def swap(one, two): 
    x = one.x
    y = one.y

    one.setLocation(two.x, two.y)
    two.setLocation(x, y)

def isBetween(start, middle, end): 
    if (start > end): 
        return end <= middle and middle <= start
    else: 
        return start <= middle and middle <= end

def isBetweenPoints(start, middle, end): 
    return isBetween(start.x, middle.x, end.x) and isBetween(start.y, middle.y, end.y)



#  16.17 - Contiguous Sequences
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