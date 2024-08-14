class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistanceFromOrigin(x1, y1):
            return pow(pow(x1, 2) + pow(y1, 2) , 0.5)

        heap = []
        for p in points:
            d = getDistanceFromOrigin(p[0], p[1])
            if len(heap) < k:
                heapq.heappush(heap, (-d, p[0], p[1]))
            else:
                heapq.heappushpop(heap, (-d, p[0], p[1]))

        return [[h[1], h[2]] for h in heap]

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