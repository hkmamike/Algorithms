class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sortedA = sorted(A)
        moves = 0
        need = 0
        
        for i in sortedA:
            moves += max(need-i, 0)
            need = max(i+1, need+1)        
            
        return moves