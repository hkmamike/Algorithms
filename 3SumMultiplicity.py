class Solution:
    def threeSumMulti(self, A, target):

        valueCount = {}
        for i, a in enumerate(A):
            if a in valueCount:
                valueCount[a] += 1
            else:
                valueCount[a] = 1
                
        counter = 0
        for i in valueCount:
            for j in valueCount:
                if j < i:
                    continue
                
                diff = target - i - j
                
                if diff in valueCount:
                    if i == j and j == diff:
                        counter += valueCount[i] * (valueCount[j] - 1) * (valueCount[diff] - 2) / 6
                    elif i == j and j != diff:
                        counter += valueCount[i] * (valueCount[j] - 1) / 2 * valueCount[diff]
                    elif diff < i and diff < j:
                        counter += valueCount[i] * valueCount[j] * valueCount[diff]
                            
        return int(counter) % (10 ** 9 + 7)
        