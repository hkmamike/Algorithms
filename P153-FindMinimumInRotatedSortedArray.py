class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        else:
            return self.findRecurse(nums, 0, len(nums)-1)
        
    def findRecurse(self, nums, start, end):
        mid = (start + end) // 2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
            return nums[mid]
        elif nums[mid] < nums[end]:
            return self.findRecurse(nums, start, mid-1)
        else:
            return self.findRecurse(nums, mid+1, end)
            
        