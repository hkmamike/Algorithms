class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        results = []
        
        if len(S) == 0:
            return results
        
        currentChar = S[0]
        currentSize = 1
        
        for i in range(1, len(S)):
            
            if S[i] == currentChar:
                currentSize += 1
            else:
                if currentSize <= 2:
                    currentChar = S[i]
                    currentSize = 1
                else:
                    results.append([i-currentSize, i-1])
                    currentChar = S[i]
                    currentSize = 1
                    
        if currentSize >= 3:
            results.append([i-currentSize+1, i])
                    
        return results
                    