# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recurseTree(self, node):
        if node:
            if node.val not in self.minTwo:
                self.minTwo.append(node.val)
            if len(self.minTwo) > 2:
                self.minTwo.sort()
                self.minTwo.pop()
            
            if node.left:
                self.recurseTree(node.left)
            if node.right:
                self.recurseTree(node.right)
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        
        self.minTwo = []
        self.recurseTree(root)
        
        if len(self.minTwo) < 2:
            return -1
        else:
            self.minTwo.sort()
            return self.minTwo[1]
        