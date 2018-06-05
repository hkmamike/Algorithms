class MapSum:

    def __init__(self):
        self.map = {}
        
    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        count = 0
        prefixLen = len(prefix)
        
        for entry in self.map:
            if prefix == entry[0:prefixLen]:
                count += self.map[entry]
                
        return count