class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers) - 1
        while x < len(numbers):
            if numbers[x] + numbers[y] > target:
                y -= 1
            elif numbers[x] + numbers[y] < target:
                x += 1
            else:
                return[x + 1, y + 1]
        