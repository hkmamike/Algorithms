# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, nodes):
            if not node:
                nodes.append("#")
            else:
                nodes.append(str(node.val))
                preorder(node.left, nodes)
                preorder(node.right, nodes)
        
        nodes = []
        preorder(root, nodes)
        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build(nodes):
            n = nodes.popleft()
            if n == "#":
                return None
            node = TreeNode(int(n))
            node.left = build(nodes)
            node.right = build(nodes)
            return node

        nodes = deque(data.split(","))
        return build(nodes)

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        
        def recurse(node):
            if node:
                serialized.append(str(node.val))
                recurse(node.left)
                recurse(node.right)
            else:
                serialized.append('#')
        
        recurse(root)
        return '-'.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
            
        vals = iter(data.split('-'))
        return doit()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))