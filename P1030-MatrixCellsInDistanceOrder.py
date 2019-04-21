class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        def distance(pt1, pt2):
            return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
        
        h = []
        for r in range(R):
            for c in range(C):
                d = distance((r,c), (r0, c0))
                heapq.heappush(h,(d, r, c))
            
        result = []
        while len(h) > 0:
            smallest = heapq.heappop(h)
            result.append([smallest[1], smallest[2]])
            
        return result
            