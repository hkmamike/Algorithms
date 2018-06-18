class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        heights = [0] + height + [0]
        length = len(heights)
        right = [0 for _ in range(length)]
        left = [0 for _ in range(length)]
        water = [0 for _ in range(length)]
        
        for i in range(1, length):
            left[i] = max(left[i-1], heights[i])
            
        for i in range(length-2, -1, -1):
            right[i] = max(right[i+1], heights[i])
            
        for i in range(length):
            water[i] = max(0, min( left[i], right[i] ) - heights[i])
            
        return sum(water)