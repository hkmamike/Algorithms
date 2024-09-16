class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[float('-inf')] * 5 for _ in range(n + 1)]
        dp[0][0] = 0

        for r in range(1, n + 1):
            for c in range(5):
                dp[r][c] = dp[r-1][c]
    
                if c > 0:
                    dp[r][c] = max(dp[r][c], dp[r-1][c-1] + a[c-1] * b[r-1])
        return dp[n][4]
