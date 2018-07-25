# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        
        self.nodesMap = {}
        self.nodesMap[node] = UndirectedGraphNode(node.label)
        stack = [node]
        
        while stack:
            item = stack.pop()
            for neighbor in item.neighbors:
                if neighbor not in self.nodesMap:
                    self.nodesMap[neighbor] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                self.nodesMap[item].neighbors.append(self.nodesMap[neighbor])
        
        return self.nodesMap[node]