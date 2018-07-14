class Solution:
    
    def largestOnRow(self, columnHeights):
        hStack = [columnHeights[0]]
        posStack = [0]
        maxOnRow = 0
        
        for i, h in enumerate(columnHeights[1:],1):
            if h == hStack[-1]:
                continue
            elif h > hStack[-1]:
                hStack.append(h)
                posStack.append(i)
            else:
                while len(hStack) > 0 and hStack[-1] > h:
                    height = hStack.pop()
                    pos = posStack.pop()
                    maxOnRow = max(maxOnRow, height * (i - pos))
                    # print(maxOnRow, height, i, pos)
                    
                hStack.append(h)
                posStack.append(pos)
            
        # print(posStack, hStack)
        while len(hStack) > 0:
            height = hStack.pop()
            position = posStack.pop()
            maxOnRow = max(maxOnRow, height*(len(columnHeights)-position))
        
        # print(columnHeights, maxOnRow)
        return maxOnRow 
        
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        H = len(matrix)
        W = len(matrix[0])
        
        columnHeights = [0] * W
        maxArea = 0
        
        for r in range(H):
            for c in range(W):
                if matrix[r][c] == '1':
                    columnHeights[c] += 1
                else:
                    columnHeights[c] = 0
                    
            area = self.largestOnRow(columnHeights)
            maxArea = max(maxArea, area)
            # print(maxArea)

        return maxArea