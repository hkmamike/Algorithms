
# TLE N^2
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                subArraySum = prefixSum[j+1] - prefixSum[i]
                if subArraySum == 0 or subArraySum % k == 0:
                    return True
        return False
