"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def exploreTree(self, node, target):
        if node:
            if abs(target-node.val) < abs(target-self.closest):
                self.closest = node.val
            
            if node.val == target:
                return
            elif target > node.val:
                self.exploreTree(node.right, target)
            else:
                self.exploreTree(node.left, target)
            
    
    def closestValue(self, root, target):
        # write your code here
        self.closest = root.val
        
        self.exploreTree(root, target)
        
        return self.closest
        