class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        index_sum = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                # print(list1[i])
                # print(list2[j] == list1[i])
                if list1[i] == list2[j]:
                    if index_sum > i + j:
                        res = []
                        res.append(list1[i])
                        index_sum = i +j 
                        break
                    elif index_sum == i+j:
                        res.append(list1[i])
                        break
        return res
        