class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        
        def move(r, c):
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r+i < len(A) and 0 <= c+j < len(A[0]):
                    yield (r+i, c+j)
                    
        height = len(A)
        width = len(A[0])
        
        def explore(r, c):
            if A[r][c] == 1:
                A[r][c] = 0
                
                for (y, x) in move(r, c):
                    explore(y, x)
        
        # flip all boundary connecting 1s to 0s
        for r in range(height):
            if A[r][0] == 1:
                explore(r, 0)
            if A[r][width-1] == 1:
                explore(r, width-1)
                
        for c in range(width):
            if A[0][c] == 1:
                explore(0, c)
            if A[height-1][c] == 1:
                explore(height-1, c)
            
        # count 1s
        count = 0
        for r in range(height):
            for c in range(width):
                if A[r][c] == 1:
                    count += 1
                    
        return count
                    