class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)
        left = 0
        right = len(skill) - 1
        res = []
        product = 0
        while left < right:
            skills = skill[left] + skill[right]
            if len(res) > 0 and res[-1] != skills:
                return -1
            res.append(skills)
            product += (skill[left] * skill[right])
            left += 1
            right -= 1
        return product
