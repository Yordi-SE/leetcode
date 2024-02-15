class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()
        count5 = 0
        count10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            if bills[i] == 10:
                if count5 < 1:
                    return False
                else:
                    count10 += 1
                    count5 -= 1
            elif bills[i] == 20:
                if count10 < 1 and count5 < 3:
                    return False
                elif count10 >= 1 and count5 < 1:
                    return False
                if count10 >= 1 and count5 >= 1:
                    count10 -= 1
                    count5  -= 1
                elif count10 < 1 and count5 >= 3:
                    count5 -= 3
        return True