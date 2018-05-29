class Solution:
    
    def canVisitAllRooms(self, rooms):
        
        self.lockedRooms = [1] * len(rooms)
        self.lockedRooms[0] = 0
        
        def explore(rooms, index):
            self.lockedRooms[index] = 0
            nextRooms = rooms[index]
            
            for room in nextRooms:
                if self.lockedRooms[room] == 1:
                    explore(rooms, room)
                
        explore(rooms, 0)
        
        return sum(self.lockedRooms) == 0