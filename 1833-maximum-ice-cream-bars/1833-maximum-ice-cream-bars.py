class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter=0
        tot=0
        for i in range(len(costs)):
            tot+=costs[i]
            if tot<=coins:
                counter+=1
            else:
                break
        return counter