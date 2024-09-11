class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        deque = collections.deque(preorder)
        
        def recurse(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                node = TreeNode(inorder[idx])
                node.left = recurse(preorder, inorder[:idx])
                node.right = recurse(preorder, inorder[idx+1:])
                return node   
            
            
        return recurse(deque, inorder)
