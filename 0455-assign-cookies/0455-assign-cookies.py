class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        counter=0
        left=0
        right=0
        while left<len(s) and right<len(g):
            if(s[left]>=g[right]):
                counter+=1
                left+=1
                right+=1
            else:
                left+=1
        return counter