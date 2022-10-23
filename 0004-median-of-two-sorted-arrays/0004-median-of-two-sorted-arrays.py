class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        x=len(num)
        if(x%2==0):
            y=x//2
            return (num[y-1]+num[y])/2
        else:
            return float(num[x//2])