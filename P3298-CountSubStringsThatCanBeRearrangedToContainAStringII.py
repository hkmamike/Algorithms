class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        word2Counter = Counter(word2)
        requiredCnt = len(word2Counter)
        formed = 0
        windowCounts = defaultdict(int)
        left, right = 0, 0
        total = 0
        lenWord1 = len(word1)

        while right < lenWord1:
            character = word1[right]
            windowCounts[character] += 1

            if character in word2Counter and windowCounts[character] == word2Counter[character]:
                formed += 1

            while left <= right and formed == requiredCnt:
                total += lenWord1 - right
                character = word1[left]
                windowCounts[character] -= 1

                if character in word2Counter and windowCounts[character] < word2Counter[character]:
                    formed -= 1
                left += 1
            right += 1

        return total