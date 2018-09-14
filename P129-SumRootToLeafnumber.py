# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    sumTotal = 0
    
    def recurseSum(self, node, valSoFar):
        if not node.left and not node.right:
            self.sumTotal += int(valSoFar+str(node.val))
        if node.left:
            self.recurseSum(node.left, valSoFar+str(node.val))
        if node.right:
            self.recurseSum(node.right, valSoFar+str(node.val))
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.recurseSum(root, '')
        return self.sumTotal
        