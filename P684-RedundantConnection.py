# union-find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(node):
            if rootMap[node] == -1:
                return node
            rootMap[node] = find(rootMap[node])
            return rootMap[node]

        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)
            if root1 == root2:
                return True
            else:
                rootMap[root1] = root2
                return False

        rootMap = defaultdict(lambda: -1)
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]