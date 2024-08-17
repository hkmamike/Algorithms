class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            return self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, n % 2)
        