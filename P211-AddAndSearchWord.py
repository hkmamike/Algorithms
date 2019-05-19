class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word + "$":
            node = node.setdefault(c, {})
         

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def find(word, idx, node):
            if word[idx] == "$":
                return "$" in node
            elif word[idx] != ".":
                return word[idx] in node and find(word, idx+1, node[word[idx]])
            else:
                return any([find(word, idx+1, child) for child in node.values()])
        
        return find(word+"$", 0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)