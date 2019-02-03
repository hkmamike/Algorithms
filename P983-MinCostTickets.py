class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        cost = 0
        last7 = collections.deque()
        last30 = collections.deque()
        
        for day in days:
            while last7 and last7[0][0] + 6 < day:
                last7.popleft()
            while last30 and last30[0][0] + 29 < day:
                last30.popleft()
                
            last7.append((day, cost + costs[1]))
            last30.append((day, cost + costs[2]))
            cost = min(cost + costs[0], last7[0][1], last30[0][1])
            
        return cost