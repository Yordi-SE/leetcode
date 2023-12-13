class Solution:
    def isHappy(self, n: int) -> bool:
        sums = n
        set1 = {n}
        while True:
            sums = str(sums)
            res = 0
            for i in sums:
                res += (int(i) ** 2)
            sums = res
            if sums in set1 and sums != 1:
                return False
            elif sums in set1 and sums == 1:
                return True
            else:
                set1.add(sums)
