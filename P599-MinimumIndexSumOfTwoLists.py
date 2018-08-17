class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        listMap = {}
        for i,entry in enumerate(list1):
            listMap[entry] = [i]
            
        for i,entry in enumerate(list2):
            if entry in listMap:
                listMap[entry].append(i)
                
        minIndexSum = len(list1) + len(list2)
        
        for entry in listMap:
            if len(listMap[entry]) > 1:
                entrySum = sum(listMap[entry])
                minIndexSum = min(minIndexSum, entrySum)
                
        results = []
        
        for entry in listMap:
            if len(listMap[entry]) > 1:
                entrySum = sum(listMap[entry])
                if entrySum == minIndexSum:
                    results.append(entry)
                    
        return results
        