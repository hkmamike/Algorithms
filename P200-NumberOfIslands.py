class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        H = len(grid)
        W = len(grid[0])
        count = 0
        visited = grid.copy()
        
        def visitIsland(grid, visited, r, c):
            if grid[r][c] == '1':
                visited[r][c] = -1
                
                if r-1 >= 0: 
                    visitIsland(grid, visited, r-1, c)
                if r+1 <= H-1: 
                    visitIsland(grid, visited, r+1, c)
                if c-1 >= 0: 
                    visitIsland(grid, visited, r, c-1)
                if c+1 <= W-1: 
                    visitIsland(grid, visited, r, c+1)
        
        for r in range(H):
            for c in range(W):
                if visited[r][c] != -1 and grid[r][c] == '1':
                    count += 1
                    visitIsland(grid, visited, r, c)
                    
        return count