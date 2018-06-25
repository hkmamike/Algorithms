# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def recurse(self, node, candidate, target):
        if node:
            L = node.left
            R = node.right
            newCandidate = candidate[:]
            newCandidate.append(node.val)

            if not L and not R:
                if sum(newCandidate) == target:
                    self.results.append(newCandidate)
            else:
                if L:
                    self.recurse(L, newCandidate, target)
                if R:
                    self.recurse(R, newCandidate, target)
                        
    def pathSum(self, root, target):
        
        self.results = []
        self.recurse(root,[],target)
        return self.results