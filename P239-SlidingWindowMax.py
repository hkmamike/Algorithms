import heapq

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        current = collections.deque(nums[0:k])
        result = [max(current)]
        
        for i in range(k,len(nums)):
            current.popleft()
            current.append(nums[i])
            result.append(max(current))
            
        return result