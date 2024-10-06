class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        maxValue = 0
        for x,y,z in permutations(nums, 3):
            value = int(format(x, 'b') + format(y, 'b') + format(z, 'b'), 2)
            maxValue = max(maxValue, value)
        return maxValue