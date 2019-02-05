class StockSpanner(object):

    def __init__(self):
        self.clock = 0
        self.stack = [[float('inf'), 0]]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.clock += 1
        
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            self.stack.pop()
        
        if len(self.stack) > 0:
            span = self.clock - self.stack[-1][1]
        else:
            span = 1
        self.stack.append([price, self.clock])
        
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)