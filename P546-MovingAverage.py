class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.data = collections.deque([])
        self.size = size
        self.length = 0
        self.sumVal = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.data.append(val)
        self.length += 1
        self.sumVal += val
        
        if self.length > self.size:
            decrement = self.data.popleft()
            self.sumVal -= decrement
            self.length -= 1
        
        return self.sumVal / self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)