class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        hashMap = {}
        def explore(node):
            if node:
                if node.val in hashMap:
                    hashMap[node.val].append(node)
                else:
                    hashMap[node.val] = [node]
                    
                explore(node.left)
                explore(node.right)
            
        explore(root)
        
        result = []
        def searchTree(node):
            if node:
                complement = k - node.val
                
                if complement in hashMap:
                    for entry in hashMap[complement]:
                        if entry != node:
                            result.append([entry, node])
                        
                searchTree(node.left)
                searchTree(node.right)
                
        searchTree(root)
        
        return len(result) > 0
        