class Bitset:

    def __init__(self, size: int):
        self.bitset = ["0"] * size
        self.set0 = set(range(size))
        self.set1 = set()

    def fix(self, idx: int) -> None:
        self.set0.discard(idx)
        self.set1.add(idx)
    def unfix(self, idx: int) -> None:
        self.set1.discard(idx)
        self.set0.add(idx)    
    def flip(self) -> None:
        self.set1, self.set0 = self.set0, self.set1

    def all(self) -> bool:
        return len(self.set0) == 0

    def one(self) -> bool:
        return len(self.set1) != 0
    def count(self) -> int:
        return len(self.set1)

    def toString(self) -> str:
        for i in self.set0:
            self.bitset[i] = "0"
        for i in self.set1:
            self.bitset[i] = "1"
        return "".join(self.bitset)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()