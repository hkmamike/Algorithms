class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        deque = collections.deque(bills)
        
        five = 0
        ten = 0
        twenty = 0
        
        while len(deque) > 0:
            nextItem = deque.popleft()
            
            if nextItem == 5:
                five += 1
                
            elif nextItem == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
                
            else:
                change = 15
                if ten >= 1:
                    ten -= 1
                    change -= 10
                while change > 0 and five >= 1:
                    change -= 5
                    five -= 1
                    
                if change > 0:
                    return False
                else:
                    twenty += 1
                    
        return True