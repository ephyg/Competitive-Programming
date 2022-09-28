class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        z = x
        if (z < 0):
            return False
        if (x < 10):
            y *= 10
            y += x
        while (x >= 10):
            y *= 10
            y += x % 10
            x = x//10
            if (x < 10):
                y *= 10
                y += x
        if (z == y):
            return True
        else:
            return False
            
palindrome = Solution()
print(palindrome.isPalindrome(-121))
