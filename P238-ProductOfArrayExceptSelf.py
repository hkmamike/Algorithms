# Sep 24, 2024
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProduct = []
        for i, n in enumerate(nums):
            if i == 0:
                prefixProduct.append(n)
            else:
                prefixProduct.append(prefixProduct[-1] * n)
        
        suffixProduct = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffixProduct[i] = nums[i]
            else:
                suffixProduct[i] = suffixProduct[i+1] * nums[i]
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffixProduct[1])
            elif i == len(nums)-1:
                result.append(prefixProduct[-2])
            else:
                result.append(suffixProduct[i+1] * prefixProduct[i-1])
        return result

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