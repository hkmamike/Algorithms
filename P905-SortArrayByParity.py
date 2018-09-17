class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A) - 1
        
        while left < right:
            if A[left] % 2 != 0:
                A[left], A[right] = A[right], A[left]
                right -= 1
            
            else:
                left += 1
                
        return A