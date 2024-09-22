class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        # optimization for edge case only
        if mountainHeight == 1:
            return min(workerTimes)

        def maxHeightReduced(workerTime, T):
            L, R = 0, mountainHeight
            ans = 0
            while L <= R:
                M = (L + R) // 2
                tRequired = workerTime * M * (M + 1) // 2
                if tRequired <= T:
                    ans = M
                    L = M + 1
                else:
                    R = M - 1
            return ans
        
        def checkFeasibility(t):
            h = mountainHeight
            for w in workerTimes:

                # slow way
                # candidateT = 0
                # x = 0
                # while candidateT + workerTime * (x + 1) <= t:
                #     x += 1
                #     candidateT += workerTime * x

                # fast way
                x = maxHeightReduced(w, t)
                h -= x
            return h <= 0

        L, R = 0, (mountainHeight * (mountainHeight + 1) // 2) * max(workerTimes)
        while L < R:
            M = (L + R) // 2
            if  checkFeasibility(M):
                R = M
            else:
                L = M + 1
        
        return L