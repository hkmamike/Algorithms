class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def getDistance(point):
            return ( point[0]**2 + point[1]**2 ) ** 0.5
        
        points = sorted(points, key=lambda point: getDistance(point))
        
        return points[0: K]