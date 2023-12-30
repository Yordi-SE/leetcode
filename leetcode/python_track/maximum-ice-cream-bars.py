class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        storage = [0] * (max(costs) + 1)
        for i in costs:
            storage[i] += 1
        res = []
        for i in range(len(storage)):
            for j in range(storage[i]):
                res.append(i)
        sums = 0
        for i in range(len(res)):
            sums += res[i]
            if sums > coins:
                return i
            elif sums == coins:
                return i + 1
        else:
            return len(res)
            
        
