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