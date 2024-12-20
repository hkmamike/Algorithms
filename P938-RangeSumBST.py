# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                if low <= node.val <= high:
                    self.result += node.val
        dfs(root)
        return self.result

class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        
        self.sumVal = 0
        
        def dfs(node, L, R):
            if node:
                if node.val <= R and node.val >= L:
                    self.sumVal += node.val
                dfs(node.left, L, R)
                dfs(node.right, L, R)

        dfs(root, L, R)
        
        return self.sumVal