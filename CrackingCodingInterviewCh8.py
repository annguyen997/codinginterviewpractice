
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 8 - Recursion and Dynamic Programming'''

# 8.1 - Triple Step
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

from ast import Set
from operator import index
import re

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

# FOLLOW-UP: What if the values are not distinct? 

"""Brute Force Algorithm"""
def magicIndexBruteForce(array): 
	for i in range(len(array)): 
		if (array[i] == i):
			return i 
	
	return -1

"""Optimized Algorithm"""
def magicIndex(array): 
	return magicIndex(array, 0, len(array)-1)

def magicIndex(array, start, end): 
	mid = (start + end) / 2

	while (start < end):
		if (array[mid] == mid): 
			return mid
		elif (array[mid] < mid): 
			start = mid + 1
		else: 
			end = mid - 1
	
	return -1

def magicIndex(array, start, end):
	"""
	mid = (start + end) / 2

	while (start < end):
		if (array[mid] == mid): 
			return mid
		elif (array[mid] < mid): 
			start = mid + 1
		else: 
			end = mid - 1
	
	return -1
	"""

	if (end < start): 
		return -1 
	
	mid = (start + end) / 2

	if (array[mid] == mid): 
		return mid
	elif (array[mid] < mid): 
		return magicIndex(array, mid+1, end)
	else: 
		return magicIndex(array, start, mid - 1) 

"""Follow-Up Question"""
def magicIndexFollowUp(array): 
	return magicIndex(array, 0, len(array)-1)

def magicIndexFollowUp(array, start, end):
	if (end < start): 
		return -1 
	
	mid = (start + end) / 2
	midValue = array[mid]

	if (midValue == mid): 
		return mid
	
	# Search left
	leftIndex = min(mid - 1, midValue)
	left = magicIndex(array, start, leftIndex) 

	if (left >= 0): 
		return left 
	
	# Search right
	rightIndex = max(mid + 1, midValue) 
	right = magicIndex(array, rightIndex, end)
	
	return right  #May return index or -1


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

# 8.6 - Towers of Hanoi
# In this classic problem, you have 3 towers and N disks of different sizes which can slide onto any tower. 
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e. each disk sits on top of an even larger one). 
# You have the following constraints: 
# (1) Only one disk can be moved at a time. 
# (2) A disk is slide off the top of one tower onto another disk. 
# (3) A disk cannot be placed on top of a smaller disk. 
# Write a program to move the disks from the first tower to the last using these 3 stacks. 

def towersOfHanoi(): 
	stacks = 3 
	towers = [] 

	# Create the towers
	for i in range(stacks): 
		towers.append(Tower(i))
	
	# Add elements to the tower, starting at the index - 1
	i = stacks - 1 
	while (i >= 0): 
		towers[0].add(i)
		i =- 1
	
	towers[0].moveDisks(stacks, towers[2], towers[1])

# Tower 1 is the origin tower; Tower 2 is the buffer tower; and Tower 3 is the destination tower
# Both Tower 1 and 3 may be using as buffers 
class Tower: 
	def __init__(self, index): 
		self.disks = []
		self.index = index 
	
	def getIndex(self): 
		return self.index
	
	def isEmpty(self): 
		return len(self.disks) == 0
	
	def peek(self): 
		return self.disks[-1]

	def add(self, number): 
		if (not self.isEmpty()) and (self.peek() <= number):
			return
		self.disks.append(number)

	def moveTop(self, stack): 
		element = self.disks.pop()
		stack.add(element)
	
	def moveDisks(self, n, destination, buffer): 
		if (n > 0): 
			# Move top n - 1 disks from origin to buffer (middle tower), using destination as an intermediate 
			self.moveDisks(n-1, buffer, destination)

			# Move n (top most disk at this point) from origin to destination 
			self.moveTop(destination)

			# Move top n - 1 disks from buffer to destination, using origin (first tower) as an intermediate 
			buffer.moveDisks(n-1, destination, self)


# 8.7 - Permutations without Dups
# Write a method to compute all permutations of a string of unique characters. 
"""Builiding permutations based on first n-1 characters"""
def getPerms(string): 

	#Base case of no string
	if (string == None): 
		return None
	
	permutations = [] 

	# Base case
	if (len(string) == 0):   
		permutations.append("")
		return permutations
	
	# Get the character of the first part of string
	first = string[0]
	remainder = string[1:len(string)]
	words = getPerms(remainder) 

	for word in words: 
		# Get the length of the word
		length = len(word) 

		# Index for each part of the word
		for i in range(length): 
			string = insertChar(first, word, i) 
			permutations.append(string) 
	
	return permutations
	
def insertChar(character, word, index): 
	start = word[0:index]
	end = word[index:len(word)]
	return start + character + end 

"""Building Permutations from all (n-1) strings"""
def getPermsAlt(remainder): 

	#Get the length of the remainder string
	length = len(remainder) 
	result = []

	# Base case 
	if (length == 0): 
		result.append("") 
		return result 
	
	# Add remainder string 
	for i in range(length):
		before = remainder[0:i]
		after = remainder[i:len(remainder)]
		partials = getPermsAlt(before + after)

		for word in partials: 
			result.append(remainder[i] + word)
	
	return result 


# 8.8 - Permutation with Dups
# Write a method to compute all permutations of a string whose characters are not necessarily unique. 
# the list of permutations should not have duplicates.

def printPerm(string): 
	result = [] 
	mapping = buildFreqTable(string) 
	printPerm(mapping, "", len(string), result) 
	return result 

def buildFreqTable(string): 
	mapping = {}
	
	for char in string: 
		if char not in mapping:
			mapping[char] = 0

		mapping[char] = mapping.get(char) + 1
	
	return mapping 

# This assumes the result is object by reference
def printPerm(mapping, prefix, remaining, result):

	#Base case
	if (remaining == 0): 
		result.append(prefix)
		return

	keySet = mapping.keys() 
	for character in keySet: 
		count = mapping[character] 

		if (count >= 0): 
			mapping[character] = mapping.get(character) - 1
			printPerm(mapping, prefix + character, remaining - 1, result)
			mapping[character] = count
	
# 8.9 - Parens
# Implement an algorithm to print all valid (i.e. properly opened and closed) combinations of n pairs of parentheses. 

# Example: 
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()

"""Naive Solution"""
def buildParens(number): 
	parenSet = Set() 

	# Base case 
	if (number == 0): 
		parenSet.add("")
	else: 
		prev = buildParens(number - 1)

		for stringParen in prev: 
			for i in range(len(stringParen)): 

				if stringParen[i] == '(': 
					start = stringParen[0:i+1]
					end = stringParen[i+1:len(stringParen)]
					parenSet.add(start + "()" + end)
		
		parenSet.add("()" + stringParen)
	
	return parenSet

# 8.10 - Paint Fill
# Implement the "paint fill" function that one might see on many image editing programs. 
# That is, given a screen (represented by 2D array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color. 

def paintFill(screen, row, column, color): 
	if screen[row][color] == color: 
		return False 

	return paintFill(screen, row, column, screen[row][column], color)

def paintFill(screen, row, column, oldColor, newColor):
	
	# Screen goes out of bounds
	if ((row < 0) or (row >= len(screen))) or ((column < 0) or (column >= len(screen[0]))): 
		return False
	
	if (screen[row][column] == oldColor): 
		# Set the new color
		screen[row][column] == newColor

		# Loop though each of the adjacent cells to change color 
		paintFill(screen, row-1, column, oldColor, newColor) # Up
		paintFill(screen, row+1, column, oldColor, newColor) # Down
		paintFill(screen, row, column-1, oldColor, newColor) # Left
		paintFill(screen, row, column+1, oldColor, newColor) # Right
	
	return True

# 8.11 - Coins
# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent)...
# Write code to calculate the number of ways of representing n cents.

def makeChange(cents): 
	denominations = [25, 10, 5, 1]
	map = [[0]*(cents+1)]*len(denominations)

	return makeChange(cents, denominations, 0, map)

def makeChange(amount, denominations, index, map): 

	# If such cents has already been calculated, return value
	if map[amount][index] > 0: 
		return map[amount][index]

	# If index is higher than length of denominations available, return 1 (past last denomination)
	if (index >= len(denominations) - 1): 
		return 1
	
	ways = 0 
	denomAmount = denominations[index] 

	i = 0
	while (i * denomAmount <= amount): 
		amountRemaining = amount - (i * denomAmount)
		ways += makeChange(amountRemaining, denominations, index + 1, map) 
		i += 1
	
	map[amount][index] = ways  # This assumes object by reference
	
	# Return the amount of ways 
	return ways 

# 8.12 - Eight Queens
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. 
# In this case, "diagonal" means all diagonals, not just the two that bisect the board. 

def placeQueens(row, columns, results): 
	GRID_SIZE = 8 

	if (row == GRID_SIZE): 
		results.add(columns.copy())
	else: 
		col = 0 
		while (col < GRID_SIZE): 
			if (checkValid(columns, row, col)): 
				columns[row] = col 
				placeQueens(row + 1, columns, results)
			col += 1
	
	return results

# Check if (row1, col1) is a valid spot to place a queen. Check if there is already a queen in the same column or diagonal. Checking rows is not necessary
def checkValid(columns, row1, col1):
	row2 = 0 
	# Check each of the rows to see if there is a spot 
	while (row2 < row1): 
		
		col2 = columns[row2] 
		# If column 2 is already occupied by a queen at another row, return False
		if (col1 == col2):
			return False
		
		# Check diagonals
		columnDistance = abs(col2 - col1)
		rowDistance = row2 - row1  #By definition row1 > row2 so no absolute value calculation needed

		# If column distance equals row distance, there is a queen in the same diagonal, return False
		if (columnDistance == rowDistance): 
			return False
		
	return True

# 8.13 - Stack of Boxes
# You have a stack of n boxes, with widths w(i), heights h(i)), and depths d(i).
# The boxes cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly larger than the box above it in width, height, and depth.
# Implement a method to compute the height of the tallest possible stack.
# The height of a stack is the sum of the heights of each box. 

# Assume the boxes list has already be created. The list contains objects of just type Box.
def createStack(boxes): 
	boxes = sorted(boxes, cmp=compare(), reverse=True)   # List by descending order; highest height first
	maxHeight = 0 
	stackMap = [0]*len(boxes)   # This assumes object by reference

	for i in range(len(boxes)): 
		height = createStack(boxes, i, stackMap) 
		maxHeight = max(maxHeight, height)
	
	return maxHeight

def createStack(boxes, bottomIndex, results):

	# If the results were already calculated previously, return the result given
	if (bottomIndex < len(boxes) and results[bottomIndex] > 0): 
		return results[bottomIndex]

	bottom = boxes[bottomIndex]
	maxHeight = 0 

	for i in range(bottomIndex + 1, len(boxes)): 
		if boxes[i].canBeAbove(bottom):   # Assume the canBeAbove function has been defined already
			height = createStack(boxes, i)
			maxHeight = max(maxHeight, height) 
	
	maxHeight += bottom.height
	results[bottomIndex] = maxHeight

	return maxHeight

def compare(box1, box2): 
	return box1.height - box2.height

"""Alternative Scenario"""

def createStackAlt(boxes): 
	boxes = sorted(boxes, cmp=compare(), reverse=True)   # List by descending order; highest height first
	stackMap = [0]*len(boxes)   # This assumes object by reference
	
	return createStackAlt(boxes, None, 0, stackMap) 


def createStackAlt(boxes, bottom, offset, results):

	# Base case
	if (offset > len(boxes)): 
		return 0

	# Calculate the height with the (new) bottom box
	newBottom = boxes[offset] 
	heightBottom = 0 

	if (bottom == None) or newBottom.canBeAbove(bottom): # Assume canBeAbove is already defined
		if (results[offset] == 0): 
			results[offset] = createStackAlt(boxes, newBottom, offset + 1, results)
			results[offset] += newBottom.height
	
	heightBottom = results[offset]

	# Calculate height without the bottom box
	heightNoBottom = createStackAlt(boxes, bottom, offset + 1, results) 

	return max(heightBottom, heightNoBottom)

# 8.14 - Boolean Evaluation
# Given a boolean expression consisting of symbols 0 (false), 1 (true), & (AND), | (OR), and ^ (XOR), and a desired boolean result value "result"...
# Implement a function to count the number of ways of parenthesizing the expression such that it evaluates to result. 
# The expression should be fully parenthensized (e.g. (0) ^ (1) ) but not extraneously (e.g. (((0))^(1)) )

# EXAMPLES: 
# countEval("1^0|0\1", False) --> 2
# countEval("0&0&0&161|0", True) --> 10 

def countEval(string, result, memory = {}): 
	if len(string) == 0: return 0 
	if len(string) == 1: return 1 if stringToBool(string) == result else 0 

	# If the result based on a result and string combo was already calculated, return that result 
	if (result + string) in memory:
		return memory.get(result + string)

	ways = 0 
	for i in range(0, len(string), 2): 
		character = string[i] 
		left = string[0:i]
		right = string[i+1:len(string)]

		#Evaluate each side for each result
		leftTrue = countEval(left, True)
		leftFalse = countEval(left, False)
		rightTrue = countEval(right, True)
		rightFalse = countEval(right, False)
		total = (leftTrue + rightTrue) + (leftFalse + rightFalse)

		totalTrue = 0
		if (character == '^'):   
			#Check with XOR
			totalTrue = (leftTrue * rightFalse) + (leftFalse * rightTrue)
		elif (character == "&"): 
			#Check with AND
			totalTrue = leftTrue * rightTrue 
		elif (character == "|"): 
			#Check with OR
			totalTrue = (leftTrue * rightTrue) + (leftFalse * rightTrue) + (leftTrue * rightFalse) 

		subWays = totalTrue if result else total - totalTrue 
		ways += subWays

	# Store the result in memory for later use	
	memory[result+string] = ways
	return ways 

def stringToBool(string): 
	return True if (string == "1") else False