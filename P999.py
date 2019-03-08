class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def findRook(board):
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == 'R':
                        return (r, c)
        
        rookPos = findRook(board)
        counter = 0
            
        for r in range(rookPos[0], len(board)):
            if board[r][c] == 'B':
                break
            elif board[r][c] == 'p':
                counter += 1
                break
                
        for r in range(rookPos[0], -1, -1):
            if board[r][c] == 'B':
                break
            elif board[r][c] == 'p':
                counter += 1
                break
                
        for c in range(rookPos[1], len(board[0])):
            if board[r][c] == 'B':
                break
            elif board[r][c] == 'p':
                counter += 1
                break
                
        for c in range(rookPos[1], -1, -1):
            if board[r][c] == 'B':
                break
            elif board[r][c] == 'p':
                counter += 1
                break
                
        return counter