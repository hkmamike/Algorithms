class Solution:
    def peakIndexInMountainArray(self, A):  
        for i in range(len(A)):
            if A[i+1] < A[i]:
                return i