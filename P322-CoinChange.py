class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        need = [0] + [amount + 1] * amount
        
        for c in coins:
            for i in range(c, amount + 1):
                need[i] = min(need[i], need[i-c]+1)
                
        if need[-1] > amount:
            return -1
        else:
            return need[-1]