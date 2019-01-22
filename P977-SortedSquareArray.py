class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ASorted = sorted(A, key = lambda x: abs(x))
        
        ASquare = []
        
        for entry in ASorted:
            ASquare.append(entry ** 2)
        
        return ASquare