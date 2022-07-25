
# Leetcode - Blind 75


"""ARRAYS"""
# Two Sum 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """ 
    #Create a dictionary of elements and their indices
    indexes = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in indexes.keys(): 
            return [indexes[complement], i]
        
        indexes[nums[i]] = i
    
    return [-1, -1]


# Best Time to Buy and Sell Stock 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            
            #Check if the current value is smaller than buy value
            if (buy > prices[i]): 
                buy = prices[i]
            
            elif (prices[i] - buy > max_profit): 
                max_profit = prices[i] - buy
        
        return max_profit

# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        duplicateSet = set()
        
        for element in nums: 
            if element in duplicateSet: 
                return True
            duplicateSet.add(element)
        
        return False

# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # If nums is empty, return empty list
        if not (nums): 
            return []
        
        # Build the answers array for returning
        answer = [1] * (len(nums))
        
        prefixResult = 1
        for i in range(len(nums)): 
            answer[i] = prefixResult
            prefixResult *= nums[i]
        
        # Traverse answers array from opposite direction
        postfixResult = 1 
        for i in range(len(nums) - 1, -1, -1): 
            answer[i] *= postfixResult
            postfixResult *= nums[i]
            
        return answer

# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = 0 
        sum = 0 

        for i in range(len(nums)): 
            sum += nums[i]

            # If the updated sum means maxSum < sum
            if (maxSum < sum): 
                maxSum = sum 
            # If adding the number results in a negative number, reset sum to zero
            elif (sum < 0): 
                sum = 0
            
        # If maximum sum is zero, return the highest negative value 
        if (maxSum == 0):
            leastNegative = None
            for i in range(len(nums)): 
                # If least negative number is None or a higher negative value found, report
                if (leastNegative == None) or (leastNegative < nums[i]): 
                    leastNegative = nums[i]

            return leastNegative
            
        return maxSum

# Maximum Product Subarray  
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.    
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # By definition, the highest value is the result (as n * 1 = n, which n is max. number)
        result = max(nums)
        
        minProduct = 1
        maxProduct = 1
        for n in nums: 
            
            # If n is zero, reset to 1 (to avoid product remain zero forever)
            if (n == 0): 
                minProduct = 1
                maxProduct = 1
            
            temp = maxProduct * n
                
            maxProduct = max(temp, n * minProduct, n)
            minProduct = min(temp, n * minProduct, n)
            
            result = max(result, maxProduct)
            
        return result

# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [] 
        
        # Sort the number array
        nums = sorted(nums) 
        
        # Find the solution set
        for i in range(len(nums)): 
            
            # If index is greater than zero, and nums[i] == nums[i-1], continue
            if (i > 0) and (nums[i] == nums[i - 1]):
                continue 
            
            # Use pointers to calculate through the list finding complements
            left = i + 1
            right = len(nums) - 1
            
            while (left < right):
                
                # Calculate sum
                threeSum = nums[i] + nums[left] + nums[right] 
                
                # If the sum is too large, decrement right pointer
                if (threeSum > 0): 
                    right -= 1
                # If sum is too small, increment left pointer
                elif (threeSum < 0): 
                    left += 1
                # Assuming sum equals zero, add three addends to list 
                else: 
                    output.append([nums[i], nums[left], nums[right]])
                    
                    # Increment left pointer to find possible another solution, avoiding repeat of same number
                    left += 1
                    while (nums[left] == nums[left - 1]) and (left < right): 
                        left += 1
        
        return output
                    
"""LINKED LISTS"""
# Reverse a Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prevNode = None 
        current = head
        while (current != None):
            next_node = current.next
            current.next = prevNode
            prevNode = current
            current = next_node
        
        head = prevNode
        return head

# Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #Cycle through the linked list using two pointers, one of them is faster
        pointer1 = head
        pointer2 = head

        while (pointer1 != None and pointer1.next != None):
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

            if (pointer1 == pointer2):
                return True
            
        return False


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
    