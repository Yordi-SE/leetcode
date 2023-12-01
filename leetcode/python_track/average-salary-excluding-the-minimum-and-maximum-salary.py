class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sal = salary[1:len(salary) - 1]
        print(salary[1:len(salary) - 1])
        return round(sum(sal) / len(sal), 5)