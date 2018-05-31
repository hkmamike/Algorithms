class Solution:
    def findDisappearedNumbers(self, nums):

        valuesSet = set()
        n = len(nums)
        result = []
        
        for num in nums:
            if num in valuesSet:
                continue
            else:
                valuesSet.add(num)
                
        for i in range(1, n+1):
            if i not in valuesSet:
                result.append(i)
                
        return result