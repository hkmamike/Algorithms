# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        
        self.parents = []
        def dfs(node, x, y, depth):
            if node:
                if node.left and (node.left.val == x or node.left.val == y):
                    self.parents.append((depth, node))
                if node.right and (node.right.val == x or node.right.val == y):
                    self.parents.append((depth, node))
                        
                dfs(node.left, x, y, depth+1)
                dfs(node.right, x, y, depth+1)
        
        dfs(root, x, y, 0)
        if len(self.parents) == 2:
            return self.parents[0][0] == self.parents[1][0] and self.parents[0][1] != self.parents[1][1]
        else:
            return False