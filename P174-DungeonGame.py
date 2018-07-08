class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        h = len(dungeon)
        w = len(dungeon[0])
        
        minHealth = [[0 for _ in range(w)] for _ in range(h)]
        minHealth[h-1][w-1] = max(1, 1-dungeon[h-1][w-1])
        
        for r in range(h-2, -1, -1):
            minHealth[r][w-1] = max(1, minHealth[r+1][w-1] - dungeon[r][w-1])
            
        for c in range(w-2, -1, -1):
            minHealth[h-1][c] = max(1, minHealth[h-1][c+1] - dungeon[h-1][c])
            
        for r in range(h-2, -1, -1):
            for c in range(w-2, -1, -1):
                minHealth[r][c] = max(1, min(minHealth[r+1][c], minHealth[r][c+1]) - dungeon[r][c])
                
        return minHealth[0][0]