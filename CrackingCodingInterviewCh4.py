
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

def main(): 
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

    print(buildOrder(projects, dependencies))


main() 