# Sep 23, 2024
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return pow((pow(x, 2) + pow(y, 2)), 0.5)
        
        h = []
        for p in points:
            d = distance(p[0], p[1])

            if len(h) < k:
                heappush(h, (-d, p[0], p[1]))
            else:
                heappushpop(h, (-d, p[0], p[1]))
        
        return [[e[1], e[2]] for e in h]

# Aug 13, 2024
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