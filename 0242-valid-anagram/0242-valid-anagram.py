class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss=Counter(s)
        for i in t:
            if ss[i]>0:
                ss[i]-=1
            else:
                return False
        return len(s)==len(t)