class Solution:
    def isHappy(self, n: int) -> bool:
        s=str(n)
        let=[]
        while True:
            summed=sum([int(i)**2 for i in s])
            if(summed==1):
                return True
            else:
                if(summed in let):
                    break
                s=str(summed)
                let.append(summed)
        return False