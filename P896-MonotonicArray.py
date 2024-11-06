class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <= 2:
            return True

        diff = []
        for i in range(1, N):
            diff.append(nums[i] - nums[i-1])
        
        return all([x >= 0 for x in diff]) or all([x <= 0 for x in diff])

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
            
        