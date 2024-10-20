
# Oct 2024
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            if len(h) == k:
                heappushpop(h, n)
            else:
                heappush(h, n)
        
        return h[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                heapq.heappushpop(h, n)
        return h[0]