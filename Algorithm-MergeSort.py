class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            M = len(nums) // 2
            L = nums[:M]
            R = nums[M:]

            L = self.mergeSort(L)
            R = self.mergeSort(R)

            l = r = k = 0

            while l < len(L) and r < len(R):
                if L[l] < R[r]:
                    nums[k] = L[l]
                    l += 1
                else:
                    nums[k] = R[r]
                    r += 1
                k+=1

            while l < len(L):
                nums[k] = L[l]
                l += 1
                k += 1
            while r < len(R):
                nums[k] = R[r]
                r += 1
                k += 1
                
        return nums
