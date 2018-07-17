# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def readNodes(self, node, nodeVals):
        if node:
            nodeVals.append(node.val)
            self.readNodes(node.left, nodeVals)
            self.readNodes(node.right, nodeVals)
            
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeVals = []
        self.readNodes(root, nodeVals)
    
        minDiff = float('inf')
            
        nodeVals.sort()
        for i in range(1, len(nodeVals)):
            diff = abs(nodeVals[i] - nodeVals[i-1])
            minDiff = min(minDiff, diff)
            
        return minDiff
            