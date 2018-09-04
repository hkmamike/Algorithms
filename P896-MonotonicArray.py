class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def sign(thisVal, lastVal):
            if thisVal > lastVal:
                return 1
            elif thisVal < lastVal:
                return -1
            
        direction = 0
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                signVal = sign(A[i], A[i-1])
                if direction != 0 and direction != signVal:
                    return False
                direction = signVal
            
        return True
            
        