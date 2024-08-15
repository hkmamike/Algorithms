class MedianFinder:

    def __init__(self):
        self.bigHalf = []
        self.smallHalf = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHalf, -num)
        heapq.heappush(self.bigHalf, -self.smallHalf[0])
        heapq.heappop(self.smallHalf)

        if len(self.smallHalf) < len(self.bigHalf):
            heappush(self.smallHalf, -self.bigHalf[0])
            heappop(self.bigHalf)

    def findMedian(self) -> float:
        if len(self.smallHalf) > len(self.bigHalf):
            return -self.smallHalf[0]
        else:
            return (self.bigHalf[0] + -self.smallHalf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


from heapq import *

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num):
        minHeap = self.minHeap
        maxHeap = self.maxHeap
        heappush(minHeap, -heappushpop(maxHeap, num))
        
        if len(minHeap) > len(maxHeap):
            heappush(maxHeap, -heappop(minHeap))
        
    def findMedian(self):
        minHeap = self.minHeap
        maxHeap = self.maxHeap
        
        if len(maxHeap) > len(minHeap):
            return maxHeap[0]
        else:
            return (maxHeap[0] - minHeap[0]) / 2