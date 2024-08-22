class Solution:
    def checkValidString(self, s: str) -> bool:
        
        openCnt = 0
        wildCnt = 0
        for c in s:
            if c == "*":
                wildCnt += 1
            elif c == "(":
                openCnt += 1
            elif c == ")":
                if openCnt > 0:
                    openCnt -= 1
                elif wildCnt > 0:
                    wildCnt -= 1
                else:
                    return False

        openCnt = 0
        wildCnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "*":
                wildCnt += 1
            elif s[i] == ")":
                openCnt += 1
            elif s[i] == "(":
                if openCnt > 0:
                    openCnt -= 1
                elif wildCnt > 0:
                    wildCnt -= 1
                else:
                    return False

        return True