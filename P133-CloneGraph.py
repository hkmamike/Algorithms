"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Oct 31, 2024 - had to reference template
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        M = {}
        M[node] = Node(node.val, [])
        stack = [node]

        while stack:
            nextNode = stack.pop()
            for neighbor in nextNode.neighbors:
                if neighbor not in M:
                    M[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                M[nextNode].neighbors.append(M[neighbor])

        return M[node]


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodesMap = {}
        nodesMap[node] = Node(node.val, [])
        nodesStack = [node]

        while nodesStack:
            nextNode = nodesStack.pop()
            
            for entry in nextNode.neighbors:
                if entry not in nodesMap:
                    nodesMap[entry] = Node(entry.val, [])
                    nodesStack.append(entry)
                nodesMap[nextNode].neighbors.append(nodesMap[entry])

        return nodesMap[node]



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