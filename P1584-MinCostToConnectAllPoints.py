class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        N = len(points)
        C = defaultdict(list)

        for i in range(N):
            for j in range(i+1, N):
                d = distance(points[i], points[j])
                C[i].append((d, j))
                C[j].append((d, i))
        
        numPtAdded = 1
        mstCost = 0
        visited = [0] * N
        h = C[0]

        visited[0] = 1
        heapq.heapify(h)

        while h:
            d, nextPt = heapq.heappop(h)
            if not visited[nextPt]:
                visited[nextPt] = 1
                numPtAdded += 1
                mstCost += d

                for entry in C[nextPt]:
                    heapq.heappush(h, entry)
            if numPtAdded == N:
                break
        return mstCost