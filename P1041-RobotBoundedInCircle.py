class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction, pos = complex(0, 1), [0, 0]
        
        for i in range(0, 4):
            for t in range(len(instructions)):
                if instructions[t] == 'G':
                    pos = [pos[0] + int(direction.real), pos[1] + int(direction.imag)]

                elif instructions[t] == 'L':
                    direction = direction * complex(0, 1)
                    
                else:
                    direction = direction * complex(0, -1)
                
        if [pos[0], pos[1]] == [0,0]:
            return True
        else:
            return False

        
        