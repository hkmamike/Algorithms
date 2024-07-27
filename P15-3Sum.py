class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        numMap = collections.defaultdict(list)
        for i, n in enumerate(nums):
            numMap[n].append(i)

        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                target = 0 - nums[i] - nums[j]
                if (target in numMap and any(idx > j for idx in numMap[target])):
                    result.append([nums[i], nums[j], target])
        return result
    