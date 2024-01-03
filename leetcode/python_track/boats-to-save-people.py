class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        x = 0
        y = len(people) - 1
        people.sort()
        count = 0
        while x <= y:
            if people[x] + people[y] > limit:
                y -= 1
                count += 1
            elif people[x] + people[y] <= limit:
                x += 1
                y -= 1
                count += 1
        return count
        