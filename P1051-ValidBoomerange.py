class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        def line(p1, p2):
            p1x = p1[0]
            p1y = p1[1]
            p2x = p2[0]
            p2y = p2[1]
            
            xDiff = abs(p2x - p1x)
            # print(xDiff, xDiff == 0)
            if xDiff == 0:
                return (None, None, p1x, None)
            
            yDiff = abs(p2y - p1y)
            if yDiff == 0:
                return (None, None, None, p1y)
            
            slope = yDiff / xDiff
            # print('intercept: ', p1y, slope, p1x, yDiff, xDiff)
            if p1x == 0:
                intercept = p1y
            else:
                intercept = p1y / (slope * p1x)
            
            return (slope, intercept, None, None)
        
        ptSet = set()
        for pt in points:
            ptSet.add((pt[0], pt[1]))
        
        if len(ptSet) != 3:
            return False
        
        # print(line(points[0], points[1]), line(points[1], points[2]), line(points[0], points[1]) != line(points[1], points[2]))
        
        return line(points[0], points[1]) != line(points[1], points[2])