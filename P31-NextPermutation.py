# Oct 23, 2024, needed hint
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        # find pivot (first drop in value from back)
        def findPivot(nums):
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    return i
            return -1
        
        # find swap value (first value from back bigger than pivot)
        def findSwap(nums, pivotIdx):
            for i in range(len(nums)-1, pivotIdx, -1):
                if nums[i] > nums[pivotIdx]:
                    return i
    
        pivotIdx = findPivot(nums)
        if pivotIdx == -1:
            nums.reverse()
            return

        swapIdx = findSwap(nums, pivotIdx)

        # swap
        nums[swapIdx], nums[pivotIdx] = nums[pivotIdx], nums[swapIdx]

        # swap everything on the right of pivot index
        L, R = pivotIdx+1, len(nums)-1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1


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