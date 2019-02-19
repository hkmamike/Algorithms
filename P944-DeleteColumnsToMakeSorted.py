class Solution:
    def minDeletionSize(self, A: 'List[str]') -> 'int':
        
        count = 0
        
        for c in range(len(A[0])):
            for r in range(1, len(A)):
                if A[r][c] < A[r-1][c]:
                    count += 1
                    break
                    
        return count
            
        