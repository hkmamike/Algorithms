class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        height = len(triangle)
        
        if height == 0:
            return 0
        elif height == 1:
            return triangle[0][0]
        
        for i in range(height-2, -1, -1):
            width = len(triangle[i])
            for j in range(width):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
                
        return triangle[0][0]