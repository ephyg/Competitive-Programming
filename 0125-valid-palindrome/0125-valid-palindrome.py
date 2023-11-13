class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        alphabets = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        small_string = ""
        for i in range(len(s)):
            if (s[i] in alphabets):
                small_string += s[i].lower()
        left = 0
        right = len(small_string)-1
        if ((len(small_string)) <= 1):
            return True
        for i in range(len(small_string)):
            if (right > left):
                if (small_string[left] != small_string[right]):
                    return False
                left += 1
                right -= 1
        return True