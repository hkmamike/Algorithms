class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        digits = []
        
        for log in logs:
            checkType = log.split()[1]
            if checkType.isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        return sorted(letters, key = lambda x: ' '.join(x.split()[1:])) + digits