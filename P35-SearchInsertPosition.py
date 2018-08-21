class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums) - 1
        
        while L < R:
            M = (L+R) // 2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M
                
        if nums[L] < target:
            return L+1
        else:
            return L
            
        