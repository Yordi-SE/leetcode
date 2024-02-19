class MinStack:

    def __init__(self):
        self.__data = []
        

    def push(self, val: int) -> None:
        self.__data.append(val)

    def pop(self) -> None:
        del self.__data[len(self.__data) - 1]

    def top(self) -> int:
        return self.__data[len(self.__data) - 1]

    def getMin(self) -> int:
        list1 = self.__data.copy()
        list1.sort()
        return list1[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()