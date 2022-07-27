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