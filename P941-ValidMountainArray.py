class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        
        peaked = False
        
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return False
            elif not peaked:
                if A[i] < A[i-1]:
                    peaked = True
            elif A[i] > A[i-1]:
                return False
            
        maxVal = max(A)
        return maxVal != A[0] and maxVal != A[-1]
                
        
        