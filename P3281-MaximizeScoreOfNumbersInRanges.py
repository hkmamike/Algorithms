class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        start.sort()

        def check(score):
            pre = -10**10
            for l in start:
                r = l + d
                cur = max(pre + score, l)
                if cur > r:
                    return False
                pre = cur
            
            return True
        
        l = 0
        r = 10**10
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans