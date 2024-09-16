class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        C = Counter(senate)
        Rcnt = C["R"]
        Dcnt = C["D"]
        banned = [False] * len(senate)

        while Rcnt > 0 and Dcnt > 0:
            Rvote = 0
            Dvote = 0
            for i in range(len(senate)):
                if banned[i] == True:
                    continue
                if senate[i] == "R":
                    if Dvote > 0:
                        Dvote -= 1
                        banned[i] = True
                        Rcnt -= 1
                    else:
                        Rvote += 1
                elif senate[i] == "D":
                    if Rvote > 0:
                        Rvote -= 1
                        banned[i] = True
                        Dcnt -= 1
                    else:
                        Dvote += 1
            for i in range(len(senate)):
                if banned[i] == True:
                    continue
                if senate[i] == "R":
                    if Dvote > 0:
                        Dvote -= 1
                        banned[i] = True
                        Rcnt -= 1
                elif senate[i] == "D":
                    if Rvote > 0:
                        Rvote -= 1
                        banned[i] = True
                        Dcnt -= 1
                    
        if Rcnt > 0:
            return "Radiant"
        else:
            return "Dire"
