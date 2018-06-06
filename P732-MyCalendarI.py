class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        
        self.events.append((start+0.1, 1))
        self.events.append((end, -1))
        self.events.sort(key=lambda x: x[0])
        
        k = 0
        maxK = 0
        
        for event in self.events:
            k += event[1]
            maxK = max(maxK, k)
            
        return maxK