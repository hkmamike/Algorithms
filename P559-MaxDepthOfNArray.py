"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        depth = 0
        stack = [root]
        
        while stack:
            nextLevel = []
            while stack:
                node = stack.pop()
                if len(node.children) > 0:
                    nextLevel.extend(node.children)
            
            stack = nextLevel
            depth += 1
            
        return depth
        