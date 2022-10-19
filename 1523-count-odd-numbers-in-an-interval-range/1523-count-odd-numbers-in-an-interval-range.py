class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if(low%2==0):
            low=low+1
        if(high%2==0):
            high=high-1
        x=(high-low+2)/2
        return int(x)