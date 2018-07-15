class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        sumSoFar = []
        sumMap = {}
        tempSum = 0
        count = 0
        
        for i, num in enumerate(nums):
            tempSum += num
            sumSoFar.append(tempSum)
            
            if tempSum in sumMap:
                sumMap[tempSum].append(i)
            else:
                sumMap[tempSum] = [i]
                
        for i in range(len(sumSoFar)):
            if sumSoFar[i] == k:
                count += 1
            
            target = sumSoFar[i] - k
            if target in sumMap:
                for index in sumMap[target]:
                    if index < i:
                        count += 1
                        
        return count