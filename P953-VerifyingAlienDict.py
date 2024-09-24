class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        translatedWords = []
        for w in words:
            candidate = ""
            for c in w:
                normalOrd = order.index(c)
                candidate += chr(ord("a") + normalOrd)
            translatedWords.append(candidate)
        
        return sorted(translatedWords) == translatedWords

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        m = {}
        for i, c in enumerate(order):
            m[c] = i
        
        mappedWords = []
        for w in words:
            charValues = []
            for c in w:
                charValues.append(m[c])
            mappedWords.append(charValues)
        
        
        zipped = zip(mappedWords, mappedWords[1:])
        return all(w1 <= w2 for w1, w2 in zipped)