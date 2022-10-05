class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        BoolCheck=False
        while(True):
            x=pow(2,i)
            i+=1
            if(x==n):
                return True
            if(x>n):
                return False