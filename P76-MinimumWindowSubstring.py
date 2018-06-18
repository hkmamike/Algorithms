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