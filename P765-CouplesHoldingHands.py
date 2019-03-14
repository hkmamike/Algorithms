class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        rowMap = {}
        for i, x in enumerate(row):
            rowMap[x] = i
            
        swapCount = 0
        
        for i in range(0, len(row), 2):
            
            couple1 = row[i]
            if couple1 % 2 == 0:
                couple2 = couple1 + 1
            else:
                couple2 = couple1 - 1
            
            couple2Pos = rowMap[couple2]
            
            if couple2Pos - i > 1:
                row[i+1], row[couple2Pos] = row[couple2Pos], row[i+1]
                rowMap[couple2] = i+1
                rowMap[row[couple2Pos]] = couple2Pos 
                swapCount += 1

                
        return swapCount
    