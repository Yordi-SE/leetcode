class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        set1 = set()
        set2 = set()
        for i in guards:
            set1.add(tuple(i))
        for i in walls:
            set2.add(tuple(i))
        # print(set1)
        # print(set2)
        set3 = set()
        counter = 0
        res2, res = [], []
        for i in guards:
            # print("II", i)
            for k in range(i[1], n):
                # print([i[0],k])
                if tuple([i[0], k]) in set1 and [i[0], k] != i:
                    break
                elif tuple([i[0], k]) in set2 and [i[0], k] != i:
                    break
                elif [i[0], k] != i:
                    if tuple([i[0], k]) not in set3:
                        counter += 1
                        set3.add(tuple([i[0], k]))
            for k in range(i[1], -1, -1):
                # print("l", [i[0],k])
                if tuple([i[0], k]) in set1 and [i[0], k] != i:
                    break
                elif tuple([i[0], k]) in set2 and [i[0], k] != i:
                    break
                elif [i[0], k] != i:
                    if tuple([i[0], k]) not in set3:
                        counter += 1
                        set3.add(tuple([i[0], k]))
            for j in range(i[0], m):
                # print("d", [j, i[1]])
                if tuple([j, i[1]]) in set1 and [j, i[1]] != i:
                    break
                elif tuple([j, i[1]]) in set2 and [j, i[1]] != i:
                    break
                elif [j, i[1]] != i:
                    if tuple([j, i[1]]) not in set3:
                        counter += 1
                        set3.add(tuple([j, i[1]]))
            for j in range(i[0], -1, -1):
                # print("u", [j, i[1]])
                if tuple([j, i[1]]) in set1 and [j, i[1]] != i:
                    break
                elif tuple([j, i[1]]) in set2 and [j, i[1]] != i:
                    break
                elif [j, i[1]] != i:
                    if tuple([j, i[1]]) not in set3:
                        counter += 1
                        set3.add(tuple([j, i[1]]))
        return (m * n) - counter - len(guards) - len(walls)

                
