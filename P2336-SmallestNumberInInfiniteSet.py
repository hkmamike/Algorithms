class SmallestInfiniteSet:

    def __init__(self):
        self.addBackList = []
        self.addBackSet = set()
        self.ceiling = 1

    def popSmallest(self) -> int:
        if len(self.addBackList) > 0:
            returnVal = heapq.heappop(self.addBackList)
            self.addBackSet.remove(returnVal)
            return returnVal
        else:
            self.ceiling += 1
            return self.ceiling - 1

    def addBack(self, num: int) -> None:
        if num >= self.ceiling:
            return
        elif num in self.addBackSet:
            return
        else:
            heapq.heappush(self.addBackList, num)
            self.addBackSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)