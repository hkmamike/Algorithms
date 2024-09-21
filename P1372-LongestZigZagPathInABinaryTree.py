# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxZigZag = 0

        def dfs(node, lastDir, cnt):
            if not node:
                self.maxZigZag = max(self.maxZigZag, cnt-1)
            else:
                if lastDir == "L":
                    dfs(node.right, "R", cnt + 1)
                    dfs(node.left, "L", 1)
                elif lastDir == "R":
                    dfs(node.left, "L", cnt + 1)
                    dfs(node.right, "R", 1)
                else:
                    dfs(node.left, "L", 1)
                    dfs(node.right, "R", 1)

        dfs(root, "root", 0)
        return self.maxZigZag