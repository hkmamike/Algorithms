
# Oct 24, tried trie first but got stuck, had to look at hints
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # def buildTrie(self, wordDict):
        #     self.root = {}
        #     for word in wordDict:
        #         node = self.root
        #         for c in word + "$":
        #             node = node.setdefault(c, {})
        # buildTrie(self, wordDict)

        dp = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                isBeginning = (i-len(w) == -1)
                isAfterValid = (i-len(w) >= 0) and dp[i-len(w)]
                if w == s[i - len(w) + 1 : i+1] and (isBeginning or isAfterValid):
                    dp[i] = True
        return dp[-1]

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