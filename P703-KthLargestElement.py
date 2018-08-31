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