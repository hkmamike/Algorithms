class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        c = collections.Counter({0: 1})
        
        result = 0
        preSum = 0
        for a in A:
            preSum += a
            result += c[preSum - S]
            c[preSum] += 1
            
        return result
            
                

            