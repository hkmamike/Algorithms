class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if len(words1) != len(words2):
            print(len(words1), len(words2))
            return False
            
        # build hashMap
        wordMap = {}
        for pair in pairs:
            if pair[0] not in wordMap:
                wordMap[pair[0]] = pair
            else:
                wordMap[pair[0]].append(pair[1])
                
            if pair[1] not in wordMap:
                wordMap[pair[1]] = pair
            else:
                wordMap[pair[1]].append(pair[0])
            
        for i in range(len(words1)):
            if words1[i] not in wordMap[words2[i]]:
                print(words1[i], words2[i], wordMap[words2[i]])
                return False
                
        return True