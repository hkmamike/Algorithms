class Solution:
    def buildTrie(self, words):
        self.root = {}
        for word in words:
            node = self.root
            for c in word + "$":
                node = node.setdefault(c, {})

    def minValidStrings(self, words: List[str], target: str) -> int:
        self.buildTrie(words)
        n = len(target)
        dp = [inf] * (n + 1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            node = self.root
            for j in range(i, n):
                if target[j] in node:
                    node = node[target[j]]
                else:
                    break
                dp[i] = min(dp[i], dp[j+1] + 1)

        return dp[0] if dp[0] < inf else -1
