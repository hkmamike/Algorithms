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
        