class Solution:
    def spiralOrder(self, matrix):

        if not matrix:
            return []
        
        turn = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}
        m = len(matrix)
        n = len(matrix[0])
        
        pos = [0, 0]
        direction = (0, 1)
        result = [matrix[0][0]]
        
        visited = set()
        visited.add((0,0))
        
        while len(result) < ( m * n ):
            
            nextRow = pos[0] + direction[0]
            nextCol = pos[1] + direction[1]
            
            if (nextRow > m-1
                or nextRow < 0
                or nextCol > n-1
                or nextCol < 0
                or (nextRow, nextCol) in visited):
                
                    direction = turn[direction]
                    nextRow = pos[0] + direction[0]
                    nextCol = pos[1] + direction[1]
                
            result.append(matrix[nextRow][nextCol])
            visited.add((nextRow,nextCol))
            pos = [nextRow, nextCol]

        return result