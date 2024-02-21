class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counter = Counter(senate)
        arr = deque(senate)
        i = 0
        while True:
            # i = i % len(arr)
            # print(arr,i)
            # print(counter)
            if arr[0] == "R" and len(counter) > 1:
                for j in range(len(arr)):
                    if arr[j] == "D":
                        if counter[arr[j]] <= 1:
                            del counter[arr[j]]
                        else:
                            counter[arr[j]] -= 1
                        arr[j] = 0
                        break
            elif arr[0] == "D" and len(counter) > 1:
                for j in range(len(arr)):
                    if arr[j] == "R":
                        
                        if counter[arr[j]] <= 1:
                            del counter[arr[j]]
                        else:
                            counter[arr[j]] -= 1
                        arr[j] = 0
                        break
            elif arr[i] != 0 and len(counter) <= 1:
                for i in counter:
                    if i == "R":
                        return "Radiant"
                    else:
                        return "Dire"
            poped = arr.popleft()
            arr.append(poped)
            # i += 1