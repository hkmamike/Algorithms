class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        N = len(nums)
        count, maxCnt = 1, 1
        
        for i in range(1, N):
            if  nums[i] > nums[i-1]:
                count += 1
            else:
                maxCnt = max(maxCnt, count)
                count = 1
                
        maxCnt = max(maxCnt, count)
                
        return maxCnt