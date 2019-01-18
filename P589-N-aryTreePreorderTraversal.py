"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def recurse(node):
            if node:
                self.result.append(node.val)
                if node.children:
                    for child in node.children:
                        recurse(child)
        
        self.result = []
        recurse(root)
        return self.result
        