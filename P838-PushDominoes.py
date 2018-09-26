class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        R = -1
        dominoes = list(dominoes)
        for i in range(len(dominoes)):
            flag = 0
            if dominoes[i] == '.':
                flag = 1
                pass
            elif dominoes[i] == 'R' and R == -1:
                flag = 2
                R = i
            elif dominoes[i] == 'R' and R != -1:
                flag = 3
                j = R
                while j < i:
                    dominoes[j] = 'R'
                    j += 1
                R = i
            elif dominoes[i] == 'L' and R == -1:
                flag = 4
                j = i-1
                while dominoes[j] == '.' and j>=0:
                    dominoes[j] = "L"
                    j -= 1
            elif dominoes[i] == 'L':
                flag = 5
                mid = (i+R) / 2
                j = i
                while j > mid:
                    dominoes[j] = 'L'
                    j -= 1
                k = R
                while k < mid:
                    dominoes[k] = "R"
                    k += 1
                R = -1
                
        if R != -1:
            while R <= len(dominoes)-1:
                dominoes[R] = 'R'
                R += 1
                
        return ''.join(dominoes)
        