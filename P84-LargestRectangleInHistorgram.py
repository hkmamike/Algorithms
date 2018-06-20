class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        else:
            posStack, hStack, maxA, length = [0], [heights[0]], 0, len(heights)
            
        for i in range(1, length):
            if heights[i] == hStack[-1]:
                continue
            elif heights[i] > hStack[-1]:
                posStack.append(i)
                hStack.append(heights[i])
            else:
                while hStack and hStack[-1] > heights[i]:
                    height = hStack.pop()
                    start = posStack.pop()
                    width = i - start
                    maxA = max(maxA, height*width)
                    
                posStack.append(start)
                hStack.append(heights[i])
                
        while hStack:
            height = hStack.pop()
            start = posStack.pop()
            width = length - start
            maxA = max(maxA, height*width)
            
        return maxA