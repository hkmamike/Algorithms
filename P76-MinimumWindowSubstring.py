class Solution:
    def minWindow(self, s, t):
        
        i, I, J = 0, 0, 0
        missing = len(t)
        need = collections.Counter(t)
        
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            
            if not missing:
                while i<j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J==0 or j-i < J-I:
                    I, J = i, j
                    
        return s[I:J]
    
# simple solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetC = Counter(t)

        L, R, minLength = 0, 0, float('inf')
        result = ""
        C = Counter(s[0])

        while L < len(s):
            if C >= targetC:
                if R - L + 1 < minLength:
                    minLength = R - L + 1
                    result = s[L:R+1]
                C[s[L]] -= 1
                L += 1
            elif R < len(s) - 1:
                R += 1
                C[s[R]] += 1
            else:
                break

        return result

