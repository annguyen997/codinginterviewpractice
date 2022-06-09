
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 2 - Linked List'''

# 2.1 - Remove Duplicates
# Write code to remove duplicates from an unsorted linked list. 
# FOLLOW-UP: How would you solve this problem if a temporary buffer is not allowed? 

def removeDups(node):
    # Use a set to track duplicates
    duplicates = {}

    #Traverse through the unsorted linked list, starting the head
    prev = None
    while (node != None):
        #If value is in the duplicates set, point previous node's next pointer to the current node's next pointer.
        if (node.value in duplicates):
            prev.next = node.next
        else:
            duplicates.add(node.value)
            prev = node

        #Advance to the next node
        node = node.next

'''Alternative Scenario - with no buffer'''
def removeDups(head):
    # Create a pointer that will traverse through entire linked list
    current = head

    while (current != None):
        #Create another node that checks all subsequent nodes for duplicates
        runner = current

        #Traverse the runner through the list, starting at the next node
        while (runner.next != None): 
            if (runner.next.value == current.value):
                runner.next = runner.next.next
            else: 
                runner = runner.next
        
        #Once runner traverses through entire list, move the current pointer
        current = current.next 


# 2.2 - Return Kth to Last
# Implement an algorithm to find the kth to last element of a singly linked list
# For this solution, assume all values of k start at 1, where 1 is the last element in the list

'''Recursive Solution - Do Not Return the Element'''
def returnKthToLast(head, kth):
    #If the linked list is zero, or reached to the end of the list
    if (head == None): 
        return 0
    
    #Recursive calls to traverse through list until kth index is found
    index = returnKthToLast(head.next, kth) + 1

    if (index == kth): 
        print(head.value) 

    return index

'''Iterative Solution'''
def returnKthToLastIterative(head, kth): 
    p1 = head
    p2 = head

    #Move p1 into the list k times
    for i in range(kth): 
        if (p1 == None): 
            return None #Out of bounds
        p1 = p1.next 

    #Move p2 towards the same spot as p1, but move at same pace. When p1 hits the end, p2 will be at the correct element
    while (p1 != None):
        p1 = p1.next
        p2 = p2.next
    
    return p2

# 2.3 - Delete Middle Node
# Delete a node in the middle (i.e. any node besides the first and last nodes, not necessarily exact middle) of a singly linked list
# You are have access to the node provided only (not the head).

def delMiddleNode(node): 
    #If node provided is null or the next node is null (that is provided node is presumably final)
    if (node == None or node.next == None): 
        return False

    #To avoid duplicate of next node in the linked list, copy the next node in a temporary variable to redirect
    nextNode = node.next
    node.data = nextNode.data
    node.next = nextNode.next   #or possibly node.next = node.next.next 

    return True

# 2.4 - Partition 
# Partition a linked list around a value x, such that all nodes less than x come before all nodes >= x. 
# If x is contained within the list, values of x only need to be after elements less than x. 
# Partition element x can appear anywhere in the "right partition"; it does not need to appear between left and right partitions. 

def partition(): 
    pass

# 2.5 - Sum Lists
# Two numbers represented by a linked list, where each node contains a single digit. 
# The digits are stored in reverse order, such that 1's digit is at the head of the list. 
# Write a function that adds two numbers and returns the sum as a linked list. 

class Node: 
    def __init__(self, value): 
        self.val = value
        self.next = None
    
    def setNext(self, next): 
        self.next = next

def sumList(head1, head2): 
    #If one of the heads contains nothing, return 0
    if (head1 == None and head2 == None): 
        return 0
    
    #Create pointers to traverse through the list
    p1 = head1
    p2 = head2

    #Create the new head object
    newHead = None
    #Store value of larger digit if > 10
    largerDigit = 0

    prevNode = None
    while (p1 != None and p2 != None):
        #Calculate the values of two pointers plus any leftover digits from previous iterations
        tempValue = p1.val + p2.val + largerDigit
        if (tempValue >= 10):
            largerDigit = int(str(tempValue)[0:-1])
        tempValue = int(str(tempValue[-1]))
        
        #Create the new node to store the new value
        newNode = Node(tempValue)
        if (newHead == None): 
            newHead == newNode
        else: 
            prevNode.next = newNode
        prevNode = newNode
        
        #Move the pointers to calculate the next digit
        p1 = p1.next
        p2 = p2.next

    #If pointer 1 is still not fully traversed
    while (p1 != None): 
        tempValue = p1.val + largerDigit

        if (tempValue >= 10):
            largerDigit = int(str(tempValue)[0:-1])
        tempValue = int(str(tempValue[-1]))
        
        #Create the new node to store the new value
        newNode = Node(tempValue)
        prevNode.next = newNode
        prevNode = newNode
        
        #Move the pointers to calculate the next digit
        p1 = p1.next
    
    #If pointer 2 is still not fully traversed
    while (p2 != None): 
        tempValue = p2.val + largerDigit

        if (tempValue >= 10):
            largerDigit = int(str(tempValue)[0:-1])
        tempValue = int(str(tempValue[-1]))
        
        #Create the new node to store the new value
        newNode = Node(tempValue)
        prevNode.next = newNode
        prevNode = newNode
        
        #Move the pointers to calculate the next digit
        p2 = p2.next
    
    if (largerDigit): 
        #Create the new node to store the new value
        newNode = Node(largerDigit)
        prevNode.next = newNode

    return newHead

"""Text Alternative"""

def addLists(head1, head2, carry):
    #If both linked lists are empty, return None
    if (head1 == None) and (head2 == None) and (carry == 0): 
        return None

    #Create a new linked list
    result = Node() 
    value = carry

    if (head1 != None): 
        value += head1.val
    if (head2 != None): 
        value += head2.val 
    
    #Get the ones digit into the result value for the created Node
    result.val = value % 10

    #Recursive 
    if (head1 != None) or (head2 != None): 
        more = addLists(head1.next if head1 != None else None, head2.next if head2 != None else None, value)
        result.setNext(more)

    return result 
    
# 2.6 - Palindrome
# Implement a function to check if a linked list is a palindrome. 

def checkLinkedListPalindrome(head):
    #Clone the original list but reversed
    reversedList = cloneLinkedList(head)

    #Traverse through both lists to check if linked lists are palindromes
    p1 = head
    p2 = reversedList 

    while (p1 != None and p2 != None): 
        if (p1.val != p2.val): 
            return False
        p1 = p1.next
        p2 = p2.next

    return True

def cloneLinkedList(node):
    newHead = None
    while (node != None): 
        newNode = Node(node.val)
        newNode.next = newHead
        newHead = node
        node = node.next
    
    return newHead 

'''Stack Solution'''
def checkLinkedListPalindromeStack(head): 
    #Create a stack and two pointers to track linked list
    stack = [] 
    p1 = head
    p2 = head 

    #Traverse through the linked list, with one pointer move twice as fast as the other
    while (p2 != None and p2.next != None): 
        stack.insert(p1.val)
        p1 = p1.next
        p2 = p2.next.next

    #This runs if there are an odd number of elements in the linked list; advance the slow pointer
    while (p2 != None):
        p1 = p1.next
    
    #First pointer should traverse through list as stack is popped. 
    while (p1 != None): 
        element = stack.pop()
        if (element != p1.val): 
            return False
        p1 = p1.next 
    
    return True
    


# 2.7 - Intersecton
# Given two (singly) linked list, determine if the two lists intersect. 
# Return the intersecting node. 
# Note the intersection is defined based on reference, not value. 

def findIntersection(head1, head2): 
    #Check if there is a linked list available
    if (head1 == None) or (head2 == None): 
        return None 

    #Traverse through the list to get the lengths of the linked lists
    pointer1 = head1
    pointer2 = head2

    length1, pointer1 = calculateSizeAndTail(pointer1)
    length2, pointer2 = calculateSizeAndTail(pointer2) 

    #Check the tails if there are different, and if so return None
    if (pointer1.val != pointer2.val): 
        return None

    #Calculate which is the longer one, and then assign head accordingly
    longer = head1 if length1 < length2 else head2
    shorter = head2 if length1 < length2 else head1

    #Move the longer one ahead first to match shorter
    difference = abs(length2 - length1)
    longer = moveKthnode(longer, difference)

    #Traverse through the linked lists to find the intersecting value
    while (longer.val != shorter.val): 
        longer = longer.next
        shorter = shorter.next
    
    #Return either one of the nodes
    return shorter

def calculateSizeAndTail(node): 
    if (node == None): 
        return None
    
    size = 1 

    while (node.next != None): 
        size += 1
        node = node.next
    
    return size, node

def moveKthnode(node, diff):
    while (node != None) and (diff > 0): 
        node = node.next
        diff -= 1
    
    return node
    




def main(): 
    pass

main() 
