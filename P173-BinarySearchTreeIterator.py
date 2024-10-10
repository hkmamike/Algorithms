# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):        
        self.nodes = [-1]
        self.curr = 0
        def preDfs(node):
            if node:
                preDfs(node.left)
                self.nodes.append(node.val)
                preDfs(node.right)
        preDfs(root)

    def next(self) -> int:
        self.curr += 1
        return self.nodes[self.curr]

    def hasNext(self) -> bool:
        return self.curr < (len(self.nodes) - 1)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()