class Solution:
    def maxWidthRamp(self, A):
        
        s = []
        res = 0
        
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
                
                
        for j in range(len(A)-1, -1, -1):
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
                
                
        return res