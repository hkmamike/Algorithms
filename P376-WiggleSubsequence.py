class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp = [0] * len(nums) #dp[i] is the longest subsequence ending at i
        diff = [0] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
        
                if i == j or nums[i] == nums[j]:
                    dp[j] = max(dp[j], 1)
                elif nums[i] < nums[j] and diff[i] < 0:
                    dp[j] = max(dp[i]+1, dp[j])
                    if dp[j] == dp[i]+1:
                        diff[j] = nums[j] - nums[i]
                elif nums[i] > nums[j] and diff[i] > 0:
                    dp[j] = max(dp[i]+1, dp[j])
                    if dp[j] == dp[i]+1:
                        diff[j] = nums[j] - nums[i]
                else:
                    dp[j] = max(dp[j], 2)
                    if dp[j] == 2:
                        diff[j] = nums[j] - nums[i]
                        
        return max(dp)
                    