
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
