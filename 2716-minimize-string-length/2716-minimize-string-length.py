class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ls=[i for i in s]
        ls=list(set(ls))
        ss=""
        for i in range(len(ls)):
            ss+=ls[i]
        return len(ss)
            