class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if(start<destination):
            x=sum(distance[start:destination])
            return min(x,sum(distance)-x)
        else:
            x=sum(distance[destination:start])
            return min(x,sum(distance)-x)
        
            