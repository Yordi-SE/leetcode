class OrderedStream:
    
    def __init__(self, n: int):
        self.stream = [0] * n
        self.pointer = 0
        self.waitlist = [0] * n
        self.n = n
    def insert(self, idKey: int, value: str) -> List[str]:
        self.waitlist[idKey - 1] = value
        if idKey - 1 == self.pointer:
            for i in range(idKey - 1, self.n):
                if self.waitlist[i] != 0:
                    self.stream[i] = self.waitlist[i]
                    index = i
                else:
                    break
                self.pointer += 1
            return self.stream[idKey - 1:index + 1]
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)