class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total=sum(prices[0:2])        
        if(money>=total):
            return money-total
        else:
            return money
            