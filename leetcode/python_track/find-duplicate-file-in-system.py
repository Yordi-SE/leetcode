class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(paths)):
            list1 = paths[i].split(" ")
            for j in range(1, len(list1)):
                temp = list1[j].split("(")
                content = temp[1][:len(temp[1]) - 1]
                if content in hashmap.keys():
                    hashmap[content].append(list1[0] + '/' + temp[0])
                else:
                    hashmap[content] = [list1[0] + '/' + temp[0]]
        print(hashmap)
        res = []
        for i in hashmap.keys():
            if len(hashmap[i]) >= 2:
                res.append(hashmap[i])
        return res
