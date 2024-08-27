# New way to do it
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def doable(node, classesPossible, depMap):
            if classesPossible[node] == 1:
                return True
            if classesPossible[node] == -1:
                return False

            classesPossible[node] = -1
            isNodeDoable = all([ doable(prereq, classesPossible, depMap) for prereq in depMap[node] ])
            if isNodeDoable:
                classesPossible[node] = 1
            return isNodeDoable
            
        depMap = defaultdict(set)
        for c, prereq in prerequisites:
            depMap[c].add(prereq)

        foundationalSet = set(range(numCourses)) - set(depMap.keys())
        classesPossible = [0] * numCourses
        for key in foundationalSet:
            classesPossible[key] = 1
        
        return all([doable(c, classesPossible, depMap) for c in range(numCourses)])

# TopologicalSort
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