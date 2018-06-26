class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        
        for h in range(12):
            for m in range(60):
                oneCount = (bin(h) + bin(m)).count('1') 
                if oneCount == num:
                    result.append('%d:%02d' % (h, m)) 
                    
        return result
        