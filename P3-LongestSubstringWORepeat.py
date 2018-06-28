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
