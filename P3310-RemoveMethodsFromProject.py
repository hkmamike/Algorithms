class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        calls = defaultdict(set)
        dependencies = defaultdict(set)
        for c, d in invocations:
            calls[c].add(d)
            dependencies[d].add(c)

        suspicious = set()
        suspiciousVisited = set()
        D = deque()
        D.append(k)

        # build suspicious list
        while len(D) > 0:
            for _ in range(len(D)):
                node = D.popleft()
                suspicious.add(node)
                for d in calls[node]:
                    if d not in suspiciousVisited:
                        D.append(d)
                        suspiciousVisited.add(d)

        removeSet = set()
        canBeRemoved = True
        for s in suspicious:
            for d in dependencies[s]:
                if d not in suspicious:
                    canBeRemoved = False
                    break
        if canBeRemoved:
            removeSet = removeSet.union(suspicious)

        result = []
        for i in range(n):
            if i not in removeSet:
                result.append(i)
        return result

