class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setMark(r, c):
            for R in range(len(matrix)):
                if matrix[R][c] != 0:
                    matrix[R][c] = "-"
            for C in range(len(matrix[0])):
                if matrix[r][C] != 0:
                    matrix[r][C] = "-"
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    setMark(r, c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "-":
                    matrix[r][c] = 0
