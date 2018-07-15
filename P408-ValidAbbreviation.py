class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        i = 0
        j = 0
        
        while j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            
            elif abbr[j] == '0':
                return False
            
            shift = 0
            
            while j < len(abbr) and abbr[j].isdigit():
                shift = shift*10 + int(abbr[j])
                j += 1
                
            i += shift
            
            if i > len(word):
                return False
            elif i < len(word) and word[i] != abbr[j]:
                return False
                
        return i == len(word)