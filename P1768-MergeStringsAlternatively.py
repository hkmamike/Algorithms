class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        merged = [word1[i] + word2[i] for i in range(minLen)]

        if len(word1) < len(word2):
            merged += [word2[minLen:]]
        elif len(word2) < len(word1):
            merged += [word1[minLen:]]

        return ''.join(merged)
