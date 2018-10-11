import math

class Solution(object):
    def reachNumber(self, target):
        n = int(math.ceil(math.sqrt(2*abs(target)+0.25)-0.5))
        diff = n*(n+1)/2-target
        if diff%2 == 0: return n
        else: return n+1+n%2