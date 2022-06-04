
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

def main(): 
    print(checkPermutationIsPalindrome("tact coa"))

main() 

    