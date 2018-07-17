class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        indexMap = {}
        for i, num in enumerate(nums):
            indexMap[num] = i
        
        sortedKeys = sorted(indexMap, key=lambda x: x, reverse=True)
        
        result = [0 for _ in range(len(nums))]
        
        for i, key in enumerate(sortedKeys):
            if i == 0:
                rank = 'Gold Medal'
            elif i == 1:
                rank = 'Silver Medal'
            elif i == 2:
                rank = 'Bronze Medal'
            else:
                rank = str(i+1)
            
            result[indexMap[key]] = rank
            
        return result