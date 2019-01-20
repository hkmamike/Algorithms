"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        
        lastLevel = collections.deque([root])
        nextLevel = collections.deque([])
        addToResult = []
        
        while len(lastLevel) > 0:
            entry = lastLevel.popleft()
            
            addToResult.append(entry.val)
            
            for child in entry.children:
                nextLevel.append(child)
        
            if len(lastLevel) == 0:
                result.append(addToResult)
                lastLevel = nextLevel
                nextLevel = collections.deque([])
                addToResult = []
                
        return result
        
        