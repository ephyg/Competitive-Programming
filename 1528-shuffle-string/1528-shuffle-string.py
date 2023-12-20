class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=""
        ls=[0]*len(s)
        for i in range(len(s)):
            ls[indices[i]]=s[i]
        return "".join(ls)
        