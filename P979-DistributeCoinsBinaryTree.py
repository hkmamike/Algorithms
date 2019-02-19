# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    passing = 0
    def distributeCoins(self, root: 'TreeNode') -> 'int':
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.passing += abs(left) + abs(right)
            return node.val + left + right - 1
        
        dfs(root)
        return self.passing
    