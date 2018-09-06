class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumSoFar = 0
        count = 0
        sumsMap = {}
        
        for i in range(len(nums)):
            sumSoFar += nums[i]
            
            if sumSoFar == k:
                count += 1
            
            if (sumSoFar - k) in sumsMap:
                count += sumsMap[sumSoFar - k]
                
            if sumSoFar in sumsMap:
                sumsMap[sumSoFar] += 1
            else:
                sumsMap[sumSoFar] = 1
                
        return count 