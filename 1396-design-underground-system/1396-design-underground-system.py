class UndergroundSystem:

    def __init__(self):
        self.check_in={}
        self.check_out=defaultdict(lambda:[0,0])
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]=[stationName,t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkout= self.check_out
        checkin=self.check_in
        key=(checkin[id][0],stationName)
        checkout[key][0]+=t-checkin[id][1]
        checkout[key][1]+=1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key=(startStation,endStation) 
        return self.check_out[key][0]/self.check_out[key][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)