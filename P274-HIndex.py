class Solution:
    def hIndex(self, citations):
        
        citations = sorted(citations)
        length = len(citations)
        
        for i in range(0, length):
            if citations[i] >= length - i:
                return length-i
        
        return 0