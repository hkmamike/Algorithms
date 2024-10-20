class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        result = 0
        N = len(s)

        for i in range(N):
            C = defaultdict(int)
            maxF = 0

            for j in range(i, N):
                C[s[j]] += 1
                maxF = max(maxF, C[s[j]])
                if maxF >= k:
                    result += N - j
                    break
        return result

# Too Slow
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        result = 0
        for i in range(len(s)):
            C = Counter()
            for j in range(i, len(s)):
                C[s[j]] += 1
                if C.most_common(1)[0][1] >= k:
                    result += len(s) - j
                    break
        return result





