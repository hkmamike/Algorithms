# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.nodes = []
        def dfs(node):
            if node:
                dfs(node.left)
                self.nodes.append(node.val)
                if len(self.nodes) == k:
                    raise Exception("Solution Found, Terminating")
                dfs(node.right)

        try:
            dfs(root)
        except:
            return self.nodes[-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        smallest = []
        
        def dfs(node, smallest):
            if node:
                dfs(node.left, smallest)
                heapq.heappush(smallest, node.val)
                dfs(node.right, smallest)
            
        dfs(root, smallest)
        
        for _ in range(k-1):
            heapq.heappop(smallest)
            
        return heapq.heappop(smallest)