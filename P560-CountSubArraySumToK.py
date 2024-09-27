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
    
# N^2 TLE simple
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = [0]
        for n in nums:
            prefixSum.append(prefixSum[-1] + n)
        
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subArraySum = prefixSum[j+1]-prefixSum[i]
                if subArraySum == k:
                    result += 1
        return result
