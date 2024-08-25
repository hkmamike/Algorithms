# copied from https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/solutions/5686810/python3-eventually-nice/
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        if multiplier == 1: return nums
        MOD = 10 ** 9 + 7
        N = len(nums)

        h = [[n, i] for i,n in enumerate(nums)]
        heapify(h)
        count = [0] * N
        while k and h[0][0] <= 1e9:
            k -= 1
            key, i = heappop(h)
            count[i] += 1
            heappush(h, [key * multiplier, i])

        q, r = divmod(k, N)
        h.sort()
        for idx, (key, i) in enumerate(h):
            count[i] += q + (idx < r)
        
        for i, c in enumerate(count):
            nums[i] *= pow(multiplier, c, MOD)
            nums[i] %= MOD

        return nums

