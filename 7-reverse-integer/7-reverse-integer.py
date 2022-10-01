class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            y = str((-1)*(x))
            y = int((y[::-1])) * (-1)
            if (y<=(-1*(2**31)-1)):
                return 0
            else:
                return y
        else:
            y = str(x)
            y = int(y[::-1])
            if (y>=(2**31)-1):
                return 0
            else:
                return y
