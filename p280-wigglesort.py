class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        
        if len(nums) >= 3:
            for i in range(1, len(nums)-2):
                sortedTemp = sorted([nums[i-1], nums[i], nums[i+1]])
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i], nums[i+1] = sortedTemp[2], sortedTemp[0], sortedTemp[1]
                else:
                    nums[i-1], nums[i], nums[i+1] = sortedTemp[0], sortedTemp[2], sortedTemp[1]
        else:
            pass