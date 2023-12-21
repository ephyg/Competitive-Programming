class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can=capacity
        steps=0
        for i in range(len(plants)):
            if(can>=plants[i]):
                steps+=1
                can=can-plants[i]
            else:
                steps+=1
                steps+=(i*2)
                can=capacity-plants[i]
                print(can)
        return steps