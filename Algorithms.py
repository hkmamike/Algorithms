## trie
def buildTrie(self, words):
    self.root = {}
    for word in words:
        node = self.root
        for c in word + "$":
            node = node.setdefault(c, {})


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
