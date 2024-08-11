class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        N = len(gas)
        surplus = [gas[i] - cost[i] for i in range(N)]
        if sum(surplus) < 0:
            return -1
        
        startIdx, tank = 0, 0
        for i in range(N):
            tank += surplus[i]

            if tank < 0:
                tank = 0
                startIdx = i+1
        
        return startIdx

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        surplus = [gi - ci for gi, ci in zip(gas, cost)]
        
        def findStart(surplus):
            surplus = surplus + surplus
            sumV, maxV, start = 0, 0, len(surplus)-1
            
            for i in range(len(surplus)-1,-1,-1):
                sumV += surplus[i]
                if sumV >= maxV:
                    maxV = sumV
                    start = i
                    
            return start
        
        if sum(surplus) < 0:
            return -1
        else:
            return findStart(surplus)
        