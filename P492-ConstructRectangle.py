import math

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        sqRoot = math.floor(area**0.5)
        
        for width in range(sqRoot,-1,-1):
            
            length = area / width
            
            if length.is_integer():
                return [int(length), width]
            