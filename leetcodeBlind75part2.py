"TREES" 
# Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if (root == None): 
            return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        
        return max(left, right) 

# Same Tree 
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # If p and q are both None
        if (not p) and (not q): 
            return True
        
        # If p or q is None, then return False
        if (not q) or (not p): 
            return False
        
        # If the values do not match, return False
        if p.val != q.val: 
            return False
        
        # If values match, check the left and right subtrees to see if the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # If root is Empty
        if root == None: 
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp 
        
        self.invertTree(root.left)
        self.invertTree(root.right) 
        
        return root 

# Binary Tree Level Order Traversal 
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # If the root is None, return [] 
        if root is None: 
            return []
        
        queue = []
        output = [] 
        
        # Add the root to the queue
        queue.append(root) 
    
        # Loop through the queue as long as queue has elements...
        while len(queue) != 0:
            level = []
            
            for i in range(len(queue)): 
    
                # Remove the first element from the queue
                item = queue.pop(0)
                level.append(item.val) 

                if item.left != None:
                    queue.append(item.left) 
                if item.right != None: 
                    queue.append(item.right)
            
            # Ensures no empty levels are added
            if level: 
                output.append(level)
        
        return output 

# Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        # If subroot is empty, then by definition it is a subroot of root
        if (subRoot == None): 
            return True
        
        # If root is empty, then the subroot has nothing to compare - return False
        if (root == None): 
            return False
        
        # If root.val == subRoot.val, and subRoot is a subtree of root, return True
        if self.sameTree(root, subRoot): 
            return True
        
        # If root.val != subRoot.val, check the left and right children to find a subtree
        return self.isSubtree(root.left, subRoot.left) or self.isSubtree(root.right, subRoot.right)
    
    def sameTree(self, root, subRoot): 
        if (root == None) and (subRoot == None): 
            return True
        
        if (root) and (subRoot) and (root.val == subRoot.val):
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) 

        return False

# Validate Binary Search Tree  
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# 1) The left subtree of a node contains only nodes with keys less than the node's key.
# 2) The right subtree of a node contains only nodes with keys greater than the node's key.
# 3) Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.validBST(root, float("-inf"), float("inf"))

    def validBST(self, root, leftBoundary, rightBoundary):
        
        # Base case, an empty root is a valid BST by definition
        if not root:
            return True
        
        if not ((leftBoundary < root.val) and (root.val < rightBoundary)):
            return False 
        
        return self.validBST(root.left, leftBoundary, root.val) and self.validBST(root.right, root.val, rightBoundary)    


# Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # If either of the lists are empty, return None (no Nodes made)
        if not (preorder) or not (inorder): 
            return None
    
        # By definition, the first element of preorder list is the root
        root = TreeNode(preorder[0])
        
        # Find index of root in the inorder, and split the inorder into two pieces
        index = inorder.index(preorder[0])
        
        # Build the child nodes using the index information and the remaining lists
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return root 

# Binary Tree Maximum Path Sum
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum = [root.val]
    
        # Calculate the max path sum without split
        def calculatePath(root):
            if not root: 
                return 0 

            leftSum = max(calculatePath(root.left), 0)
            rightSum = max(calculatePath(root.right), 0)

            # Compute max path sum with split 
            maxSum[0] = max(maxSum[0], leftSum + rightSum + root.val)

            return root.val + max(leftSum, rightSum)
        
        calculatePath(root)
        return maxSum[0]

# Implement Trie (Prefix Tree) 
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
# 1) Trie() Initializes the trie object.
# 2) void insert(String word) Inserts the string word into the trie.
# 3) boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# 4) boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
class TrieNode: 
    def __init__(self): 
        self.children = {} 
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        currentNode = self.root
        
        for character in word: 
            
            # If character does not exist in children, create TrieNode for that character 
            if character not in currentNode.children:
                currentNode.children[character] = TrieNode() 
            
            # Get the character
            currentNode = currentNode.children[character]
        
        currentNode.endOfWord = True
                

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        currentNode = self.root
        
        for character in word: 
            # If character does not exist in children, return False
            if character not in currentNode.children:
                return False
            
            currentNode = currentNode.children[character]
        
        # Check if the current node is end of word
        return currentNode.endOfWord 
            
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        currentNode = self.root
        
        for character in prefix: 
            # If character does not exist in children, return False
            if character not in currentNode.children:
                return False
            
            currentNode = currentNode.children[character]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""STRING"""
# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = [] 
        
        for element in s: 
            if element in [')', '}', ']']:
                if (len(stack) == 0): 
                    return False
                
                stackElement = stack.pop()

                if (element == ')' and stackElement != '('): 
                    return False
                elif (element == '}' and stackElement != '{'): 
                    return False
                elif (element == ']' and stackElement != '['): 
                    return False
            else: 
                stack.append(element) 
        
        if (len(stack)): 
            return False 
        
        return True

# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Set up the pointers
        end = len(s) - 1
        start = 0
        
        while (start < end): 
            # Skip positions which characters are not alpahnumeric 
            while (start < end) and (not self.isAlphaNum(s[start])):
                start += 1
            while (end > start) and (not self.isAlphaNum(s[end])): 
                end -= 1
            
            # If the characters do not match, return False
            if (s[start].lower() != s[end].lower()): 
                return False
            
            # Iterate the pointers
            start += 1
            end -= 1
        
        return True
            
    def isAlphaNum(self, c): 
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

"""Alternative Solution"""

class Solution(object):
    def isPalindrome(self, s):
        newString = ""
        
        
        # Remove all non-alphanumeric characters and lowercase the letters
        for c in s: 
            if c.isalnum(): 
                newString += c.lower() 
        
        return newString == newString[::-1]

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxLength = 0
        left = 0
        charSet = set()
        
        for right in range(len(s)): 
            # If element is in character set, remove the element from set and shift left pointer
            while s[right] in charSet: 
                charSet.remove(s[left])
                left += 1
            
            # Add the character to the set
            charSet.add(s[right])
            
            maxLength = max(maxLength, right - left + 1)
                
        return maxLength

# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths are not equal, by definition they are not anagrams
        if len(s) != len(t): 
            return False
        
        charStr = {} 
        
        for ch in s:
            if ch not in charStr:
                charStr[ch] = 0
            
            charStr[ch] = 1 + charStr[ch]
        
        for ch in t: 
            if ch not in charStr: 
                return False
            
            charStr[ch] = charStr[ch] - 1
            
            if charStr[ch] == 0: 
                del charStr[ch]
        
        if charStr: 
            return False
        
        return True
 
 # Group Anagrams
 # Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Base case
        if not strs: 
            return None
        
        listAnagrams = defaultdict(list)  # Mapping charCount to list of anagrams
        
        for string in strs:
            count = [0] * 26 # a - z
            
            for c in string: 
                count[ord(c) - ord("a")] += 1
            
            # Add the count as a key, append the string
            listAnagrams[tuple(count)].append(string)
            
        return listAnagrams.values()

# Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Get the counts of the each character in the string s
        count = {} 
        result = 0
        
        left = 0
        maxFreq = 0 
        for right in range(len(s)): 
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq = max(maxFreq, count[s[right]])
            
            # If the number of replacements is greater than k, shift left
            while (right - left + 1) - maxFreq > k: 
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        # Return the result (maximum length) of the replacements
        return result