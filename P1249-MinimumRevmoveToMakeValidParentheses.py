class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        sList = list(s)
        firstPassResult = []
        openB = 0
        for c in sList:
            if c == "(":
                openB += 1
                firstPassResult.append(c)
            elif c == ")":
                if openB > 0:
                    openB -= 1
                    firstPassResult.append(c)
                else:
                    continue
            else:
                firstPassResult.append(c)
        
        # then remove for first open brackets until balanced
        result = []
        for i in range(len(firstPassResult) - 1, -1, -1):
            if firstPassResult[i] == "(" and openB > 0:
                openB -= 1
                continue
            else:
                result.append(firstPassResult[i])
                
        result.reverse()
        return "".join(result)