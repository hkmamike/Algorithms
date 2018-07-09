class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        distance = [0 for _ in range(len(seats))]

        count = float('inf')
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                count = 1
                distance[i] = 0
            else:
                distance[i] = count
                count += 1
                
        count = float('inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                count = 1
            else:
                distance[i] = min(distance[i], count)
                count += 1
                
        return max(distance)