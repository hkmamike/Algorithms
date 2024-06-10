# easier to understand
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

# more efficient
class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        safeLevel = 0
        totalWater = 0

        while L < R:
            lower = min(height[L], height[R])
            safeLevel = max(safeLevel, lower)
            totalWater += safeLevel - lower

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return totalWater