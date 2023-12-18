class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        on_both = set()
        min_good = float('inf')
        for i, j in zip(fronts, backs):
            if i == j:
                on_both.add(i)
        for i, j in zip(fronts, backs):
            if j not in on_both and i not in on_both:
                min_good = min(min_good, j, i)
            elif j not in on_both:
                min_good = min(min_good, j)
            elif i not in on_both:
                min_good = min(min_good, i)
        if min_good == float('inf'):
            return 0
        return min_good
            
