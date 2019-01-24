class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A) / 2
        hashMap = {}
        
        for entry in A:
            if entry in hashMap:
                hashMap[entry] += 1
            else:
                hashMap[entry] = 1
                
            if hashMap[entry] == N:
                return entry