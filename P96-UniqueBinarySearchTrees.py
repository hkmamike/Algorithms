class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return [1,1,2][n]

        def calculateI (results, i):
            for j in range(1, i+1):
                results[i] = results[i] + results[j-1] * results[i-j]
                
        results = [0] * (n+1)
        results[0] = 1
        results[1] = 1
        results[2] = 2

        for i in range(3, n+1):
            calculateI(results, i)
            
        return results[n]