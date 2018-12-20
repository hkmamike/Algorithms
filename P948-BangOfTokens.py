class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        result = 0
        currency = 0
        d = collections.deque(sorted(tokens))
        
        while d and (d[0] <= P or currency):
            if d[0] <= P:
                P -= d.popleft()
                currency += 1
            else:
                P += d.pop()
                currency -= 1
            result = max(result, currency)

        return result
        