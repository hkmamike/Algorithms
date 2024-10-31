# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colMap = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:            
            for i in range(len(queue)):
                node, lv, col = queue.popleft()
                colMap[col].append((lv, node.val))

                if node.left:
                    queue.append((node.left, lv+1, col-1))
                if node.right:
                    queue.append((node.right, lv+1, col+1))

        h = []
        for k, v in colMap.items():
            v.sort()
            heappush(h, (k, v))

        result = []
        while h:
            k, v = heappop(h)
            cleanedV = [x[1] for x in v]
            result.append(cleanedV)

        return result