class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            if n == 1:
                return True
            strN = str(n)
            digitList = list(strN)
            n = sum([int(d) * int(d) for d in digitList])
            if n in visited:
                return False
            else:
                visited.add(n)