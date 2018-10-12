class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = 0
        maxSum = -float('inf')
        curMax = 0
        minSum = float('inf')
        curMin = 0
        
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            
            total += a
        
        if maxSum > 0:
            return max(maxSum, total - minSum)
        else:
            return maxSum
        