class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def explore(matrix, r, c):
            values = []
            originalVal = matrix[r][c]
            if r >= 1:
                values.append(matrix[r-1][c])
            if r < len(matrix) - 1: 
                values.append(matrix[r+1][c])
            if c >= 1: 
                values.append(matrix[r][c-1])
            if c < len(matrix[0]) - 1: 
                values.append(matrix[r][c+1])
                
            matrix[r][c] = min(values) + 1
            
            if matrix[r][c] != originalVal:
                return True
            else:
                return False
            
        continueFlag = True
        while continueFlag:
            continueFlag = False
            
            for r in range(len(matrix)):
                for c in range(len(matrix[0])):
                    if matrix[r][c] != 0:
                        if explore(matrix, r, c):
                            continueFlag = True
                            
        return matrix