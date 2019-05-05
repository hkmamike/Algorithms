# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.smaller = 0
        
        def explore(node, total):
            if node:
                leftSubTreeSum = explore(node.left, total)
                
                # print(node.val, total, self.smaller)
                originalVal = node.val
                node.val = total - self.smaller
                self.smaller += originalVal
                
                rightSubTreeSum = explore(node.right, total)
                
        
        def count(node):
            if node:
                leftSum = count(node.left)
                rightSum = count(node.right)
                return leftSum + rightSum + node.val
            else:
                return 0
        
        total = count(root)
        explore(root, total)
        return root
        