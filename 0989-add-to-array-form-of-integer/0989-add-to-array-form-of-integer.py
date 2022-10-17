class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s+=str(i)
        y=int(s)
        ans=y+k
        num=str(ans)
        num=[int(i) for i in num]
        return num