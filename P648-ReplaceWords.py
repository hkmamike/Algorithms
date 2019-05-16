class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        
        root = {}
        for entry in dict:
            node = root
            for c in entry + "$":
                node = node.setdefault(c, {})
    
        def replace(word):
            def search(word, idx, node):
                if "$" in node:
                    return word[:idx]
                elif idx == len(word) - 1 or word[idx] not in node:
                    return word
                else:
                    return search(word, idx+1, node[word[idx]])
            
            returnWord = search(word, 0, root)
            return returnWord
            
        sentenceList = sentence.split()
        for i in range(len(sentenceList)):
            sentenceList[i] = replace(sentenceList[i])
        
        return " ".join(sentenceList)