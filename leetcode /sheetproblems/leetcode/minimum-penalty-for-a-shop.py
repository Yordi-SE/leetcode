class Solution:
    def bestClosingTime(self, customers: str) -> int:
        list1 = list(customers)
        for i in range(len(customers)):
            if list1[i] == "N":
                list1[i] = 0
            else:
                list1[i] = 1
        prefix = [list1[0]]
        for i in range(1,len(list1)):
            prefix.append(prefix[-1]+list1[i])
        mins = [prefix[len(prefix) - 1]]
        for i in range(len(prefix)):
            if i == len(list1) - 1:
                mins.append(i - prefix[i-1])
            else:
                mins.append((prefix[len(prefix) - 1] - prefix[i]) + (i - prefix[i] +1))
        mins2 = float('inf')
        for i in range(len(mins)):
            if mins2 > mins[i]:
                mins2 = mins[i]
                idx = i
        return idx