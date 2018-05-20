class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        length = len(grid[0])
        count = 0
        
        for r in range(height):
            isGround = False
            
            for c in range(length):
                if isGround and grid[r][c] == 0:
                    count += 1
                    isGround = False
                elif not isGround and grid[r][c] == 1:
                    count += 1
                    isGround = True
                    
            if grid[r][c] == 1:
                count += 1
                    
        for c in range(length):
            isGround = False
            
            for r in range(height):
                if isGround and grid[r][c] == 0:
                    count += 1
                    isGround = False
                elif not isGround and grid[r][c] == 1:
                    count += 1
                    isGround = True
                    
            if grid[r][c] == 1:
                count += 1
                    
        return count
        