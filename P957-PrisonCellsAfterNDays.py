class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        seen = {str(cells) : N}
        prevCells = cells[:]

        while N > 0:
            seen.setdefault(str(prevCells), N)
            N -= 1
            
            cells[0] = 0
            cells[-1] = 0
            for i in range(1, len(cells)-1):
                if prevCells[i-1] == prevCells[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0
                    
            prevCells = cells[:]
            
            if str(cells) in seen:
                N = N % (seen[str(cells)] - N)
                
        return cells
        