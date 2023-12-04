class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        full_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            capacity = capacity - plants[i]
            # print(capacity)
            if capacity < 0:
                steps += i + 1 + i
                capacity = full_capacity - plants[i]
            else:
                steps += 1
        return steps