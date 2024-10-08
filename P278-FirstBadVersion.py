# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 0, n
        while L < R:
            M = (L + R) // 2
            if not isBadVersion(M):
                L = M + 1
            else:
                R = M
        return L