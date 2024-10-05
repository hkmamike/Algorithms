# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Oct 4, 2024
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def recurse(node, depth, levelMap):
            if not node:
                return
            if depth not in levelMap:
                levelMap[depth] = node.val
            recurse(node.right, depth+1, levelMap)
            recurse(node.left, depth+1, levelMap)

        levelMap = {}
        recurse(root, 0, levelMap)
        result = []
        for i in range(len(levelMap)):
            result.append(levelMap[i])

        return result

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