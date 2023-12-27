class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        x=set()
        union=set(fronts+backs)
        min_=float("inf")
        for i in range(len(fronts)):
            if(fronts[i]==backs[i]):
                x.add(backs[i])
        for i in union:
            if(i not in x):
                min_=min(i,min_)
        if(min_ != float("inf")):
            return min_
        else:
            return 0
            
        