class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            elif tx > ty:
                tx -= max(1, (tx-sx) // ty) * ty
            elif ty > tx:
                ty -= max(1, (ty-sy) // tx) * tx
            else:
                break
            
        return False