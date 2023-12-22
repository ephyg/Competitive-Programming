class Solution:
    def maxScore(self, s: str) -> int:
        ans=[]
        for i in range(len(s)-1):
            left=s[:i+1].count('0')
            right=s[i+1:].count('1')
            ans.append(left+right)
        return max(ans)
            