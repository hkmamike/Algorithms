class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        pCnt = Counter(p)
        windowCnt = Counter(s[:len(p)])
        L, R = 0, len(p)-1
        result = []

        # manually do initial window
        if windowCnt == pCnt:
            result.append(0)

        while R < (N-1):
            # move window
            windowCnt[s[L]] -= 1
            L += 1
            R += 1 
            windowCnt[s[R]] += 1
            if windowCnt == pCnt:
                result.append(L)
        
        return result

