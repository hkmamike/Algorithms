class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        bestAt = [1] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                continue
            bestLeft = max([bestAt[j] if nums[j] < n else 0 for j in range(i)])
            bestAt[i] = bestLeft + 1
        
        return max(bestAt)
 