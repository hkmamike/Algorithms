class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here

        dependencies = { c:0 for word in words for c in word }
        neighbors = { c:[] for word in words for c in word }

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    dependencies[words[i+1][j]] += 1
                    neighbors[words[i][j]].append(words[i+1][j])
                    break
        
        noDep = deque([ch for ch in dependencies if dependencies[ch] == 0])
        result = []

        while noDep:
            for _ in range(len(noDep)):
                c = noDep.popleft()
                result.append(c)
                for neighbor in neighbors[c]:
                    dependencies[neighbor] -= 1
                    if dependencies[neighbor] == 0:
                        noDep.append(neighbor)

        if len(result) != len(dependencies): return ""
        return "".join(result)