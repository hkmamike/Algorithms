class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def isExit(r, c):
            if r == R and c == C:
                return False
            return r == 0 or r == (len(maze) - 1) or c == 0 or c == (len(maze[0]) - 1)

        def nearbyCells(r, c):
            neighbors = []
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (r+i, c+j) not in self.visited and 0 <= r+i < len(maze) and 0 <= c+j < len(maze[0]) and maze[r+i][c+j] == ".":
                    neighbors.append((r+i, c+j))
                    self.visited.add((r+i, c+j))
            return neighbors

        R, C = entrance
        steps = 0
        self.visited = set()
        self.visited.add((R, C))
        Q = [(R, C)]
        loopFlag = True

        while loopFlag:
            loopFlag = False
            nextQ = []
            while len(Q) > 0:
                r, c = Q.pop()
                if isExit(r, c):
                    return steps
                else:
                    nextQ.extend(nearbyCells(r, c))

            if len(nextQ) > 0:
                Q = nextQ
                steps += 1
                loopFlag = True

        return -1