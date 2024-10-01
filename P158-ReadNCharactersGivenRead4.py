"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""

class Solution:

    def __init__(self):
        self.storage = 0
        self.fileDone = False

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        if n == 0:
            return 0
        
        cnt = 0
        if n <= self.storage:
            self.storage -= n
            return n
        elif self.storage > 0:
            n = n - self.storage
            cnt += self.storage
            self.storage = 0

        while n > 0 and not self.fileDone:
            nextBuf = Reader.read4(buf)
            if nextBuf > 0:
                taken = min(n, nextBuf)
                cnt += taken
                if nextBuf - n > 0:
                    self.storage += nextBuf - n
                n -= taken
            else:
                self.fileDone = True
                return cnt
                break
        return cnt