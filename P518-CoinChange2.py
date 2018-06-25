class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ways = [0] * (amount + 1)
        ways[0] = 1
        
        for c in coins:
            for i in range(c, amount + 1):
                ways[i] += ways[i-c]
                
        return ways[-1]