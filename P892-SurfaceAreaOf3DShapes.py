class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        result = 0
        
        for r in range(height):
            for c in range(width):
                if grid[r][c] != 0:
                    result += 2
        
        for r in range(height):
            for c in range(1, width):
                result += abs(grid[r][c] - grid[r][c-1])
                
            result += grid[r][0]
            result += grid[r][width-1]
            
        for c in range(width):
            for r in range(1, height):
                result += abs(grid[r][c] - grid[r-1][c])
                
            result += grid[0][c]
            result += grid[height-1][c]
            
        return result
        