# practice on optimal solution - Sep 26
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumSum, result = 0, 0
        numSubarrayWithSum = {}
        for i, n in enumerate(nums):
            cumSum += n

            if cumSum == k:
                result += 1
            if cumSum - k in numSubarrayWithSum:
                result += numSubarrayWithSum[cumSum - k]
            if cumSum in numSubarrayWithSum:
                numSubarrayWithSum[cumSum] += 1
            else:
                numSubarrayWithSum[cumSum] = 1
        return result

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
