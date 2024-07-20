
# using heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums[:k]
        self.k = k
        heapify(self.nums)
        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                heappushpop(self.nums, nums[i])
        
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif val > self.nums[0]:
            heappushpop(self.nums, val)

        return self.nums[0]


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.store = sorted(nums, reverse=True)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k > len(self.store):
            self.store.append(val)
            self.store.sort(reverse=True)
        elif val > self.store[-1]:
            self.store.pop()
            self.store.append(val)
            self.store.sort(reverse=True)
            
        return self.store[self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)