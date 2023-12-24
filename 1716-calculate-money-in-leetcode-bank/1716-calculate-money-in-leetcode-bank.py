class Solution:
    def totalMoney(self, n: int) -> int:
        week = n//7
        remaining_day = n % 7
        last_week=(week+week+6)*7//2
        complete_week=week*(28+last_week)//2
        remaining_week = remaining_day*(2*(week+1)+remaining_day-1)/2

        return int(complete_week+remaining_week)

            
            