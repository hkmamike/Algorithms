class Solution:
    def productExceptSelf(self, nums):

        result = []
        n = len(nums)
        
        previousProduct = 1
        
        for i in range(0, n):
            result.append(previousProduct)
            previousProduct *= nums[i]
            
        previousProduct = 1
        
        for i in range(n-1, -1, -1):
            result[i] *= previousProduct
            previousProduct *= nums[i]
            
        return result