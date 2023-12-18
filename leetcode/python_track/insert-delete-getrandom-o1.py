class RandomizedSet:

    def __init__(self):
        self.set1 = set()
        self.mins = float('inf')
        self.maxs = float('-inf')

    def insert(self, val: int) -> bool:
        if val in self.set1:
            idx = False
        else:
            idx = True
        self.set1.add(val)
        self.mins = min(self.mins, val)
        self.maxs = max(self.maxs, val)
        return idx

    def remove(self, val: int) -> bool:
        if val in self.set1:
            idx = True
        else:
            idx = False
        self.set1.discard(val)
        if val == self.mins:
            if len(self.set1) != 0:
                self.mins = min(self.set1)
            else:
                self.mins = float('inf')
        elif val == self.maxs:
            if len(self.set1) != 0:
                self.maxs = max(self.set1)
            else:
                self.maxs = float('-inf')
        return idx
    def getRandom(self) -> int:
        return random.sample(self.set1,1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()