class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        length = len(A)
        mod = 10 ** 9 + 7
        
        left = [0] * length 
        right = [0] * length
        s1 = []
        s2 = []
        
        for i in range(length):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
            
        for i in range(length)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
            
        minSum = 0
        
        for i in range(length):
            minSum += left[i] * right[i] * A[i]
            
        return minSum % mod
                
        