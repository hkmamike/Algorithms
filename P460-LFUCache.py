class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.totalCap = capacity
        self.slot = capacity
        self.cache = {}
        self.cnt = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.totalCap == 0:
            return -1
        
        self.cnt += 1
        if key in self.cache:
            self.cache[key][1] += 1
            self.cache[key][2] = self.cnt
            return self.cache[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.totalCap == 0:
            return -1
        
        self.cnt += 1
        if self.slot == 0 and key not in self.cache:
            minUsedCnt = float("inf")
            minUsedKey = []
            
            for entry in self.cache:
                if self.cache[entry][1] < minUsedCnt:
                    minUsedCnt = self.cache[entry][1]
                    minUsedKey = [entry]
                elif self.cache[entry][1] == minUsedCnt:
                    minUsedKey.append(entry)
                
            # print('minUsedKey', minUsedKey)
            #remove key
            if len(minUsedKey) == 1:
                del self.cache[minUsedKey[0]]
                self.slot += 1
            else:
                earliest = self.cnt+1
                delKey = None
                
                for entry in minUsedKey:
                    timeStamp = self.cache[entry][2]
                    if timeStamp < earliest or not delKey:
                        earliest = timeStamp
                        delKey = entry
                
                del self.cache[delKey]
                self.slot += 1
        
        if key not in self.cache:
            self.cache[key] = [value, 0, self.cnt]
            self.slot -= 1
            
        else:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] += self.cnt
            
#         print(key, value)
#         print(self.cache)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)