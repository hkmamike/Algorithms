class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        visitOrder = []
        directions = {(0, 1):(-1, 0), (-1, 0):(0, -1), (0, -1):(1, 0), (1, 0):(0, 1)}
        self.posAt = (r0, c0)
        visited = set()
        
        def findNext(r, c):            
            if all([ (i, j) not in visited for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]]):
                return (r, c+1)
            else:
                found = False
                check = (r, c+1)
                direction = (0, 1)
                
                while True:
                    if found and check not in visited:
                        return check
                    elif check in visited:
                        found = True

                    direction = directions[direction]
                    check = (r+direction[0], c+direction[1])
        
        def explore(r, c):
            if 0 <= r < R and 0 <= c < C:
                visitOrder.append([r, c])
            visited.add((r, c))
            self.posAt = findNext(r, c)
        
        while len(visitOrder) < R*C:
            explore(self.posAt[0], self.posAt[1])
            
        return visitOrder
        