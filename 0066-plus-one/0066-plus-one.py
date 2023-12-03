class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=""
        for i in range(len(digits)):
            x+=str(digits[i])
        x=int(x)
        x+=1
        x=str(x)
        y=[int(i) for i in x]
        return y
        