class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        
        perms = itertools.permutations(A)
        validEntries = []
        
        for p in perms:

            if p[:2] < (2, 4) and p[2] < 6:
                validEntries.append("%d%d:%d%d" % p)
            else:
                validEntries.append("")

        return max(validEntries)
