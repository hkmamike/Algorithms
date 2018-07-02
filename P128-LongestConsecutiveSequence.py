class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        best = 0
        
        for num in nums:
            if num-1 not in numSet:
                y = num + 1
                
                while y in numSet:
                    y += 1
                    
                best = max(best, y-num)
                
        return best