class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        pos = 0
        jumps = nums[0]

        while pos != len(nums)-1 and jumps > 0:
            # print(pos, jumps)
            if pos + jumps >= len(nums)-1:
                return True

            candidates = [(i + nums[i], i) for i in range(pos+1, pos+jumps+1)]
            pos = max(candidates, key=lambda x: x[0])[1]
            # print(candidates, pos)
            if pos <= len(nums)-1:
                jumps = nums[pos]
            else:
                jumps = 0

        return pos >= len(nums)-1