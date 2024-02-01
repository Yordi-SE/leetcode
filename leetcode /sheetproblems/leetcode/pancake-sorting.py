class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        if sorted(arr) == arr:
            return []
        for i in range(len(arr)):
            maxs = max(arr[:len(arr)-i])
            idx = arr.index(maxs)
            arr = list(reversed(arr[0:idx + 1:])) + arr[idx+1:]
            arr = list(reversed(arr[0:len(arr)-i])) + arr[len(arr)-i:]
            res.append(idx+1)
            res.append(len(arr)-i)
        return res
