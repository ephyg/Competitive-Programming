class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx=-1
        left=0
        right=0
        while left<len(s):
            for i in range(len(s)-1,left,-1):
                if(s[left]==s[i]):
                    length=len(s[left+1:i])
                    mx=max(mx,length)
                    break
            left+=1
        return mx