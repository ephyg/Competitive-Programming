class Solution:
    def minimumSum(self, num: int) -> int:
        x=sorted(str(num),reverse=True)
        a=int(x[0])
        b=int(x[1])
        c=int(x[2])*10
        d=int(x[3])*10
        return a+b+c+d