class Solution:
    def maxScore(self, nums: List[int]) -> int:

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
            
        def lcm(a, b):
            return abs(a*b) // gcd(a, b)

        n = len(nums)
        maxScore = 0
        for i in range(n+1):
            if i == n:
                modifiedNums = nums
            else:
                modifiedNums = nums[:i] + nums[i+1:]

            if not modifiedNums:
                score = 0
            else:
                gcdVal = modifiedNums[0]
                for entry in modifiedNums[1:]:
                    gcdVal = gcd(gcdVal, entry)

                lcmVal = modifiedNums[0]
                for entry in modifiedNums[1:]:
                    lcmVal = lcm(lcmVal, entry)

                score = gcdVal * lcmVal

            maxScore = max(maxScore, score)

        return maxScore