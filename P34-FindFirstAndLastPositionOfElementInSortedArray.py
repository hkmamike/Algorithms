class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def bSearchLeft():
            l = 0
            r = len(nums)-1
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m+1
            if nums[r] == target:
                return r
            else:
                return -1
            
        def bSearchRight():
            l = 0
            r = len(nums)-1
            while l < r:
                m = (l+r)//2+1
                if nums[m] <= target:
                    l = m
                else:
                    r = m-1
            if nums[l] == target:
                return l
            else:
                return -1
        
        return [bSearchLeft(), bSearchRight()]