#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        
        def recurseHelper(node):
            if node:
                leftValid = recurseHelper(node.left)
                rightValid = recurseHelper(node.right)
                
                if not leftValid:
                    node.left = None
                if not rightValid:
                    node.right = None
                    
                if not leftValid and not rightValid and node.val == 0:
                    return False
                else:
                    return True
            else:
                return False
                
        rootValid = recurseHelper(root)
        
        return root
        