
dijkstra
priority queue
introduction to algorithms
shortest path problems

## trie
def buildTrie(self, words):
    self.root = {}
    for word in words:
        node = self.root
        for c in word + "$":
            node = node.setdefault(c, {})

## binarySearch with Exact Match
def binarySearch(array, target):
    L = 0
    R = len(array) - 1
    while L < R:
        M = (L+R) // 2
        if array[M] == target:
            return M
        elif array[M] < target:
            L = M + 1
        else:
            R = M
    return L

## binarySearch General
## reference: https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/
def binarySearch(array, target):
    def feasible(value) -> bool:
        # encode condition that matches desired result
        pass

    # include all elements
    L, R = 0, len(array)

    while L < R:
        M = (L+R) // 2
        if feasible(M)
            R = M
        else:
            L = M + 1
    return L

## shuffle
def shuffle(nums):
    n = len(nums)
    for i in range(n):
        rand = random.randrange(i,n-1)
        nums[rand], nums[i] = nums[i], nums[rand]

    return nums

## rotate matrix
def rotate(self, matrix):
        n = len(matrix)
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]


## grid move
def move(r, c):
    for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= r+i < len(grid) and 0 <= c+1 < len(grid[0]):
            yield (r+i, c+j)

## union-find
def find(node):
    if rootMap[node] == -1:
        return node
    rootMap[node] = find(rootMap[node])
    return rootMap[node]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA <= rootB:
        rootMap[rootB] = rootA
    elif rootB < rootA:
        rootMap[rootA] = rootB

rootMap = collections.defaultdict(lambda: -1)
for a, b in edges:
	union(a, b)

## topological sort with cycle detection
def topologicalSort(self, numCourses, prerequisites):

    prereqMap = collections.defaultdict(list)
    for pair in prerequisites:
        prereqMap[pair[0]].append(pair[1])
    
    def dfs(node, visited, order, pathSet):
        pathSet.add(node)
        
        for neighbor in prereqMap[node]:
            if neighbor in pathSet:
                self.loopFound = True
            elif neighbor not in visited:
                dfs(neighbor, visited, order, pathSet)
                
        order.append(node)
        pathSet.remove(node)
        visited.add(node)
        
    visited = set()
    order = []
    for i in range(numCourses):
        if i not in visited:
            self.loopFound = False
            dfs(i, visited, order, set())
            if self.loopFound:
                return []

    return order

## clone graph
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None
    
    nodesMap = {}
    nodesMap[node] = Node(node.val, [])
    stack = [node]
    
    while stack:
        item = stack.pop()
        for neighbor in item.neighbors:
            if neighbor not in nodesMap:
                nodesMap[neighbor] = Node(neighbor.val, [])
                stack.append(neighbor)
                
            nodesMap[item].neighbors.append(nodesMap[neighbor])
        
    return nodesMap[node]

## coin change:
def coinChange(self, coins, amount):
    if amount == 0:
        return 0
    
    dp = [amount+1] * (amount+1)
    for i in range(1, amount+1):
        for coin in coins:
            if i == coin:
                dp[i] = 1  
            elif i - coin > 0 and dp[i-coin] != amount + 1:
                dp[i] = min(dp[i], dp[i-coin] + 1)
                
    return dp[amount] if dp[amount] != amount + 1 else -1

## linked list
def reverseList(head):
    pre = None
    while head:
        current = head
        head = current.next
        current.next = pre
        pre = current
    return pre

## count primes
def countPrimes(self, n):
    if n < 3:
        return 0
    
    prime = [True] * n
    prime[0] = prime[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n, i):
                prime[j] = False
                
    return sum(prime)

## edit distance without replacement
def editDistance(w1, w2, allowance):
    if len(w1) > len(w2):
        w1, w2 = w2, w1
    if len(w2) != len(w1) + allowance:
        return False
    
    p1 = p2 = 0
    while p1 < len(w1):
        if w1[p1] == w2[p2]:
            p1 += 1
            p2 += 1
        elif allowance == 0:
            return False
        else:
            p2 += 1
            allowance -= 1
    return True

## addBinary
def addBinary(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = carry >> 1
        return res[::-1]

## sorting
def radixSort(self, num):
    for i in range(32):
        big = []
        small = []
        needle = 1 << i
        for val in num:
            if val & needle != 0:
                big.append(val)
            else:
                small.append(val)

        num = []
        num += small
        num += big

    return num

def mergeSort(enum):
    h = len(enum) // 2
    if h:
        L, R = mergeSort(enum[:h]), mergeSort(enum[h:])
        for i in range(len(enum)-1, -1, -1):
            if not R or L and L[-1] > R[-1]:
                enum[i] = L.pop()
            else:
                enum[i] = R.pop()
    return enum

## reorderList
class Solution:
    def reorderList(self, head: ListNode) -> None:

        def split(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            middle = slow.next
            slow.next = None
            
            return head, middle
            
        def reverse(head):
            last = None
            currentNode = head
            
            while currentNode:
                nextNode = currentNode.next
                currentNode.next = last
                last = currentNode
                currentNode = nextNode

            return last
        
        def mergeLists(a, b):
            head = tail = a
            
            a = a.next
            while b:
                tail.next = b
                tail = tail.next
                b = b.next
                if a:
                    a, b = b, a
                    
            return head
        
        if not head or not head.next:
            return
        
        a, b = split(head)
        b = reverse(b)
        head = mergeLists(a, b)

## divide
def divide(self, y, x):
    positive = (y > 0) == (x > 0)
    x = abs(x)
    y = abs(y)
    result = 0

    while y >= x:
        temp, i = x, 1
        while y >= temp:
            i <<= 1
            temp <<= 1
            
        i >>= 1
        temp >>= 1
        y -= temp
        result += i

    if not positive:
        result = - result
        
    return min(max(result, -2147483648), 2147483647)


### Segment Tree Implementation, P152,  ###

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
### Segment Tree Implementation Ends ###

## power
def pow(self, x: float, n: int) -> float:
    if n == 0:
        return 1
    
    elif n < 0:
        return 1 / self.myPow(x, -n)
    
    elif n % 2 == 1:
        return x * self.myPow(x, n-1)

    return self.myPow(x*x, n/2)

## next permutation, next lexicographical permutation
def nextPermutation(self, nums: List[int]) -> None:
    if len(nums) <= 1:
        return
    
    def findPivot():
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                return i
        return -1
    
    def findSwap(pivotIdx):
        for i in range(len(nums)-1, pivotIdx, -1):
            if nums[i] > nums[pivotIdx]:
                return i
    
    # step 1, from the end, find the first drop, this is the pivot
    pivotIdx = findPivot()
    if pivotIdx == -1:
        nums.reverse()
        return
    
    # step 2, again from the end, find the first thing that is bigger than pivot
    swapIdx = findSwap(pivotIdx)
    
    # step 3, swap pivot and the idx found in step 2
    nums[swapIdx], nums[pivotIdx] = nums[pivotIdx], nums[swapIdx]
    
    # step 4, from the pivot idx, swap everything on the right
    l = pivotIdx + 1
    r = len(nums)-1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

## testing
import time
class Environment:

    def __init__(self):
        self.someGlobalVar = 1

    def solution(self, nums):
        sumV = 0
        for num in nums:
            sumV += num
            return sumV

    def test(self, cases, functionToTest):
        for i, case in enumerate(cases):
            caseInput, expected = case
            failed = functionToTest(caseInput) != expected
            if failed:
                print('Failed: test case {} of {} with:\nInput: {}\nReturned: {}\nExpected: {}'.format(i+1, len(cases), caseInput, functionToTest(caseInput), expected))
                return 

        print('Succeeded: All {} test cases passed'.format(len(cases)))
        return

cases = [
    ([-2, -7], -9),
    ([2, -2], 0) ]

env = Environment()

start = time.process_time()
env.test(cases, env.solution)
end = time.process_time()

print('Running all {} test cases took {}ms.'.format(len(cases), round((end - start)*1000, 4)))
