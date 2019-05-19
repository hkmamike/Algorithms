class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        pathsMap = collections.defaultdict(set)
        for path in paths:
            g1 = path[0]-1
            g2 = path[1]-1
            pathsMap[g1].add(g2)
            pathsMap[g2].add(g1)
        
        # print(pathsMap)
        result = [None] * N
        result[0] = 1
        
        queue = collections.deque([(0, 1)])
        unfilled = set([ i for i in range(len(result))])
        unfilled.remove(0)
        
        def chooseColor(node):
            choice = set([1,2,3,4])
            for neighbor in pathsMap[node]:
                if result[neighbor] != None and result[neighbor] in choice:
                    choice.remove(result[neighbor])
            return choice.pop()
            
        while len(unfilled) > 0 or len(queue):
            # print(result)
            # print(unfilled, queue)
            if queue:
                garden = queue.popleft()

                for neighbor in pathsMap[garden[0]]:
                    if neighbor in unfilled:
                        color = chooseColor(neighbor)
                        
                        result[neighbor] = color
                        # print(result, garden[1], color)
                        queue.append((neighbor, color))
                        unfilled.remove(neighbor)
            else:
                garden = unfilled.pop()
                color = 1
                result[garden] = 1
                for neighbor in pathsMap[garden]:
                    if neighbor in unfilled:
                        if color < 4:
                            color += 1
                        else:
                            color = 1
                            
                        result[neighbor] = color
                        queue.append((neighbor, color))
                        unfilled.remove(neighbor)
                        
        return result
                    
                    
            
        
        
        