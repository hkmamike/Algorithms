class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position:
            return 0
        else:
            length = len(position)
            fleet = 1
        
        times = []
        for i in range(length):
            time = (target-position[i]) / speed[i]
            times.append(time)
            
        tuples = []
        for i in range(length):
            tuples.append((position[i], times[i]))
            
        tuples = sorted(tuples, key=lambda x: x[0], reverse=True)
        
        sortedTimes = []
        for i in range(length):
            sortedTimes.append(tuples[i][1])
            
        for i in range(1, length):
            sortedTimes[i] = max(sortedTimes[i], sortedTimes[i-1])
            if sortedTimes[i] > sortedTimes[i-1]:
                fleet += 1
                
        return fleet