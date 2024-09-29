
# O(N)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atLeast(num):
            charTypes = "aeiouz"
            L, R, N = 0, 0, len(word)
            cnt = defaultdict(int)
            result = 0

            while R < N:
                # add word[R] into counter
                ch = word[R]
                if ch in "aeiou":
                    cnt[ch] += 1
                else:
                    cnt["z"] += 1
    
                # check valid condition
                isValid = True
                for c in "aeiou":
                    if cnt[c] == 0:
                        isValid = False
                        break
                if cnt["z"] < num:
                    isValid = False

                # Shrink L
                while isValid:
                    result += (N - R)
                    ch = word[L]
                    if ch in "aeiou":
                        cnt[ch] -= 1
                    else:
                        cnt["z"] -= 1

                    isValid = True
                    for c in "aeiou":
                        if cnt[c] == 0:
                            isValid = False
                            break
                    if cnt["z"] < num:
                        isValid = False
                    L += 1
                R += 1
            return result
        return atLeast(k) - atLeast(k+1)

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