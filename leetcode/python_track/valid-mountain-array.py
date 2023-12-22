class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        num = float("-inf")
        for i in range(1,len(arr) - 1):
            if num != float("-inf"):
                if arr[i] > arr[i + 1]:
                    continue
                else:
                    return False
            elif arr[i] > arr[i + 1] and arr[i - 1] < arr[i]:
                num = arr[i]
            elif arr[i] > arr[i - 1] and num == float('-inf'):
                continue
            else:
                return False
        if num == float("-inf"):
            return False
        return True