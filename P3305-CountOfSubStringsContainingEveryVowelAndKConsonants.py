


# N^2
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        result = 0
        
        for L in range(n):
            consonantCnt = 0
            vowelCnt = Counter()
            for R in range(L, n):
                ch = word[R]
                if ch in vowels:
                    vowelCnt[ch] += 1
                else:
                    consonantCnt += 1
                if consonantCnt > k:
                    break
                elif consonantCnt == k and len(vowelCnt) == 5:
                    result += 1
        return result