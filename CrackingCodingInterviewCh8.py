
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 8 - Recursion and Dynamic Programming'''

# 8.1 - Triple Step
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def runStairsCounts(n): 
	#Base cases
	if (n < 0):
		return 0
	elif (n == 0): 
		return 1 
	else: 
		runStairsCounts(n-1) + runStairsCounts(n-2) + runStairsCounts(n-3) 

#Memoization
def runStairsCounts(n): 
	listMemory = [] #n+1 slots
	return runStairsCountsMemo(n, listMemory)

def runStairsCountsMemo(n, listMemory): 
	
	#Base cases
	if (n < 0):
		return 0
	elif (n == 0): 
		return 1 
	elif (listMemory[n] > -1): 
		return listMemory[n]
	else: 
		listMemory[n] = runStairsCountsMemo(n-1, listMemory) + runStairsCountsMemo(n-2, listMemory) + runStairsCountsMemo(n-3, listMemory) 

		return listMemory[n]

# 8.2 - Robots in a Grid


# 8.3 - Magic Index
# A magic index in an array A[0 ... n-1] is defined to be an index such that A[i] = i. 
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A. 


# 8.4 - Power Set
# Write a method to return all subsets of a set. 

#Assume the set is a list for the code simplicity. 
def getSubsets(set): 
	subSets = [] 

	if len(set) == 0: 
		return None

	if len(set) == 1: 
		subSets.add([set[0], None]) 



