class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        quota = nums[0]
        jumps = 0

        while pos < len(nums) - 1 and quota > 0:
            if pos + quota >= len(nums) - 1:
                return jumps + 1
            champion = nums[pos + quota]
            nextPos = pos + quota
            for i in range(pos+1, pos+quota+1):
                challenger = i + nums[i]
                if challenger >= champion:
                    champion = challenger
                    nextPos = i
            pos = nextPos
            jumps += 1
            quota = nums[nextPos]
        return jumps

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        pos = 0
        jump = nums[0]
        goal = length - 1
        count = 0
        
        if pos == goal:
            return 0
        
        while True:
            if pos + jump >= goal:
                return count+1
            
            bestC = 1
            bestV = 1 + nums[pos+1]
            
            for i in range(1, jump+1):
                value = i + nums[pos+i]
                if value > bestV:
                    bestC = i
                    bestV = value
                    
            pos += bestC
            count += 1
            jump = nums[pos]