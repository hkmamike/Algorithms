# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def readNodes(self, node):
        if node:
            if node.val in self.frequencyMap:
                self.frequencyMap[node.val] += 1
            else:
                self.frequencyMap[node.val] = 1

            self.readNodes(node.left)
            self.readNodes(node.right)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.frequencyMap = {}
        self.readNodes(root)
        result = []
        mapKeys = sorted(self.frequencyMap, key=lambda x: self.frequencyMap[x], reverse=True)
        # print(mapKeys)
        
        maxFrequency = self.frequencyMap[mapKeys[0]]
        
        # print(self.frequencyMap)
        for key in mapKeys:
            if self.frequencyMap[key] == maxFrequency:
                result.append(key)
            else:
                break
                
        return result