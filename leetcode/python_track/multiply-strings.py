class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        temp = 0
        res = ""
        if "0" == num1 or "0" == num2:
            return "0"
        ress = [0] * (len(num1) + len(num2))
        for i, u in enumerate(num2):
            for j, k in enumerate(num1):
                val = int(num1[j]) * int(num2[i])
                ress[i + j] += (val % 10) 
                ress[i + j + 1] += (val // 10)
                index = i + j
        for i in range(len(ress)):
            if ress[i] > 9:
                ress[i + 1] += (ress[i] // 10)
                ress[i] = (ress[i] % 10)
        ress = ress[::-1]
        for i, k in enumerate(ress):
            if k != 0:
                index = i
                ress = ress[index:]
                break
        ress = list(map(str, ress))
        return "".join(ress)
        