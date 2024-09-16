class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        consecutiveN = []
        cnt = 0
        for n in nums:
            if n == 0:
                consecutiveN.append(cnt)
                cnt = 0
            else:
                cnt += 1
        if cnt != 0:
            consecutiveN.append(cnt)

        if len(consecutiveN) == 1 and consecutiveN[0] == 0:
            return 0
        elif len(consecutiveN) == 1:
            return consecutiveN[0] - 1

        maxPair = 0
        for i in range(1, len(consecutiveN)):
            candidate = consecutiveN[i] + consecutiveN[i-1]
            maxPair = max(maxPair, candidate)
        
        return maxPair
