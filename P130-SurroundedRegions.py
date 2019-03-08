class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            
            height = len(board)
            width = len(board[0])

            def move(y, x):
                for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
                    if 0 <= y + i < height and 0 <= x + j < width:
                        yield (y + i , x + j)

            def dfs(x, y):
                if board[x][y] == "O":
                    board[x][y] = "Y"

                    for r, c in move(x, y):
                        dfs(r, c)

            for r in range(height):
                dfs(r, 0)
                dfs(r, width-1)

            for c in range(width):
                dfs(0, c)
                dfs(height-1, c)

            for r in range(height):
                for c in range(width):
                    if board[r][c] == "O":
                        board[r][c] = "X"
                    
                    if board[r][c] == "Y":
                        board[r][c] = "O"
                    
