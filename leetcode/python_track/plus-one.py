class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i, u in enumerate(digits):
            if u == 9 and i == len(digits) - 1:
                digits[i] = 0
                digits.append(1)
                break
            elif u == 9 and digits[i + 1] != 9:
                digits[i] = 0
                digits[i + 1] = digits[i + 1] + 1
                break
            elif u == 9:
                digits[i] = 0
            elif u != 9:
                digits[i] = digits[i] + 1
                break
        digits.reverse()
        return digits