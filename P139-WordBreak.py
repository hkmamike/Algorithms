class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1 : i+1] and (dp[i-len(w)] or i-len(w) == -1):
                    dp[i] = True
                    
        return dp[-1]