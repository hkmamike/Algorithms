class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edgesMap = {}
        for entry in times:
            if entry[0] in edgesMap:
                edgesMap[entry[0]].append(tuple(entry))
            else:
                edgesMap[entry[0]] = [tuple(entry)]
        
        
        reachedTimes = [[] for _ in range(N)]
        edgesUsed = set()
        
        def traverse(node, time):
            reachedTimes[node-1].append(time)
            if node in edgesMap:
                for entry in edgesMap[node]:
                    if entry in edgesUsed and time + entry[2] > min(reachedTimes[entry[1]-1]):
                        pass
                    else:
                        edgesUsed.add(entry)
                        traverse(entry[1], time + entry[2])
            
        traverse(K, 0)
        
        for i, entry in enumerate(reachedTimes):
            if len(entry) < 1:
                return -1
            else:
                reachedTimes[i] = min(entry)
                
        return max(reachedTimes)
        
            