class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        maxFrequency = max(cnt.values())

        firstSeen = {}
        lastSeen = {}

        for i, n in enumerate(nums):
            if n not in firstSeen:
                firstSeen[n] = i
            lastSeen[n] = i
        
        result = float('inf')
        for k, v in cnt.items():
            if v == maxFrequency:
                candidate = lastSeen[k] - firstSeen[k] + 1
                result = min(candidate, result)
        
        return result
        
