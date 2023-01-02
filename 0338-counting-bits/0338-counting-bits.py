class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            x=bin(i)
            x=x[2:]
            x=str(x)
            ans.append(x.count('1'))
        return ans
            
            
        