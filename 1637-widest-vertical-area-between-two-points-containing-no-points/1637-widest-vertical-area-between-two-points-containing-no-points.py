class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # [[7,4],[8,7],[9,7],[9,9]]
        points.sort()
        left=0
        right=1
        ans=0
        while right<len(points):
            x=points[right][0]-points[left][0]
            ans=max(x,ans)
            right+=1
            left+=1
        return ans
    