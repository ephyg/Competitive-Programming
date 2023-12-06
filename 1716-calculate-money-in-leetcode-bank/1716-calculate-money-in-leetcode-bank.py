class Solution:
    def totalMoney(self, n: int) -> int:
        q = n//7
        r = n % 7

        complete_week = 7*((q*(q-1))/2) + (28*q)
        remaining_week = (r*(2*q+r+1))/2

        return int(complete_week+remaining_week)

            
            