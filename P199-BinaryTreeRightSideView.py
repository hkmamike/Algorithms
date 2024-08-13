# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levelTakenSet = set()
        self.result = []

        def dfs(node, level):
            if node:
                if level not in self.levelTakenSet:
                    self.result.append(node.val)
                    self.levelTakenSet.add(level)
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)

        dfs(root, 0)
        return self.result