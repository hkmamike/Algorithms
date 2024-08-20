# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def dfs(node):
            if not node:
                return (None, None)

            minL, maxL = dfs(node.left)
            minR, maxR = dfs(node.right)
            if (maxL != None and maxL >= node.val) or (minR != None and minR <= node.val):
                self.result = False

            returnMin = minL if minL != None else node.val
            returnMax = maxR if maxR != None else node.val
            return (returnMin, returnMax)

        dfs(root)
        return self.result