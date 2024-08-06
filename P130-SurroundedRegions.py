
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def onEdge(r, c, H, W):
            return r == 0 or r == H-1 or c == 0 or c == W-1

        def move(r, c, H, W):
                for (i, j) in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0 <= r+i < H and 0 <= c+j < W:
                        yield (r+i, c+j)
            
        def visit(r, c, board, H, W):
            if board[r][c] == "O":
                board[r][c] = "E"
                for (R, C) in move(r, c, H, W):
                    visit(R, C, board, H, W)

        H = len(board)
        W = len(board[0])
        
        for r in range(H):
            for c in range(W):
                if onEdge(r, c, H, W) and board[r][c] == "O":
                    visit(r, c, board, H, W)
        
        for r in range(H):
            for c in range(W):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"



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
                    
