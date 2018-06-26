class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        length = len(citations)
        L = 0
        R = length-1
        
        while L<R:
            M = (L+R) // 2
            
            if citations[M] >= length-M:
                R = M
            else:
                L = M+1
                
        if citations[L] >= length-L:
            return length - L
        else:
            return 0