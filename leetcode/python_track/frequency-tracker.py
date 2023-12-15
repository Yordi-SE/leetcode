class FrequencyTracker:

    def __init__(self):
        self.mine = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        temp = self.mine[number]
        self.mine[number] += 1
        if temp in self.freq:
            if self.freq[temp] == 1:
                del self.freq[temp]
            else:
                self.freq[temp] -= 1
        self.freq[self.mine[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.mine:
            if self.mine[number] == 1:
                del self.mine[number]
                if self.freq[1] == 1:
                    del self.freq[1]
                else:
                    self.freq[1] -= 1
            else:
                temp = self.mine[number]
                self.mine[number] -= 1
                if self.freq[temp] == 1:
                    del self.freq[temp]
                else:
                    self.freq[temp] -= 1
                self.freq[self.mine[number]] += 1


    def hasFrequency(self, frequency: int) -> bool:
        print(self.freq)
        if frequency in self.freq:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)