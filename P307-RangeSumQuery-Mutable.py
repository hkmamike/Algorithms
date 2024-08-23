# Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray(object):
    def __init__(self, nums: List[int]):
        # recursive helper create tree from input list
        def createTree(nums, l, r):
            # base case
            if l > r:
                return None
            # leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            root = Node(l, r)

            # build the tree recursively
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)

            # populate root value
            root.total = root.left.total + root.right.total
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        # recursive helper to update tree
        def updateVal(root, i, val):
            # Base case for leaf node
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2
            # if idx is less than mid, leaf is on left subtree
            if i <= mid:
                updateVal(root.left, i, val)
            # otherwise, the right subtree
            else:
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total
            return root.total

        return updateVal(self.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:

        # helper to recursively calculate range sum
        def rangeSum(root, i, j):
            #If the range matches the root, return total from the root
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i > mid:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, left, right)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)