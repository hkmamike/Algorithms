class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        r = 0
        c = width-1
        
        while r <= height-1 and c >= 0:
            print(r, c)
            if matrix[r][c] == target:
                return True
            
            elif matrix[r][c] > target:
                c -= 1
            
            elif matrix[r][c] < target:
                r += 1
            
        return False