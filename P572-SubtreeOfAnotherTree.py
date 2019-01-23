class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        self.isSubTree = False
        self.tHead = t
        
        def compareTwoTrees(a, b):
            self.isEqual = True
            
            def recurseCompare(node1, node2):
                if node1 and node2:
                    if (node1.val != node2.val):
                        self.isEqual = False
                    else:
                        recurseCompare(node1.left, node2.left)
                        recurseCompare(node1.right, node2.right)
                elif node1 == None and node2 == None:
                    pass
                else:
                    self.isEqual = False
                    
            recurseCompare(a, b)
            return self.isEqual
            
        def recurse(node):
            if node:
                if node.val == self.tHead.val:
                    if(compareTwoTrees(node, self.tHead)):
                        self.isSubTree = True
                recurse(node.left)
                recurse(node.right)
                
        recurse(s)

        return self.isSubTree
        
        