class Solution:
    def dailyTemperatures(self, temperatures):
        
        result = [ 0 for _ in range(len(temperatures))]
        stackTemp = []
        stackIndex = []
        
        for i, entry in enumerate(temperatures):
            
            while stackTemp and entry > stackTemp[-1]:
                index = stackIndex.pop()
                result[index] = i - index
                stackTemp.pop()
                
            stackTemp.append(entry)
            stackIndex.append(i)
            
        return result
                    
                