class Solution:
    def myPow(self, x: float, n: int) -> float:
        z=pow(x,n)
        return round(z,5)