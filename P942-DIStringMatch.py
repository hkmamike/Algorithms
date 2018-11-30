class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left,right=0,len(S)
        
        res=[]
        
        for i in S:
            if i =='I':
                res.append(left)
                left+=1
            else:
                res.append(right)
                right-=1
        
        if S[-1] == "I":
            return res + [left]
        else:
            return res + [right]
        
                