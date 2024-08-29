# new way to do it
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        depMap = defaultdict(set)
        for c, prereq in prerequisites:
            depMap[c].add(prereq)
        
        foundationalCourses = set(range(numCourses)) - set(depMap.keys())
        ranks = [0] * numCourses
        for c in foundationalCourses:
            ranks[c] = 1
        
        def rankCourse(course, ranks, depMap):
            if ranks[course] == 4000001:
                return 4000001
            elif ranks[course] != 0:
                return ranks[course]
            
            ranks[course] = 4000001
            courseRank = max([rankCourse(c, ranks, depMap) for c in depMap[course]]) + 1
            ranks[course] = courseRank
            return courseRank
            
        for c in range(numCourses):
            if ranks[c] == 0:
                rankCourse(c, ranks, depMap)

        if max(ranks) >= 4000001:
            return []
        else:
            result = [n for n in range(numCourses)]
            result.sort(key = lambda x: ranks[x])
            return result

# topological sort
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        prereqMap = collections.defaultdict(list)
        for pair in prerequisites:
            prereqMap[pair[0]].append(pair[1])
        
        def dfs(node, visited, order, pathSet):
            pathSet.add(node)
            
            for neighbor in prereqMap[node]:
                if neighbor in pathSet:
                    self.loopFound = True
                elif neighbor not in visited:
                    dfs(neighbor, visited, order, pathSet)
                    
            order.append(node)
            pathSet.remove(node)
            visited.add(node)
            
        visited = set()
        order = []
        for i in range(numCourses):
            if i not in visited:
                self.loopFound = False
                dfs(i, visited, order, set())
                if self.loopFound:
                    return []

        return order