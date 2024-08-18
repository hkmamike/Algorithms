class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        
        countMap = {}
        def count(s, start, end, k):

            def fulfilled(s, start, end, k):
                candidateId = str(start) + "|" + str(end-1)
                if candidateId in countMap:
                    return countMap[candidateId][2]

                lastId = str(start) + "|" + str(end-2)
                if lastId in countMap:
                    endIsOne = 1 if s[end-1] == "1" else 0
                    num1 = countMap[lastId][0] + endIsOne
                    num0 = (end - start) - num1
                    if lastId in countMap:
                        del countMap[lastId]
                else:
                    substring = s[start:end]
                    num1 = sum([int(c) for c in substring])
                    num0 = len(substring) - num1
                
                result = num1 <= k or num0 <= k
                countMap[candidateId] = (num1, num0, result)
                return result
            
            result = 0
            for i in range(start, end+1):
                for j in range(i+1, end+2):
                    if fulfilled(s, i, j, k):
                        result += 1
            return result

        queryResults = []
        for query in queries:
            queryResults.append(count(s, query[0], query[1], k))
        return queryResults
