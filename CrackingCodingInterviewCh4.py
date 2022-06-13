
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 4 - Trees and Graphs'''


# 4.1 - Route Between Nodes
# Given a direct graph, design an algorithm to find out whether there is a route between two nodes.

"""Breadth-First Search case"""
from tkinter import E


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


    
    return False

# 4.2 - Minimal Tree
# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height. 