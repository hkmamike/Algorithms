class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def searchFrom(r, c, idx, word, usedSet):
            if r < 0 or c < 0 or r > H-1 or c > W-1:
                return
            elif idx == len(word) - 1:
                if word[idx] == board[r][c] and (r, c) not in usedSet:
                    self.found = True
            elif word[idx] == board[r][c] and (r, c) not in usedSet:
                newSet = usedSet.copy()
                newSet.add((r, c))
                searchFrom(r+1, c, idx + 1, word, newSet)
                searchFrom(r-1, c, idx + 1, word, newSet)
                searchFrom(r, c+1, idx + 1, word, newSet)
                searchFrom(r, c-1, idx + 1, word, newSet)
        
        self.found = False
        H = len(board)
        W = len(board[0])
        for r in range(H):
            for c in range(W):
                searchFrom(r, c, 0, word, set())
        return self.found
