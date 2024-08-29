class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def isOutofBound(r, c, M, N):
            if r < 0 or r > M - 1:
                return True
            if c < 0 or c > N - 1:
                return True
            return False

        def isVisited(r, c, visited):
            if (r, c) in visited:
                return True
            return False

        dirMap = {(0, 1):(1, 0), (1, 0):(0, -1), (0, -1):(-1, 0), (-1, 0):(0, 1)}
        M = len(matrix)
        N = len(matrix[0])
        visited = set()
        visited.add((0, 0))
        total = M * N
        cnt = 1
        result = [matrix[0][0]]
        curPos = [0, 0]
        curDir = [0, 1]

        while cnt < total:
            nextCandidate = [curPos[0] + curDir[0], curPos[1] + curDir[1]]

            # turn if we hit a wall
            if isOutofBound(nextCandidate[0], nextCandidate[1], M, N) or isVisited(nextCandidate[0], nextCandidate[1], visited):
                curDir[0], curDir[1] = dirMap[(curDir[0], curDir[1])]
                nextCandidate = [curPos[0] + curDir[0], curPos[1] + curDir[1]]
            
            result.append(matrix[nextCandidate[0]][nextCandidate[1]])
            visited.add((nextCandidate[0], nextCandidate[1]))
            curPos[0] = nextCandidate[0]
            curPos[1] = nextCandidate[1]
            cnt += 1

        return result

        

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