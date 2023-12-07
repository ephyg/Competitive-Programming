class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        for i in range(len(num)):
            n = num[:len(num) - i]
            
            if int(num[len(num)-i-1]) % 2 != 0:
                ans = n
                break
        return ans
