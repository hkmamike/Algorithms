class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)-1
        
        even = 0
        odd = 1
        
        while even <= length or odd <= length:
            
            while even <= length and A[even] % 2 == 0:
                even += 2
                
            while odd <= length and A[odd] % 2 == 1:
                odd += 2
            
            if even <= length and odd <= length:
                A[even], A[odd] = A[odd], A[even]
            
        return A