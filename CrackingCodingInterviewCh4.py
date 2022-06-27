
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 4 - Trees and Graphs'''

from os import pathsep
from tabnanny import check
import sys
import random
from turtle import left, right

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
# This solution assumes a "left < curr < right" binary search tree, meaning there are no duplicates
    
class TreeNode:
    def __init__(self, value, parent=None): 
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
  
def findSuccessor(node):
    if (node == None): 
        return None
    
    #If the given node has no right children, go up to parent
    if (node.right == None):
        currentNode = node 
        parentNode = node.parent
        
        #Go up to another parent level as long as this is still the right subtree (i.e. go until at left subtree)
        while (parentNode != None) and (parentNode.left != currentNode):
            currentNode = parentNode
            parentNode = parentNode.parent

        return parentNode

    else: 
        return leftMostChild(node.right)
    

def leftMostChild(node): 
    if (node == None):
        return None
    
    while (node.left != None): 
        node = node.left
    
    return node

# 4.7 - Build Order
# You are given a list of projects, and a list of dependencies (that is a list of pairs of projects, where the second project is dependent on the first project)
# All of the project's dependencies must be built before the project is.
# Find a build order that will allow the projects to be built. 
# If there is no valid order, return an error.

# This assumes any independent nodes (i.e. no dependencies and dependents) can be done at any time, so order of output may be arbitrary for those cases. 

class ProjectNode:
    def __init__(self, value): 
        self.value = value
        self.children = []
        self.map = {}
        self.incomingEdges = 0
    
    def addConnectingNodes(self, node): 
        if not (self.map.get(node.getValue())): 
            self.children.append(node)
            self.map[node.getValue()] = node
            node.incrementEdge()
    
    def getValue(self): 
        return self.value

    def getChildren(self): 
        return self.children
    
    def getIncomingEdges(self):
        return self.incomingEdges

    def incrementEdge(self): 
        self.incomingEdges += 1
    
    def decrementEdge(self): 
        self.incomingEdges -= 1

class ProjectGraph:
    def __init__(self): 
        self.nodes = [] 
        self.map = {}
    
    def getNode(self, name):
        #If the node is not in the graph 
        if not (self.map.get(name)):
            self.createNode(name)

        #Get the node from the graph that has the associated name
        return self.map.get(name)

    #Create a new node to add to the graph
    def createNode(self, name): 
        node = ProjectNode(name)
        self.nodes.append(node)
        self.map[name] = node
    
    #Add an edge to the graph
    def addEdge(self, node1, node2):
        start = self.getNode(node1)
        end = self.getNode(node2) 
        start.addConnectingNodes(end)
    
    def getNodes(self): 
        return self.nodes

def buildOrder(projects, dependencies): 
    if (projects == None):
        return None
    
    if (dependencies == None): 
        return projects

    graph = buildGraph(projects, dependencies)
    return orderProjects(graph.getNodes())
        
def buildGraph(projects, dependencies):
    graph = ProjectGraph()

    for project in projects: 
        graph.createNode(project)

    #For this function, assume dependencies is a list of tuples
    for dependency in dependencies:
        first, second = dependency
        graph.addEdge(first, second)
    
    return graph
        
def orderProjects(nodes):
    projectOrder = [0 * len(nodes)]

    #Start with projects with zero dependencies
    endofList = addNonDependent(projectOrder, nodes, 0)

    toBeProccessed = 0 
    while (toBeProccessed < len(projectOrder)):
        current = projectOrder[toBeProccessed]

        # A circular dependency, which means no applicable project order is found. Return None.
        if (current == None): 
            return None

        # Go through the children of that node, decrement the dependency, and then add that node to order. 
        children = current.getChildren()
        for child in children:
            child.decrementEdge()
        
        endofList = addNonDependent(projectOrder, children, endofList)
        toBeProccessed += 1
    
    return projectOrder


def addNonDependent(order, nodes, offset): 
    for node in nodes: 
        #If the node has no incoming nodes (that is no dependencies), add to order
        if (node.getIncomingEdges() == 0): 
            order[offset] = node
            offset += 1
    
    return offset 

"""Depth-First Search Solution"""

# 4.8 - Find Common Ancestor
# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
# Avoid storing additional nodes in a data structure. 
# This is not necessarily a binary search tree. 

#For this solution, assume the two nodes have links to the parent
def findCommonAncestor(node1, node2):
    if (node1 == None) or (node2 == None):
        return None
    
    #Calculate the difference in depths of the two provided nodes
    heightDelta = depth(node1) - depth(node2)

    #Determine which one is the higher node
    higherNode = node2 if heightDelta > 0 else node1
    lowerNode = node1 if heightDelta > 0 else node2

    #Raise the lower node up to the same depth as higher node 
    lowerNode = goUpBy(lowerNode, abs(heightDelta))

    #Once the nodes are at the same depth, go up towards the common ancestor if there is one
    while (lowerNode != higherNode) and (lowerNode != None) and (higherNode != None): 
        higherNode = higherNode.parent
        lowerNode = lowerNode.parent

    if (higherNode == None) or (lowerNode == None): 
        return None

    return higherNode

def depth(node): 
    depth = 0
    while (node != None): 
        node = node.parent
        depth += 1
    
    return depth 

def goUpBy(node, height):
    while (node != None and height != 0): 
        node = node.parent
        height -= 1
    
    return node


# 4.9 - BST Sequences
# A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

# This solution assumes this binary search tree has already been built. 
def BSTSequences(node):
    elementArray = [] 
    
    if (node == None): 
        elementArray.add(LinkedListNode())
        return elementArray
    
    prefix = LinkedListNode() 
    prefix.setValue(node.data)

    # Recurse on both left and right subtrees
    leftSequence = BSTSequences(node.left)
    rightSequence = BSTSequences(node.right) 
    
    for leftNodes in leftSequence: 
        for rightNodes in rightSequence: 
            weaved = []
            weaveLists(leftNodes, rightNodes, weaved, prefix)
            
            for weavedItem in weaved:
                elementArray.add(weavedItem)
    
    return elementArray
    
def weaveLists(leftNodes, rightNodes, weavedList, prefix):
    # One list is empty. Add remainder to (a cloned) prefix and store result. 
    if (len(leftNodes) == 0) or (len(rightNodes) == 0): 
        result = prefix.copy()

        for leftNode in leftNodes:
            result.add(leftNode) 

        for rightNode in rightNodes: 
            result.add(rightNode)

        weavedList.add(result) 

        return; 
    
    # Recurse with head of first of left node added to the prefix. 
    headFirst = leftNode.removeFirst() 
    prefix.addLast(headFirst)
    weaveLists(leftNodes, rightNodes, weavedList, prefix) 
    prefix.removeLast(headFirst) 
    leftNodes.add(headFirst) 

    # Recurse with head of the first of right node added to the prefix.
    headSecond = rightNode.removeFirst() 
    prefix.addLast(headSecond)
    weaveLists(leftNodes, rightNodes, weavedList, prefix) 
    prefix.removeLast(headSecond)
    rightNodes.add(headSecond) 

# 4.10 - Check Subtree
# T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
# Create an algorithm to determine if T2 is a subtree of T1.

# A tree T2 is a subtree of T1 IF there exists a node n in T1 such that the subtree of n is identical to T2. 
# That is if you cut the tree at node n, the two trees would be identical. 

def checkSubtree(nodeT1, nodeT2): 
    if (nodeT1 == None):
        return None 
    
    #If an empty subtree, by definition it is a subtree
    if (nodeT2 == None): 
        return True 

    traversal1 = preOrderTraversal(nodeT1)
    traversal2 = preOrderTraversal(nodeT2)

    return traversal1 == traversal2

def preOrderTraversal(node, traversal = ""): 

    if (node == None): 
        traversal += "X" + " "
        return traversal

    traversal += str(node.value) + " "
    traversal = str(preOrderTraversal.left, traversal)
    traversal = str(preOrderTraversal, traversal)

    return traversal 

# 4.11 - Random Node
# You are implementing a binary tree class from scratch.
# In addition to insert, find, and delete functions, there is a getRandomNode()
# The getRandomNode() returns a random node from the tree. All nodes should be equally likely to be chosen. 
# Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods. 

class RandomTreeNode: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
        self.size = 0 
    
    def insert(self, value): 
        if (value <= self.value): 
            if (self.left == None): 
                self.left = RandomTreeNode(value)
            else: 
                self.left.insert(value) 
        else:
            if (self.right == None): 
                self.right = RandomTreeNode(value) 
            else: 
                self.right.insert(value) 
        
        self.size += 1
    
    def find(self, value): 
        if (value == self.value): 
            return self 
        elif (value < self.value): 
            return self.left.find(value) if self.left != None else None
        elif (value > self.value):  
            return self.right.find(value) if self.right != None else None
        
        return None
    
    def delete(self, value): 
        pass

    def getRandomNode(self): 
        leftSize = self.left.getSize() if self.left != None else None
        
        #Start the random seed to generate random node of the tree. Getting size of left tree is important in probability (LEFT_SIZE * 1/n)
        random.seed()
        index = random.randInt(self.size) 

        if (index < leftSize): 
            return self.left.getRandomNode()
        elif (index == leftSize): 
            return self
        else: 
            return self.right.getRandomNode() 

    def getIthIndex(self, index):
        leftSize = self.left.getSize() if self.left != None else 0
        if (index < leftSize): 
            return self.left.getIthIndex(index) 
        elif (index == leftSize): 
            return self
        elif (index > leftSize): 
            return self.right.getIthIndex(index - (leftSize + 1))

    def getSize(self): 
        return self.size
    
    def getValue(self):
        return self.value
        
class BinaryTree: 
    def __init__(self): 
        self.root = None
    
    def insert(self, value): 
        if (self.root == None): 
            self.root = RandomTreeNode(value)
        else:
            self.root.insert(value)
    
    def find(self, node): 
        #If the root's value equals the value of provided node, return the node
        if (node.val == self.root.val): 
            return self.root
        elif (node.val < self.root.val): 
            return self.find(self.root.left) if self.root.left != None else None

    def delete(self, node): 
        self.numberNodes -= 1

    def getRandomNode(self):
        if (self.root == None):
            return None
        
        random.seed() 
        index = random.randInt(self.getSize())

        return self.root.getIthIndex(index) 
    
    def getSize(self): 
        return self.root.size() if self.root != None else None

         
# 4.12 - Paths with Sum
# You are given a binary tree in which each node contains an integer value (which might be positive or negative). 
# Design an algorithm to count the number of paths that sum to a given value. 
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes). 

def countPathsWithSum(root, targetSum):

    if (root == None): 
        return None
    
    #Check for paths from the root, if available 
    numPathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)

    #Check for paths from the left and right sides of the binary tree
    numPathsFromLeft = countPathsWithSum(root.left, targetSum)
    numPathsFromRight = countPathsWithSum(root.right, targetSum)

    return numPathsFromLeft + numPathsFromRight + numPathsFromRoot

def countPathsWithSumFromNode(node, targetSum, currentSum):
    #If node is Null, return 0
    if (node == None): 
        return 0
    
    currentSum += node.value

    totalPaths = 0 
    #If the current sum matches the target path, add path
    if (currentSum == targetSum): 
         totalPaths += 1
    
    totalPaths += countPathsWithSumFromNode(node.left, targetSum, currentSum) 
    totalPaths += countPathsWithSumFromNode(node.right, targetSum, currentSum)

    return totalPaths
    
"""Optimized Solution"""
def countPathsOptimized(root, targetSum): 
    if (root == None): 
        return 0
    
    pathCount = {} 

    return countPathsWithSumOptimized(root, targetSum, 0, pathCount)

def countPathsWithSumOptimized(node, targetSum, runningSum, pathCount): 
    if (node == None): 
        return 0

    runningSum += node.data
    sum = runningSum - targetSum
    totalPaths = pathCount.get(sum) if (pathCount.get(sum) != 0) else 0 

    if (runningSum == targetSum): 
        totalPaths += 1
    
    #Increment pathCount, recurse for both sides of the binary tree, then decrement count
    incrementPathCount(pathCount, runningSum, 1)
    totalPaths += countPathsWithSumOptimized(node.left, targetSum, runningSum, pathCount)
    totalPaths += countPathsWithSumOptimized(node.right, targetSum, runningSum, pathCount) 
    incrementPathCount(pathCount, runningSum, -1)

def incrementPathCount(pathCount, key, delta):
    newCount = pathCount.get(key) + delta
    if (newCount == 0): 
        del pathCount[key]
    else: 
        pathCount[key] == newCount
    

def main(): 
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

    print(buildOrder(projects, dependencies))


main() 