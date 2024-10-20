class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        def getGPD(num):
            def getSmallestD(n):
                if n % 2 == 0:
                    return 2
                i = 3
                while i * i <= n:
                    if n % i == 0:
                        return i
                    i += 2
                return n
            small = getSmallestD(num)
            return num // small

        result = 0
        for i in range(len(nums)-2, -1, -1):
            while nums[i] > nums[i+1]:
                GPD = getGPD(nums[i])
                if GPD == 1:
                    return -1
                else:
                    nums[i] = nums[i] // GPD
                    result += 1
        return result