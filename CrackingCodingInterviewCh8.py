
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 8 - Recursion and Dynamic Programming'''

# 8.1 - Triple Step
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

from ast import Set


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
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
# The robot can only move in two directions, right and down. 
# There are certain cells that are "off limits" such that robot cannot step on them. 
# Design an algorithm to find a path for the robot from the top left to the bottom right. 

class Point: 
	def __init__(self, row, column): 
		self.row = row
		self.column = column 

def getPath(maze): 
	#Base case 
	if (maze == None) or (len(maze) == 0): 
		return None

	path = []
	failedPoints = set() 
	if (getPath(maze, len(maze) - 1, len(maze[0]) - 1, path, failedPoints)):
		return path 
	return None


def getPath(maze, row, column, path, failedPoints):
	# If a cell is not available/out of bounds or column/row < 0 (i.e. out of bounds), return False
	if (column < 0) or (row < 0) or not (maze[row][column]): 
		return False

	currentPoint = Point(row, column) 

	# Check if the current point is failed point (that is this cell is already visited and not allowed)
	if (currentPoint in failedPoints):
		return False 

	# Check if the cell is at the upper-left corner of the maze. 
	isAtOrigin = (row == 0) and (column == 0) 

	if (isAtOrigin) or (getPath(maze, row, column - 1, path, failedPoints)) or (getPath(maze, row - 1, column, maze, failedPoints)):
		#point = Point(row, column)
		path.append(currentPoint)
		return True
	
	# Cache current point
	failedPoints.add(currentPoint)

	return False 
	


# 8.3 - Magic Index
# A magic index in an array A[0 ... n-1] is defined to be an index such that A[i] = i. 
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A. 


# 8.4 - Power Set
# Write a method to return all subsets of a set. 

# Assume the set is a list for the code simplicity. 
def getSubsets(set, index): 
	allSubsets = [] 

	#Base case
	if (len(set) == index): 
		allSubsets.append([]) #Empty set 
	else: 
		allSubsets = getSubsets(set, index+1)
		item = set[index]

		moreSubsets = [] 
		for subset in allSubsets: 
			newSubset = []
			newSubset.append(subset)
			newSubset.append(item)
			moreSubsets.append(newSubset)
		
		allSubsets.append(moreSubsets) 

	return allSubsets

# 8.5 - Recursive Multiply
# Write a recursive function to multiply two positive integers without using the * operator (or / operator). 
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations. 

def minProduct(a, b): 
	smaller = a if a < b else b
	larger = b if a < b else a

	memo = []
	return minProductHelper(smaller, larger, memo)

def minProductHelper(smaller, larger, memo): 

	# Check if one of the integers are zero or one.
	# By definition n * 0 = 0; n * 1 = n 
	if (smaller == 0): 
		return 0 
	elif (smaller == 1): 
		return larger
	#If the value has been calculated already, return that number
	elif (memo[smaller] > 0): 
		return memo[smaller]

	# Compute half. If uneven, compute other half. If even, double it. 
	half = smaller / 2
	side1 = minProductHelper(half, larger, memo)
	#side2 = side1 

	if (smaller % 2 == 1): 
		#side2 = minProductHelper(smaller - half, larger, memo)
		side2 = side1 + side1 + larger
	else: 
		side2 = side1 + side1
	
	#Cache the results
	#memo[smaller] = side1 + side2

	#return memo[smaller]
	return side2

	



