class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height)-1
        maxWater = 0

        while i < j:
            waterHeight = min(height[i], height[j])
            waterWidth = j-i
            maxWater = max(maxWater, waterHeight * waterWidth)

            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

        return maxWater
