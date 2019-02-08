class Solution:
    def canReorderDoubled(self, A: 'List[int]') -> 'bool':
        
        A.sort()
        pairMap = {}
        
        for a in A:
            if a in pairMap:
                pairMap[a] += 1
            else:
                pairMap[a] = 1
                
        for key in A:
            if 2 * key in pairMap:
                while pairMap[key] > 0 and pairMap[2 * key] > 0:
                    pairMap[key] -= 1
                    pairMap[2 * key] -= 1
        
        pairMap = {x:y for x,y in pairMap.items() if y!=0}

        return len(pairMap) == 0
                