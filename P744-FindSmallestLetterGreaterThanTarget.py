class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        diffs = []
        
        for char in letters:
            diffs.append(ord(char) - ord(target))
            
        if max(diffs) <= 0:
            return chr(min(diffs) + ord(target))
        else:
            return chr(min([i for i in diffs if i > 0]) + ord(target))