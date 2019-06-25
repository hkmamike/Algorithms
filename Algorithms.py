








## trie
def buildTrie(self, words):
    self.root = {}
    for word in words:
        node = self.root
        for c in word + "$":
            node = node.setdefault(c, {})

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

## binarySearch
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

def mergeSort(self, nums: List[int]) -> List[int]:
    if len(nums) > 1:
        M = len(nums) // 2
        L = nums[:M]
        R = nums[M:]

        L = self.mergeSort(L)
        R = self.mergeSort(R)
        l = r = k = 0
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                nums[k] = L[l]
                l += 1
            else:
                nums[k] = R[r]
                r += 1
            k+=1

        while l < len(L):
            nums[k] = L[l]
            l += 1
            k += 1
        while r < len(R):
            nums[k] = R[r]
            r += 1
            k += 1
            
    return nums

## shuffle


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
def shuffle(nums):
    n = len(nums)
    for i in range(n):
        rand = random.randrange(i,n-1)
        nums[rand], nums[i] = nums[i], nums[rand]

    return nums

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

## power
def pow(self, x: float, n: int) -> float:
    if n == 0:
        return 1
    
    elif n < 0:
        return 1 / self.myPow(x, -n)
    
    elif n % 2 == 1:
        return x * self.myPow(x, n-1)

    return self.myPow(x*x, n/2)

## rotate matrix
def rotate(self, matrix):
        n = len(matrix)
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]

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

## union-find
def find(node):
	if rootMap[node] == -1:
        Return node
	rootMap[node] = find(rootMap[node])
	return rootMap[node]

def union(a, b):
	rootA = find(a)
	rootB = find(b)
    if rootA < rootB:
        rootMap[rootB] = rootA
    elif rootB < rootA:
        rootMap[rootA] = rootB

rootMap = collections.defaultdict(lambda: -1)
for a, b in pairs:
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

## linked list
def reverseList(head):
    pre = None
    while head:
        current = head
        head = current.next
        current.next = pre
        pre = current
    return pre


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
