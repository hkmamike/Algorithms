class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hashMap = {}
        maxEdges = -1
        result = 0
        width = sum(wall[0])
        height = len(wall)
        
        for row in wall:
            
            atPosition = 0
            for brick in row:
                atPosition += brick
                
                if atPosition in hashMap:
                    hashMap[atPosition] += 1
                else:
                    hashMap[atPosition] = 1
                    
        for entry in hashMap:
            if hashMap[entry] > maxEdges and entry != width:
                maxEdges = hashMap[entry]
                result = height - maxEdges

        if maxEdges == -1:
            return height
        else:
            return result