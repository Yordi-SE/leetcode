class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n
        for i in bookings:
            prefix[i[0] - 1] += i[2]
            if i[1] < n:
                prefix[i[1]] -= i[2]
        prefix2 = [prefix[0]]
        for i in range(1,len(prefix)):
            prefix2.append(prefix2[-1] + prefix[i])
        return prefix2