class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sums = 0
        costs.sort(key=lambda x:x[0]-x[1])
        for i in range(len(costs)):
            if i < len(costs) // 2:
                sums += costs[i][0]
            else:
                sums += costs[i][1]
        return sums