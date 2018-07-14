"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def recurse(self, node, countSoFar, parentVal):
        if node:
            if node.val == parentVal+1:
                self.count = max(self.count, countSoFar+1)
            else:
                countSoFar = 0
                
            self.recurse(node.left, countSoFar+1, node.val)
            self.recurse(node.right, countSoFar+1, node.val)
            
    
    def longestConsecutive(self, root):
        # write your code here
        
        if not root:
            return 0
            
        self.count = 1
        self.recurse(root, 0, float('inf'))
        
        return self.count
        
