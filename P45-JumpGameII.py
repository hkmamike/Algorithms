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