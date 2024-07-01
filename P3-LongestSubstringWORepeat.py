# sliding window solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sLength = len(s)
        if sLength <= 1:
            return sLength

        L, R = 0, 1
        charsSet = set()
        charsSet.add(s[0])
        maxLength = 0

        while R < sLength:
            if s[R] in charsSet:
                charsSet.remove(s[L])
                L += 1
            else:
                charsSet.add(s[R])
                maxLength = max(maxLength, R - L + 1)
                R += 1

        return maxLength

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0
        maxLength = 0
        seenChar = {}
        length = len(s)
        
        for i in range (0, length):
            
            if s[i] in seenChar and start <= seenChar[s[i]]:
                start = seenChar[s[i]] + 1
                
            else:
                maxLength = max(maxLength, i-start+1)
                
            seenChar[s[i]] = i

        return maxLength
