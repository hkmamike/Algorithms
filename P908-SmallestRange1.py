class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxVal = max(A)
        minVal = min(A)
        midVal = (maxVal+minVal) // 2
        
        for i in range(len(A)):
            if A[i] > midVal:
                A[i] = A[i] - min(A[i]-midVal, K)
            else:
                A[i] = A[i] + min(midVal-A[i], K)
            
        newMax = max(A)
        newMin = min(A)
            
        return newMax - newMin
        