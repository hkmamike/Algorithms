class Solution:
    def find132pattern(self, nums: 'List[int]') -> 'bool':
        val2 = float('-inf')
        stack = []
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < val2:
                return True
            
            while stack and stack[-1] < nums[i]:
                val2 = stack.pop()
                
            stack.append(nums[i])
            
        return False