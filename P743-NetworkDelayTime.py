class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
                
        edgesMap = collections.defaultdict(list)
        for t in times:
            edgesMap[t[0]].append( (t[1], t[2]) )
                
        
        reachedTimes = {node: float('inf') for node in range(1, N+1)}
        visitedNodes = set([K])
        reachedTimes[K] = 0
        new = K
        
        for _ in range(N-1):
            for target, distance in edgesMap[new]:
                if target not in visitedNodes:
                    reachedTimes[target] = min(reachedTimes[new] + distance, reachedTimes[target])
            
            minDistance = float('inf')
            for i in range(1, N+1):
                if i not in visitedNodes:
                    if reachedTimes[i] < minDistance:
                        new = i
                        minDistance = reachedTimes[i]
                        
            visitedNodes.add(new)
        
        if max(reachedTimes.values()) != float('inf'):
            return max(reachedTimes.values())
        else:
            print(reachedTimes.values())
            return -1
        
            