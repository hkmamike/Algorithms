class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binN = bin(N)
        onePos = []
        maxD = 0
        
        for i, char in enumerate(binN):
            if char == '1':
                onePos.append(i)
        
        if len(onePos) <= 1:
            pass
        else:
            start = onePos[0]
            for i in range(1, len(onePos)):
                distance = onePos[i] - onePos[i-1]
                maxD = max(maxD, distance)
                
        return maxD
        