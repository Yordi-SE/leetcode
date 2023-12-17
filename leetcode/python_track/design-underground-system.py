class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id]= (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        difference = t - self.customer[id][1]
        if (self.customer[id][0], stationName) in self.stations:
            self.stations[(self.customer[id][0], stationName)].append(difference)
        else:
            self.stations[(self.customer[id][0], stationName)] = [difference]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (sum(self.stations[(startStation, endStation)])/len(self.stations[(startStation, endStation)]))

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)