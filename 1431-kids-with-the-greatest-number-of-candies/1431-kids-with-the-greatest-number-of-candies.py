class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        ans=[]
        for i in range(len(candies)):
            if((candies[i]+extraCandies)>=x):
                ans.append(True)
            else:
                ans.append(False)
        return ans