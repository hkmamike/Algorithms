
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        dp = [0] * N
        dp[0] = 0
        d = deque([0])

        for j in range(1, N):
            while d and ((j - d[0]) * nums[d[0]] + dp[d[0]]) < ((j - d[-1]) * nums[d[-1]] + dp[d[-1]]):
                d.popleft()

            i = d[0]
            dp[j] = max(dp[j], dp[i] + (j - i) * nums[i])
            d.append(j)
        
        return dp[-1]

# TLE
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        TLE
        dp = [0] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dp[j] = max(dp[j], (j-i) * nums[i] + dp[i])
        return dp[-1]