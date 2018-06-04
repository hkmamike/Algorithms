class Solution:
    def maxChunksToSorted(self, arr):
        sortedArr = sorted(arr)
        sortedSet = {}
        arrSet = {}
        count = 0
        
        for i in range(len(arr)):
            if sortedArr[i] in sortedSet:
                sortedSet[sortedArr[i]] += 1
            else:
                sortedSet[sortedArr[i]] = 1
                
            if arr[i] in arrSet:
                arrSet[arr[i]] += 1
            else:
                arrSet[arr[i]] = 1
            
            if sortedSet == arrSet:
                count += 1
                sortedSet = {}
                arrSet = {}
                
        return count