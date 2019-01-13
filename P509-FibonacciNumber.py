class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        resultArray = [0, 1]
        
        if N < 2:
            return resultArray[N]
        
        for i in range(2, N+1):
            resultArray.append(resultArray[i-1] + resultArray[i-2])
            
        return resultArray[N]
        