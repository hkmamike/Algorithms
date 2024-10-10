# Oct 2024, cleaner, same big O but less efficient
class Solution:
    def isPalindrome(self, s: str) -> bool:

        lowerS = s.lower()
        lowerSAlpha = "".join([c for c in lowerS if c.isalnum()])
        return lowerSAlpha == lowerSAlpha[::-1]



class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = ''.join([c for c in s if c.isalnum()])
        loweredCleanS = cleanedS.lower()

        L = 0
        R = len(loweredCleanS)-1
        while L <= R:
            if loweredCleanS[L] != loweredCleanS[R]:
                return False
            L += 1
            R -= 1

        return True
