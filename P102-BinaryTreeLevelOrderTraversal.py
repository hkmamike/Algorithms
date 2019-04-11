# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        self.result = []
        
        def traverse(node, level):
            if node:
                if len(self.result) < level + 1:
                    self.result.append([node.val])
                else:
                    self.result[level].append(node.val)
                
                traverse(node.left, level+1)
                traverse(node.right, level+1)
            
        traverse(root, 0)
        return self.result
        