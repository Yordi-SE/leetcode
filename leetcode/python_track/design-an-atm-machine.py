class ATM:

    def __init__(self):
        self.depositi = {20:0, 50:0, 100:0, 200:0, 500: 0}
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.depositi[self.notes[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(len(self.notes) - 1,-1, -1):
            freq = self.depositi[self.notes[i]]
            if freq == 0:
                continue
            else:
                n = amount // self.notes[i]
                if n > freq:
                    amount = amount - (freq * self.notes[i])
                    res[i] = freq
                elif n <= freq:
                    amount = amount - (n * self.notes[i])
                    res[i] = n
                if amount == 0:
                    break
        if amount != 0:
            return [-1]
        else:
            for i,u in enumerate(self.notes):
                if self.depositi[u] >= res[i]:
                    self.depositi[u] -= res[i]
                else:
                    self.depositi[u] = 0
        return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)