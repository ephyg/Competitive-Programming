class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        you=0
        left=0
        right=len(piles)-1

        while(right>left):
            you+=piles[right-1]
            right-=2
            left+=1
        return you