class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # keep biggest positive and smallest negative
        memory = [(nums[0], nums[0])]
        maxP = nums[0]
        for i, n in enumerate(nums):
            if i == 0:
                continue
            candidate1 = n * memory[i-1][0]
            candidate2 = n * memory[i-1][1]
            maxCandidate = max(candidate1, candidate2, n)
            minCandidate = min(candidate1, candidate2, n)
            maxP = max(maxP, maxCandidate)
            memory.append((minCandidate, maxCandidate))

        return maxP
