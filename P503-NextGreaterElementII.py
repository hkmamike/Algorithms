class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        result = [-1] * len(nums)
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
                
            stack.append(i)
            
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
                
            if stack == []:
                break

        return result