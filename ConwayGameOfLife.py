class Solution:
    
    def nextGen(self, state, m, h, w):
        
        if m == 0:
            return state
        
        def checkDeadRules(state, r, c):
            liveNeighbors = 0
            
            ## verticals and horizontals
            if r >= 1:
                if state[r-1][c] == 1:
                    liveNeighbors += 1
            if r <= w-2:
                if state[r+1][c] == 1:
                    liveNeighbors += 1
            if c >= 1:
                if state[r][c-1] == 1:
                    liveNeighbors += 1
            if c <= w-2:
                if state[r][c+1] == 1:
                    liveNeighbors += 1
                    
            ## diagonals
            if r >= 1:
                if c >= 1:
                    if state[r-1][c-1] == 1:
                        liveNeighbors += 1
                if c <= w-2:
                    if state[r-1][c+1] == 1:
                        liveNeighbors += 1
            if r <= w-2:
                if c >= 1:
                    if state[r+1][c-1] == 1:
                        liveNeighbors += 1
                if c <= w-2:
                    if state[r+1][c+1] == 1:
                        liveNeighbors += 1
            
            return liveNeighbors == 3
        
        def checkLiveRules(state, r, c):
            liveNeighbors = 0
            
            ## verticals and horizontals
            if r >= 1:
                if state[r-1][c] == 1:
                    liveNeighbors += 1
            if r <= w-2:
                if state[r+1][c] == 1:
                    liveNeighbors += 1
            if c >= 1:
                if state[r][c-1] == 1:
                    liveNeighbors += 1
            if c <= w-2:
                if state[r][c+1] == 1:
                    liveNeighbors += 1
                    
            ## diagonals
            if r >= 1:
                if c >= 1:
                    if state[r-1][c-1] == 1:
                        liveNeighbors += 1
                if c <= w-2:
                    if state[r-1][c+1] == 1:
                        liveNeighbors += 1
            if r <= w-2:
                if c >= 1:
                    if state[r+1][c-1] == 1:
                        liveNeighbors += 1
                if c <= w-2:
                    if state[r+1][c+1] == 1:
                        liveNeighbors += 1
            
            if liveNeighbors < 2:
                return 0
            elif liveNeighbors < 4:
                return 1
            else:
                return 0
        
        newState = [[0 for _ in range(h)] for _ in range(w)]
        for r in range(h):
            for c in range(w):
                
                if state[r][c] == 0:
                    newState[r][c] = int(checkDeadRules(state, r, c))
                    
                elif state[r][c] == 1:
                    newState[r][c] = int(checkLiveRules(state, r, c))
        
        return self.nextGen(newState, m-1, h, w)
    
    
    
    def conwayGame(self, initialState, n):
        if n == 0:
            return initialState
        
        h = len(initialState)
        w = len(initialState[0])
        
        finalState = self.nextGen(initialState, n, h, w)
        
        print(finalState)
        return finalState
        
    '''
    000    010    000
    111 -> 010 -> 111 -> ...
    000    010    000
    '''
    
n = 2
testState = [[0,0,0],[1,1,1],[0,0,0]]
instance = Solution()
instance.conwayGame(testState, n)