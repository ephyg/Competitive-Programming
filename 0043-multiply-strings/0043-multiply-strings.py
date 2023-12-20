class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        ans=""
        for nums in num1:
            n1=n1*10+(ord(nums)-48)
        for nums in num2:
            n2=n2*10+(ord(nums)-48) 
        ans+=str(n1*n2)
        return ans