class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        left, right, sumSoFar = 0, 0, 0
        lenAll = len(nums)
        minSoFar = lenAll + 1
        
        while right < len(nums):
            sumSoFar += nums[right]
            right += 1
            
            while sumSoFar >= s:
                minSoFar = min(minSoFar, right-left)
                sumSoFar -= nums[left]
                left += 1
                
        if minSoFar == lenAll + 1:
            return 0
        else:
            return minSoFar
        