# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def recurse(node):
            if not node:
                return 0
            L = recurse(node.left)
            R = recurse(node.right)
            LPlusNode = L + node.val
            RPlusNode = R + node.val
            FullNode = L + R + node.val
            self.maxSum = max(LPlusNode, RPlusNode, FullNode, node.val, self.maxSum)
            return max(LPlusNode, RPlusNode, node.val)
        
        recurse(root)
        return self.maxSum
