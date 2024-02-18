class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        self.counter.append(t)
        lower_range = t-3000
        while self.counter[0] < lower_range:
            self.counter.popleft()
        
        # count = 0
        # for i in self.counter:
        #     if lower_range <= i and i <= t:
        #         count+= 1
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)