
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

# Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.     
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0 
        right = len(nums) - 1
        
        while left <= right: 
            mid = (left + right) // 2
            
            if (nums[mid] == target): 
                return mid 
            
            # Check the left sorted portion  
            if (nums[left] <= nums[mid]): 
                if (target > nums[mid]) or (target < nums[left]):
                    left = mid + 1
                else: 
                    right = mid - 1
            
            # Check the right sorted portion
            else: 
                if (target < nums[mid]) or (target > nums[right]):
                    right = mid - 1
                else: 
                    left = mid + 1
                    
        return -1 

# Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# 1) [4,5,6,7,0,1,2] if it was rotated 4 times.
# 2) [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minNum = nums[0]
        
        left = 0 
        right = len(nums) - 1
        
        while left <= right: 
            
            # If number on left is less than right, then by definition left number is min.
            if nums[left] < nums[right]: 
                minNum = min(minNum, nums[left])
                break 
            
            # Otherwise, use the number at midpoint 
            mid = (left + right) // 2
            minNum = min(minNum, nums[mid])
            
            # If the value of left most value is less than or equal to mid
            if (nums[left] <= nums[mid]): 
                left = mid + 1
            else: 
                right = mid - 1
            
        return minNum

# Container With Most Water
#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        """
        BRUTE FORCE
        
        maxArea = 0 
        
        for left in range(len(height)): 
            for right in range(left + 1, len(height)): 
                
                area = (right - left) * min(height[left], height[right])
                
                maxArea = max(maxArea, area)
        
        return maxArea 
        """
        
        maxArea = 0 
        
        # Use left and right pointers
        left = 0
        right = len(height)-1
        
        # Loop through the height array
        while (left < right): 
            
            # Calculate the area
            area = (right - left) * min(height[left], height[right])
            
            # Determine which area is largest
            maxArea = max(maxArea, area) 
            
            if (height[left] < height[right]): 
                left += 1
            else: 
                right -= 1
        
        return maxArea

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

# Detect Cycle in a Linked List
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

# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists
# Return the head of the merged linked list.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        new = ListNode()
        tail = new
        
        while list1 and list2: 
            # If value of current node at list 2 is less than the current node of list 1, add that node to new list
            if (list2.val < list1.val):
                tail.next = list2
                list2 = list2.next
            else: 
                tail.next = list1
                list1 = list1.next
            
            tail = tail.next
        
        # Add any remaining list1 elements to new list
        if list1: 
            tail.next = list1
        elif list2:
            tail.next = list2
  
        # Node initialized for new is a dummy node, return the next node to retrieve list
        return new.next
            
# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Create the distance between the two nodes equal to n
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Move the pointers, with right moving towards end of the list
        while right: 
            left = left.next
            right = right.next
        
        # Remove the node that is at index n from end
        left.next = left.next.next
        
        return dummy.next

# Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# 
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # Create the pointers
        slow = head
        fast = head.next
        
        # Move the pointers towards the end, with fast pointer moving faster
        # This will locate the middle
        while (fast) and (fast.next): 
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        second = slow.next      # This marks the first node of second half of the list 
        slow.next = None        # This marks the middle node's next pointer to be empty
        prev = None
        while second: 
            tmp = second.next
            second.next = prev 
            prev = second
            second = tmp
        
        # Merge two halves; reset the pointers to first element of their respective halves 
        first = head
        second = prev 
        
        while second: 
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

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