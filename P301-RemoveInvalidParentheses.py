class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        removalCnt = 0
        openB = 0
        for c in s:
            if c == ")":
                if openB == 0:
                    removalCnt += 1
                else:
                    openB -= 1
            elif c == "(":
                openB += 1
            else:
                continue
        removalCnt += openB

        def isValid(s):
            openB = 0
            for c in s:
                if c == ")":
                    if openB == 0:
                        return False
                    else:
                        openB -= 1
                elif c == "(":
                    openB += 1
                else:
                    continue
            return openB == 0

        self.result = []
        @cache
        def backtrack(s, cnt):
            if cnt == 0:
                if isValid(s):
                    self.result.append(s)
            else:
                for i in range(len(s)):
                    backtrack(s[:i]+s[i+1:], cnt-1)

        backtrack(s, removalCnt)
        return self.result