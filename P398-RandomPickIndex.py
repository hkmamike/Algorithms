
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.memory = defaultdict(list)
        for i, n in enumerate(nums):
            self.memory[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.memory[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution:
    def __init__(self, nums: List[int]):
        self.valMap = {}
        
        for i, num in enumerate(nums):
            if num in self.valMap:
                self.valMap[num].append(i)
            else:
                self.valMap[num] = [i]

    def pick(self, target: int) -> int:
        
        indices = self.valMap[target]
        length = len(indices)
        randIndex = random.randrange(length)
        return indices[randIndex]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)