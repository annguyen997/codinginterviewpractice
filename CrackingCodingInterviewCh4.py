
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 4 - Trees and Graphs'''

from tabnanny import check
import sys

# 4.1 - Route Between Nodes
# Given a direct graph, design an algorithm to find out whether there is a route between two nodes.

"""Breadth-First Search case"""
def routeFound(graph, node1, node2):
    #If the node references point to same node, return True by definition
    if (node1 == node2): 
        return True

    #Create a list that operates as a queue
    queue = []

    #Mark each node in the graph as unvisited
    for node in graph: 
        node.visited = False

    #This mechanism uses the breadth-first search
    queue.append(node1) 
    
    while (len(queue)): 
        #Dequeue the node from the beginning of the list
        node = queue.remove(0)

        if (node.adjacent):
            for child in node.getAdjacent():
                if (child == node2): 
                    return True
                else: 
                    queue.append(child) 

        node.visited = True
    
    return False

"""Depth-First Search case"""
def routeFoundDFS(graph, node1, node2):
    #If the first node is None, return False by definition
    if (node1 == None): 
        return False 

    #If the node references point to same node, return True by definition
    if (node1 == node2): 
        return True

    #Ensure all nodes in the graph are unvisited
    for node in graph: 
        node.visited = False

    node1.visited = True

    for adjacentNode in node1.getAdjacent():
        if (adjacentNode == node2): 
            return True
        
        if (adjacentNode.visited == False): 
            routeFoundDFS(graph, adjacentNode, node2)
    
    return False 

# 4.2 - Minimal Tree
# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

class BinaryTreeNode: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, node):
        self.left = node
    
    def getRight(self):
        return self.right
    
    def setRight(self, node):
        self.right = node

#This function is used to determine the start and end points of the given array
def createMinimalTree(array):
    start = 0 
    end = len(array) - 1

    return createMinimalTreeBFS(array, start, end)

def createMinimalTreeBFS(array, start, end):
    #If the ending is somehow smaller than start, return None
    if (end < start): 
        return None

    middle = start + end / 2
    value = array[middle] 

    node = BinaryTreeNode(value)
    node.setLeft(createMinimalTreeBFS(array, start, middle - 1))
    node.setRight(createMinimalTreeBFS(array, middle + 1, end))

    return node 


# 4.3 - List of Depths
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
# That is, if there is a tree with depth D, there are D linked lists. 

"""Depth-First Search Approach"""
class LinkedListNode: 
    def __init__(self, value): 
        self.value = value
        self.next = None
    
    def setNext(self, node): 
        self.next = node
    
    def getNext(self):
        return self.next
    
    def setValue(self, value):
        self.value = value 

    def getValue(self):
        return self.value

def createDepthLinkedLists(root, lists = [], level = 0):
    #If the root node has no Node, then return None. This may also indicate the "parent" node is a leaf. 
    #Base case
    if (root == None): 
        return None
    
    #If the number of lists equals the level, that means there is currently no linked list of that level
    if (len(lists) == level): 
        list = LinkedListNode(root.value)
        lists.add(list)
    else:
        #Add the new node to the current linked list; traverse through linked list towards the end
        list = lists[level]
        while (list.getNext() != None): 
            list = list.getNext()
        
        list.setNext(LinkedListNode(root.value))

    #Depth-first search, using preorder traversal 
    createDepthLinkedLists(root.getLeft(), lists, level + 1)
    createDepthLinkedLists(root.getRight(), lists, level + 1)

    return lists

"""Breadth-First Search Approach"""

# 4.4 - Check Balanced
# Implement a function to check if a binary tree is balanced. 
# DEFINITION for this question: A balanced tree is a tree such that the heights of the two subtrees of any node never differ more than one.

def checkBalanced(node):
    return checkHeight(node) != -2

def checkHeight(node):
    #This node is used for leaves as well as None nodes; this is the base case 
    if (node == None): 
        return -1

    left = checkHeight(node.left)
    right = checkHeight(node.right)

    heightDiff = left - right
    if (abs(heightDiff) > 1): 
        #This is the value used to indicate the binary tree is not balanced
        return -2  
    else: 
        return max(left, right) + 1  #Plus one is used to count the previous level (i.e. iterate height)

# 4.5 - Validate BST
# Implement a function to check if a binary tree is a binary search tree. 
# For this problem, the definition is assumed to be: left_nodes <= current_node < right_nodes. This means a duplicate value is permitted. 

def chekBST(node):
    return checkBSTInternal(node)

def checkBSTInternal(node, min = None, max = None): 
    #Base case 
    if (node == None): 
        return True
    
    #If minimum and maximum values are provided, and the current node's value is <= min or > max, this is not a BST
    if ((min != None and node.val <= min) or (max != None and node.val > max)): 
        return False
    
    #If the left node check fails or the right node check fails, return False, that is this is not a BST
    if not (checkBSTInternal(node.left, min, node.val)) or not (checkBSTInternal(node.right, node.val, max)): 
        return False
    
    return True

# 4.6 - Successor
# Write an algorithm to find the "next" node (i.e. in-order successor) of a given node in a binary search tree. 
# You may assume that each node has a link to its parent. 
    
    
  
