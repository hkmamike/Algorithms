class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.leaderAtT = []
        self.times = times
        self.length = len(persons)
        
        counter = {}
        for i in range(len(persons)):
            if persons[i] in counter:
                counter[persons[i]] += 1
            else:
                counter[persons[i]] = 1
                
            if i == 0:
                self.leaderAtT.append(persons[i])
            else:
                if counter[persons[i]] >= counter[self.leaderAtT[-1]]:
                    self.leaderAtT.append(persons[i])
                else:
                    self.leaderAtT.append(self.leaderAtT[-1])
                    

    def q(self, t: int) -> int:
        
        # binary search for the index where last vote happened before t
        L = 0
        R = self.length - 1
        
        while L < R:
            M = (L+R) // 2
            if self.times[M] <= t and self.times[M+1] > t:
                L = M
                break
            elif self.times[M] > t:
                R = M
            else:
                L = M + 1
                
        return self.leaderAtT[L]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)