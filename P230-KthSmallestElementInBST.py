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