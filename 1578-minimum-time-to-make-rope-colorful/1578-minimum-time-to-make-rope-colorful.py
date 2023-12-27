class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left=0
        right=1
        ans=0
        while(right<len(colors)):
            if(colors[left] ==colors[right]):
                ans+=min(neededTime[left],neededTime[right])
                if(neededTime[left]<=neededTime[right]):
                    left=right
            else:
                left=right
            right+=1
        return ans
    
                