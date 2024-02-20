class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sums = 0
        for i in range(len(arr)):
            while stack and stack[-1][1] >= arr[i]:
                # print("i",i)
                ans = stack.pop()
                if stack:
                    sums +=  ((((i - 1) - ans[0] + 1) * (ans[0] - (stack[-1][0] + 1) + 1)) * ans[1])
                    # print(((i - 1) - ans[0] + 1) ,ans[1])
                else:
                    sums += ((((ans[0] + 1)*(i - 1 + 1 - ans[0])) * ans[1]))
                    # print((i - 1 + 1 - ans[0]), ans[1])
            # print("==============================")
            stack.append((i,arr[i]))
        for i,u in enumerate(stack):
            if i == 0:
                sums += ((((u[0] + 1) * (len(arr) - 1 - u[0] + 1))) * u[1])
                # print((len(arr) - 1 - u[0] + 1),u[1])
            else:
                sums +=(((u[0] - (stack[i - 1][0] + 1) + 1) * (len(arr) - 1 - u[0] + 1)) * u[1])
                # print((stack[i - 1][0] + 1),u[0])
        return sums %(10 ** 9 + 7)