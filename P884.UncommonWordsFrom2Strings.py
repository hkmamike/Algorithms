class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        mapFreq = {}
        result = []
        A = A.split()
        B = B.split()
        
        for char in A:
            if char in mapFreq:
                mapFreq[char] += 1
            else:
                mapFreq[char] = 1
                
        for char in B:
            if char in mapFreq:
                mapFreq[char] += 1
            else:
                mapFreq[char] = 1
                
        for entry in mapFreq:
            if mapFreq[entry] == 1:
                result.append(entry)
                
        return result
        