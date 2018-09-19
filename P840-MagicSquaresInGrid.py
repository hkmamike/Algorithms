class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(grid, r, c):
            allowed = set([1,2,3,4,5,6,7,8,9])
            
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] not in allowed:
                        return False
                    else:
                        allowed.remove(grid[i][j])
            
            row1 = (grid[r][c] + grid[r][c+1] + grid[r][c+2])
            row2 = (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2])
            row3 = (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2])
            col1 = (grid[r][c] + grid[r+1][c] + grid[r+2][c])
            col2 = (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1])
            col3 = (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2])
            d1 = (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2])
            d2 = (grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2])
            
            
            
            print(row1,row2,row3,col1,col2,col3,d1,d2)
            
            return row1 == row2 == row3 == col1 == col2 == col3 == d1 == d2
        
        height = len(grid)
        width = len(grid[0])
        
        count = 0
        
        for r in range(height-2):
            for c in range(width-2):
                if isMagic(grid,r,c):
                    count += 1
                    
        return count