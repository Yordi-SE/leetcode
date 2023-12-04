class Solution:
    def largestGoodInteger(self, num: str) -> str:
        hashmap = {}
        for i in range(9, -1, -1):
            hashmap[str(i) + str(i) + str(i)] = 1
        temp = ""
        for i in range(len(num)):
            if num[i:i + 3] in hashmap.keys():
                if temp < num[i:i + 3]:
                    temp = num[i:i + 3]
        return temp