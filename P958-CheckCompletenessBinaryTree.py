# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        def bfs(queue, nextQueue, valuesMap):
            while len(queue) > 0:
                node, pos, counter = queue.popleft()
                valuesMap[counter] = pos
                
                if node.left:
                    self.counter += 1
                    nextQueue.append((node.left, pos + str("0"), self.counter))
                    
                if node.right:
                    self.counter += 1
                    nextQueue.append((node.right, pos + str("1"), self.counter))

                if len(queue) == 0 and len(nextQueue) > 0:
                    queue = nextQueue
                    nextQueue = collections.deque()
        
        queue = collections.deque([(root, "1", 1)])
        self.counter = 1
        nextQueue = collections.deque()
        valuesMap = {}
        
        bfs(queue, nextQueue, valuesMap)
        
        maxVal = max(valuesMap.keys())
        return valuesMap[maxVal] == bin(maxVal)[2:]
        