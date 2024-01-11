class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        pre_sum=[]
        ps=0
        counter=0
        for i in range(len(flips)):
            ps+=flips[i]
            pre_sum.append(ps)
            calc=(i+1)*(1+(i+1))//2
            if pre_sum[i]==calc:
                counter+=1
        return counter
            