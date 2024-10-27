class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        MOD = 10**9 + 7
        dp = [[0] * 26 for _ in range(2)]
        for c in range(26):
            dp[0][c] = 1

        for time in range(1, t+1):
            # rolling array technique to throw old dp rows away
            curr = time % 2
            prev = (time - 1) % 2

            for c in range(26):
                if c != 25:
                    dp[curr][c] = dp[prev][(c+1) % 26]
                else:
                    dp[curr][c] = (dp[prev][0] + dp[prev][1]) % MOD
            for c in range(26):
                dp[curr][c] %= MOD

        result = 0
        curr = t % 2
        for c in s:
            idx = ord(c) - ord("a")
            result = (result + dp[curr][idx]) % MOD
        return result