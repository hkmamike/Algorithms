class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs, key= lambda x: abs(x[0] - x[1]))
        
        N = len(costs) // 2
        Acost = 0
        Bcost = 0
        Acount = 0
        Bcount = 0
        
        for i in range(len(costs)-1, -1, -1):
            if Acount == N:
                Bcost += costs[i][1]
                continue
            elif Bcount == N:
                Acost += costs[i][0]
                continue
                
            if costs[i][0] <= costs[i][1]:
                Acost += costs[i][0]
                Acount += 1
            else:
                Bcost += costs[i][1]
                Bcount += 1
                
        return Acost + Bcost
        
        