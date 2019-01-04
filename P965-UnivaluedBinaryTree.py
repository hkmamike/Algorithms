# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        value = root.val
        
        def recurse(node):
            if node:
                if node.val != value:
                    return False
                else:
                    return recurse(node.left) and recurse(node.right)
            else:
                return True
            
        return recurse(root)
        