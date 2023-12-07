class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest_index = -1
        for i in range(len(num)):
            if int(num[i]) % 2:
                largest_index = i
        return num[:largest_index+ 1]