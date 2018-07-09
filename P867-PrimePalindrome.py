class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        def makePalindrome(n):
            if n == 1:
                for i in range(10):
                    yield i
            elif n % 2 == 0:
                d = n//2
                for i in range(10**(d-1), 10**d):
                    s = str(i)
                    yield int(s+s[::-1])
            else:
                d = n // 2
                for i in range(10**(d-1), 10**d):
                    s = str(i)
                    for j in range(10):
                        yield int(s + str(j) +s[::-1])
                
        def isPrime(n):
            if n == 1:
                return False
            elif n == 2:
                return True
            
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
            
        digitCnt = len(str(N))
        while True:
            for x in makePalindrome(digitCnt):
                if x >= N and isPrime(x):
                    return x
            digitCnt += 1