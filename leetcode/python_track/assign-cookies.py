class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        # setG = set(g)
        s.sort()
        first = 0
        second = 0
        counter = 0
        print(g)
        print(s)
        while first < len(g) and second < len(s):
            if g[first] <= s[second]:
                counter +=1 
                first +=1
            second += 1

        return counter
            