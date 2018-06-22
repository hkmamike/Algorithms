class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 0:
            return 0
        
        length = len(primes)
        ugly = [1]
        primesI = [0 for _ in range(length)]
        
        while len(ugly) < n:
            candidates = []
                                    
            for i in range(length):
                print(primes[i])
                print(ugly[primesI[i]])
                print('product', primes[i]*ugly[primesI[i]])
                candidates.append(primes[i]*ugly[primesI[i]])
                
            minV = min(candidates)
            ugly.append(minV)
                                    
            for i in range(length):
                if candidates[i] == minV:
                    primesI[i] += 1
                                    
        return ugly[-1]