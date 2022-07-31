"""HEAPS"""
# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # Create a frequency hash map and bucket list
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the number of elements, then populate the lists through iteration
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items(): 
            freq[count].append(num)
        
        # Find the top k values
        result = [] 
        
        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]:  # For every number at index i, add to the result
                result.append(num)
                
                if (len(result)) == k: 
                    return result   

# Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Base case
        if not lists or len(lists) == 0: 
            return None
        
        while len(lists) > 1: 
            mergedLists = [] 
            
            # Merge two linked lists
            for i in range(0, len(lists), 2): 
                list1 = lists[i]
                list2 = lists[i + 1] if ((i + 1) < len(lists)) else None
                mergedLists.append(self.mergeLists(list1, list2))
            # Update the merged lists to continue merging larger lists
            lists = mergedLists
        
        # Return the merged list
        return lists[0]
    
    def mergeLists(self, list1, list2):
        
        dummy = ListNode() 
        tail = dummy
        
        while list1 and list2: 
            if (list1.val < list2.val): 
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        # Add any remaining nodes to the new list
        if list1: 
            tail.next = list1
        if list2: 
            tail.next = list2
        
        # Return the dummy's next node
        return dummy.next    