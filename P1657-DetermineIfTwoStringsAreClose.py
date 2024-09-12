class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False

        C1 = Counter(word1)
        C2 = Counter(word2)

        Occurence1 = []
        Occurence2 = []
        for k, v in C1.items():
            Occurence1.append(v)
        for k, v in C2.items():
            Occurence2.append(v)

        return sorted(Occurence1) == sorted(Occurence2)
