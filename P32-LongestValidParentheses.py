class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        length = len(s)
        maxL = [0]
        
        for i in range(1, length):
            if s[i] == '(':
                maxL.append(0)
            elif s[i-1] == "(":
                if i >=3:
                    maxL.append(2+maxL[i-2])
                else:
                    maxL.append(2)
            else:
                lastL = maxL[i-1]
                if i-lastL-2 >= 0 and s[i-lastL-1] == "(":
                    maxL.append(lastL+2+maxL[i-lastL-2])
                elif i-lastL-1 >= 0 and s[i-lastL-1] == "(":
                    maxL.append(lastL+2)
                else:
                    maxL.append(0)
                    
        return max(maxL)
        