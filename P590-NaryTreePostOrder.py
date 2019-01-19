"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def recurse(node):
            if node:
                if len(node.children) > 0:
                    for child in node.children:
                        recurse(child)
                    self.result.append(node.val)
                else:
                    self.result.append(node.val)
            
            
        self.result = []
        recurse(root)
        
        return self.result