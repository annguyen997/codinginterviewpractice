
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


def main(): 
    print(URLify("Mr John Smith"))

main() 
    