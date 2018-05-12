#!/usr/bin/python

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        
        rowMax = []
        colMax = []
        
        for i in range(r):
            maxInRow = max(grid[i])
            rowMax.append(maxInRow)
            
        for i in range(c):
            maxInCol = grid[0][i]
            for j in range(1,r):
                if grid[j][i] > maxInCol:
                    maxInCol = grid[j][i]
            colMax.append(maxInCol)
        
        count = 0
            
        for i in range(r):
            for j in range(c):
                maxHeight = min(rowMax[i], colMax[j])
                count = count + maxHeight - grid[i][j]
                
        return count
        