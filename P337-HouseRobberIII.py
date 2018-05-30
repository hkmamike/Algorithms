
class Solution:
    def rob(self, root):
        def explore(node):
            if node:
                left = explore(node.left)
                right = explore(node.right)
                grandChildrenVal = left[1] + right[1]
                childrenVal = left[0] + right[0]
                
                nodeVal = max(node.val + grandChildrenVal, childrenVal)
                return (nodeVal, childrenVal)
                
            else:
                return (0, 0)
        
        return explore(root)[0]
        