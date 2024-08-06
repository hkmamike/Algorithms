class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        N = len(grid)
        q = deque()
        q.append((0, 0))
        visited = {(0, 0)}

        def move(r, c):
            for (i, j) in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                R = r+i
                C = c+j
                if 0 <= R < N and 0 <= C < N and (R, C) not in visited and grid[R][C] == 0:
                    yield (R, C)

        currentDistance = 1
        while q:
            qCnt = len(q)

            for _ in range(qCnt):
                r, c = q.popleft()

                if r == N-1 and c == N-1:
                    return currentDistance     
           
                for neighbor in move(r, c):
                    visited.add(neighbor)
                    q.append(neighbor)

            currentDistance += 1

        return -1