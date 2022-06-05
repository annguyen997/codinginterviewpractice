
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 1 - Arrays and Strings'''
# 1.1 - Is Unique: 
# - Implement an algorithm to determine if a string has all unique characters.
# - What if you cannot use additional data structures?
def isUnique(text): 

    #Get the length of the text
    length = len(text) 

    # Assume there are 128 unique characters in the ASCII string that can be validated. 
    # If there is more than 128, by definition the string does not have characters that are unique. 
    if (length > 128): 
        return False 
        
    charSet = set() 

    #Loop through each character in the text
    for i in range(length): 
        if text[i] in charSet:
            return False
        
        charSet.add(text[i])
    
    return True

# 1.2 - Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other 
# - Assume letters are case senstitive
# - Assume whitespace is significant
# - Assume the strings cannot be sorted 

def checkPermutation(string1, string2): 

    #Check if the two strings have equal length
    if (len(string1) != len(string2)): 
        return False

    #Create a hash map to count the number of characters 
    charDict = dict() 

    #Add all the characters of string1 to dictionary
    for i in range(len(string1)): 
        char1 = string1[i]

        if char1 not in charDict: 
            charDict[char1] = 1 
        else: 
            charDict[char1] += 1 
    
    #Check all characters of string2 in dictionary
    for j in range(len(string2)): 
        char2 = string2[j]
        if char2 in charDict: 
            charDict[char2] -= 1
            if charDict[char2] == 0: 
                charDict.remove(char2)
        else:
            #If the character does not appear in dictionary, then permutation is not True
            return False 
        
    return True 

# 1.3 - URLify: 
# - Write a method to rpelace all spaces in a string with '%20'.
# - Assume string has sufficient space at end to hold additional characters 
# - Assume that the true length of the string is provided 

def URLify(url): 
    
    newString = ""

    for i in range(len(url)): 
        if url[i] == ' ': 
            newString += "%20" 
        else: 
            newString += url[i]
    
    return newString

# 1.4 - Palindrome Permutation: 
# Given a string, check if it is a permutation of a palindrome. 
# The palindrome does not need to be limited to just dictionary words. 
# Assume the characters are alphanumeric; other characters are disregarded for purposes of calculation.

def checkPermutationIsPalindrome(string):
    permuDict = dict() 

    for i in range(len(string)): 
        charStr = string[i]

        #If character in question is not alphanumeric
        if (not charStr.isalnum()): 
            continue 
        
        #Calculate the number of times a character occurs in string
        if charStr not in permuDict: 
            permuDict[charStr] = 1
        else: 
            permuDict[charStr] += 1
    
    #There must be at most one character that appears odd; otherwise not valid palindrome
    #If even-numbered length string, all characters have even number
    oddNumber = False
    for key, value in permuDict.items():
        if value % 2 == 1:
            if (oddNumber): 
                return False
            else:  
                oddNumber = True

    return True  
        
# 1.5 - One Away: 
# There are three types of edits that can be performed on strings: Insert, remove, or replace (a character)
# Given two strings, write a function to check if they are one edit (or zero edits) away. 

def oneEditAway(first, second): 
    #Check the length of the two strings
    if (len(first) - len(second) > 1): 
        return False
    
    #Get the shorter and longer strings
    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first

    #Get the indexes to begin traversing through strings, and have boolean to check if difference has been found
    index1 = 0
    index2 = 0
    foundDifference = False 

    while (index2 < len(second) and index1 < len(first)): 
        if first[index1] != second[index2]: 
            #Check if this is the first difference found
            if foundDifference: 
                return False
            else: 
                foundDifference = True
        
            #This if statement is used if there is a replacement char
            if (len(s1) == len(s2)): 
                index1 += 1
        else:
            #This executes when index1 == index2 
            index1 += 1
        
        #Always move pointer of longer string
        index2 += 1
    
    return True


'''
def checkOneAway(givenString, desiredString):

    #Use a dictionary to store the contents of original string
    charString = dict() 

    for char in givenString: 
        if char in charString: 
            charString[char] += 1
        else: 
            charString[char] = 1
    
    #Check characters of desired string in compared to dictionary
    oneEdit = False

    for char2 in desiredString: 
        if char2 not in charString:
            if not oneEdit: 
                oneEdit = True
            else: 
                return False 
        else: 
            charString[char2] -= 1
            if charString[char2] == 0: 
                del charString[char2]

    
    return True
'''

# 1.6 - Implement Compression
# Implement a method to perform basic string compression using counts of repeated characters. 
# If compressed string would not become any smaller than original string, method should return original string
# Assume string has only upper and lowercase letters

def compressString(string): 
    #Establish count mechanism, and create compressed string variable
    count = 0
    compressedString = "" 
    
    #Traverse through the string, starting at beginning
    for i in range(len(string)): 
        count += 1

        if (string[i] != string[i+1] or i + 1 > len(string)):
            compressedString += "" + str(string[i]) + str(count)
            count = 0
    
    #Check if the compressed string is smaller than the original string, and return so if true
    return compressedString if (compressedString) < string else string

# 1.7 - Rotate Matrix
# Write a method to rotate the image by 90 degrees. Can you do this in place? 
# A given image is represented by an NxN matrix, which each pixel is 4 bytes

def rotate90matrix(matrix):

    #If matrix is empty or non-matching size of NxN, return False
    if (len(matrix) == 0) or (len(matrix) != len(matrix[0])): 
        return False 

    #Calculate the length of matrix for layering
    length = len(matrix)

    #Do this in layers, starting with outermost layer, in a circular rotation
    for layer in range(length/2):  #Swapping by 90 degrees mean length / 2 
        first = layer 
        last = length - 1 - layer

        for i in range(first, last): 
            #Offset is used to calculate bytes that have already been completed
            offset = i - first

            #Get the top as the temp
            top = matrix[first][i]
            #Swap top with left
            matrix[first][i] = matrix[last-offset][first]
            #Swap left with bottom
            matrix[last-offset][first] = matrix[last][last-offset]
            #Swap bottom with right
            matrix[last][last-offset] = matrix[i][last]
            #Swap right with top 
            matrix[i][last] = top

# 1.8 - Zero Matrix
# Write an algorithm such if an element in an MxN matrix is 0, its entire row and column are set to zero. 
def rotate90matrix(matrix):
    #Create a list variable to hold locations of zeros
    zeros = []

    #Traverse through the matrix
    colNum = len(matrix)
    rowNum = len(matrix[0])

    for i in range(rowNum): 
        for j in range(colNum): 
            if matrix[i][j] == 0: 
                zeros.append((i, j))
    
    #Edit all rows and columns of i, j to zeros
    while len(zeros) > 0: 
        i, j = zeros.pop() 

        #Turn all values of row i to zeros 
        for k in range(colNum): 
            matrix[i][k] = 0
        
        #Turn all values of column j to zeros
        for k in range(rowNum):
            matrix[k][j] = 0
    
    return matrix

'''Alternative Scenario'''
def setZeros(matrix): 
    rowHasZero = False
    colHasZero = False 

    #Check if the first row has a zero 
    for j in range(len(matrix[0])):
        if (matrix[0][j] == 0): 
            rowHasZero = True
            break 
    
    #Check if the first column has a zero
    for i in range(len(matrix)): 
        if (matrix[i][0] == 0): 
            colHasZero = False
            break 

    #Check for zeros in the rest of array
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): 
            if (matrix[i][j] == 0): 
                matrix[i][0] = 0 
                matrix[0][j] = 0
    
    #Nullify rows based on first column
    for i in range(len(matrix)): 
        if matrix[i][0] == 0: 
            nullifyRow(matrix, i)
    
    #Nullify columns based on first row
    for j in range(len(matrix[0])): 
        if matrix[0][j] == 0: 
            nullifyColumn(matrix, j)

    #Nullify first row and/or column
    if (rowHasZero): 
        nullifyRow(matrix, 0)
    if (colHasZero): 
        nullifyColumn(matrix, 0)

def nullifyRow(matrix, row): 
    for j in range(len(matrix[0])): 
        matrix[row][j] = 0

def nullifyColumn(matrix, column): 
    for i in range(len(matrix)): 
        matrix[i][column] = 0

# 1.9 - String Rotation
# Assume method isSubstring, which checks if one word is substring of another. 
# Given two strings s1, s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring

def isRotation(s1, s2):
    if (len(s2) == len(s1) and len(s1) > 0): 
        # Concantenate s1 twice
        s1s1 = s1 + s1
        
        # Get the first character of s2
        chars2 = s2[0]

        index = 0
        while index < len(s1s1):
            if chars2 == s1s1[index]:
                if s2[0:len(s2)] == s1s1[index:index+len(s2)]:
                    return True
            index += 1
        
    return False
        
def main(): 
    print(isRotation("waterbottle", "erbottlewat"))

main() 

    