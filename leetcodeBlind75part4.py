
"""MATRIX"""

# Spiral Matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []

        # Row
        top = 0 
        bottom = len(matrix)   
        
        # Column 
        left = 0
        right = len(matrix[0])  
        
        while (left < right) and (top < bottom): 
            
            # Get values from top row, left to right
            for i in range(left, right): 
                result.append(matrix[top][i])
            top += 1  # Shift top by 1 (eliminating row just completed)
            
            # Get values from rightmost column, top to bottom
            for i in range(top, bottom): 
                result.append(matrix[i][right - 1])   #-1 to prevent out of bounds
            right -= 1 
            
            # This is used for the middle the matrix 
            if not (left < right and top < bottom): 
                break 

            # Get values from bottom row, right to left
            for i in range(right - 1, left - 1, -1): 
                result.append(matrix[bottom - 1][i]) 
            bottom -= 1
            
            # Get values from leftmost column, bottom to top 
            for i in range(bottom - 1, top - 1, -1): 
                result.append(matrix[i][left])
            left += 1
        
        return result          
            
# Word Search 
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# EXAMPLE: 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        ROWS = len(board)
        COLS = len(board[0])
        
        # Add current values from board that currently in path
        path = set() 
        
        def dfs(row, col, i):

            # If index i is length of word, word has been found
            if i == len(word): 
                return True

            # If index is out of bounds, or index at word does not match the board, or row/col combination is already in path
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS or 
                word[i] != board[row][col] or 
                (row, col) in path): 
                return False
            
            path.add((row, col))
            
            # Find the target word continuously at next index
            result = (dfs(row+1, col, i + 1) or 
                        dfs(row-1, col, i + 1) or 
                        dfs(row, col+1, i + 1) or 
                        dfs(row, col-1, i + 1))
            
            # Remove row, col combination once backtracking 
            path.remove((row, col))
            
            return result 
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r, c, 0): return True
        return False

# Rotate Image 
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# EXAMPLE: 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Build the pointers
        left = 0
        right = len(matrix) - 1
        
        # Left and right pointers may not cross
        while (left < right):
            for i in range(right - left):
                
                # This is a square matrix pointers
                top = left
                bottom = right
            
                # Save the leftmost top value
                topLeft = matrix[top][left + i] 
                
                # Move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # Move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # Move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # Move top left to top right using temp variable
                matrix[top + i][right] = topLeft
        
            # Update the left and right pointers to do submatrix 
            left += 1
            right -= 1
                 
# Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.                      
# 
# EXAMPLE
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # O(1) solution 
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS): 
            for c in range(COLS): 

                # Set the first row and of that column zero if zero is found at matrix(r,c)
                if matrix[r][c] == 0: 
                    matrix[0][c] = 0

                    # Also set the first column of a given row zero only if it is not the first row
                    if r > 0: 
                        matrix[r][0] = 0
                    else: 
                        rowZero = True

        # Do the zeroing, skipping the first row and col
        for r in range(1, ROWS): 
            for c in range(1, COLS): 
                
                # If the first row or column is marked zero, zero that position too
                if matrix[0][r] == 0 or matrix[r][0] == 0: 
                    matrix[r][c] = 0

        # If the upperleft corner is zero, zero each row of first column
        if matrix[0][0] == 0: 
            for r in range(ROWS): 
                matrix[r][0] = 0 

        # If a column in the first row is zero, zero the columns of the first row
        if rowZero: 
            for c in range(COLS): 
                matrix[0][c] = 0

        return matrix