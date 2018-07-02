class Solution:
    def gameOfLife(self, board):
        h = len(board)
        w = len(board[0])
        
        for r in range(h):
            for c in range(w):
                if board[r][c] == 0:
                    if self.countNeighbors(board, r, c) == 3:
                        board[r][c] = 2
                else:
                    liveNeighbors = self.countNeighbors(board, r, c)
                    if liveNeighbors < 2 or liveNeighbors > 3:
                        board[r][c] = 3
                        
        for r in range(h):
            for c in range(w):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0
        
    def countNeighbors(self,board,r,c):
        count = 0
        h = len(board)
        w = len(board[0])
        
        if r>=1: count += board[r-1][c] % 2
        if r<=h-2: count += board[r+1][c] % 2
        if c>=1: count += board[r][c-1] % 2
        if c<=w-2: count += board[r][c+1] % 2
            
        if r>=1 and c>=1: count += board[r-1][c-1] % 2
        if r<=h-2 and c<=w-2: count += board[r+1][c+1] % 2
        if r>=1 and c<=w-2: count += board[r-1][c+1] % 2
        if r<=h-2 and c>=1: count += board[r+1][c-1] % 2
            
        return count