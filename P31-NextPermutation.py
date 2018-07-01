class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        if length <= 2:
            nums.reverse()
            
        else:
            n1 = None
            n2 = length-1
            
            for i in range(length-1, 0, -1):
                if nums[i] > nums[i-1]:
                    n1 = i-1
                    break

            if n1 == None:
                nums.reverse()
                
            else:
                for i in range(length-1, -1, -1):
                    if nums[i] > nums[n1]:
                        n2 = i
                        break
                    
                nums[n1], nums[n2] = nums[n2], nums[n1]
                l = n1+1
                r = len(nums) - 1

                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1