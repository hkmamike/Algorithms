class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
            
        for i in range(numCourses):
            if not self.dfs(visited, graph, i):
                return False
                
        return True
            
    def dfs(self, visited, graph, i):
        if visited[i] == 1:
            return True
        elif visited[i] == -1:
            return False
        
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(visited, graph, j):
                return False
            
        visited[i] = 1
        
        return True