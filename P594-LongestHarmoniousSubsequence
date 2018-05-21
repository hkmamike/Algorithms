class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        LHS = 0
        
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for value in hashMap:
            if value+1 in hashMap:
                LHS = max(LHS, hashMap[value] + hashMap[value+1])
                
        return LHS