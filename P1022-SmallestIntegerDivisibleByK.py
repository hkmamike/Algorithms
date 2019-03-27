class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        
        if (K % 2 == 0 or K % 5 == 0): 
            return -1
        r = 0
        N = 1
        while True:
            r = (r * 10 + 1) % K
            if not r:
                return N
            N += 1