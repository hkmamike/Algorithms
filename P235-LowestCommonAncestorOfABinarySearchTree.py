# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.LCA = None
        self.found = False

        def dfs(node):
            if not node:
                return 0

            LValue = dfs(node.left) 
            RValue = dfs(node.right)
            nodeValue = 1 if (node == p or nQode == q) else 0
            sumValue = LValue + RValue + nodeValue
            if not self.found and sumValue == 2:
                self.LCA = node
                self.found = True
            return sumValue

        dfs(root)
        return self.LCA