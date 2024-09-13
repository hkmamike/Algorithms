class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        temp = []
        starCnt = 0
        for i in range(n-1, -1, -1):
            if s[i] == "*":
                starCnt += 1
            elif starCnt == 0:
                temp.append(s[i])
            else:
                starCnt -= 1
        return ''.join(temp)[::-1]
