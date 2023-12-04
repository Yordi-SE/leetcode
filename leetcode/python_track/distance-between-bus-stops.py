class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        d1 = distance[start:destination]
        d11 = 0
        d22 = 0
        for i in d1:
            d11 += i
        d2 = (distance[destination:] + distance[:start])
        for i in d2:
            d22 += i
        if d11 < d22:
            return d11
        return d22