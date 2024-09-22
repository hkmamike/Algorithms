class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedSet = set(bannedWords)
        cnt = 0
        for m in message:
            if m in bannedSet:
                cnt += 1
        
        return cnt >= 2