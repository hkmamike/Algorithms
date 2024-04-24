# Attempt 2: cleaner
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = []
        for i in range(len(position)):
            posAndSpeed.append((position[i], speed[i]))
        posAndSpeed.sort()

        expectedArrivalTimes = [(target - entry[0])/entry[1] for entry in posAndSpeed]
        
        for i in range(len(position)-2, -1, -1):
            if expectedArrivalTimes[i] < expectedArrivalTimes[i+1]:
                expectedArrivalTimes[i] = expectedArrivalTimes[i+1]

        return len(set(expectedArrivalTimes))

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

