class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here]
        
        def mirror(half):
            mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
            half = half[::-1]
            result = ''
            
            for char in half:
                result += mapping[char]
                
            return result
        
        def generateHalfs(build, n, halfs):
            allNums = ['0', '1', '6', '8', '9']
            if n == 0:
                halfs.append(build)
            else:
                for num in allNums:
                    if build == "" and num == '0':
                        continue
                    generateHalfs(build+num, n-1, halfs)
            
        halfLength = n // 2
        halfs = []
        generateHalfs('', halfLength, halfs)
            
        if n % 2 == 0:
            for i in range(len(halfs)):
                halfs[i] = halfs[i] + mirror(halfs[i])
                
            return halfs
            
        else:
            oddResult = []
            selfMirrors = ['0', '1', '8']
            for i in range(len(halfs)):
                for num in selfMirrors:
                    oddEntry = halfs[i] + num + mirror(halfs[i])
                    oddResult.append(oddEntry)
                
            return oddResult