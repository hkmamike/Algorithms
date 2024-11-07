class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        N = len(graph)
        colors = [0] * N

        for i in range(N):
            if colors[i] != 0:
                continue
            
            q = deque([i])
            colors[i] = 1

            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[curr]
                        q.append(neighbor)
                    elif colors[neighbor] == colors[curr]:
                        return False
        return True