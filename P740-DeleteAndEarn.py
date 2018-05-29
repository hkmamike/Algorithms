class Solution:
    def deleteAndEarn(self, nums):
        
        resultsArray = scoresArray = [0 for _ in range(10001)]
        
        for num in nums:
            scoresArray[num] += num
        
        resultsArray[1] = scoresArray[1]
        resultsArray[2] = max(scoresArray[1], scoresArray[2])
        
        for i in range(3, len(resultsArray)):
            resultsArray[i] = max(resultsArray[i-1], resultsArray[i-2] + scoresArray[i])
            
        return resultsArray[-1]