class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_nums1=set(nums1)
        set_nums2=set(nums2)
        inter=set_nums1.intersection(set_nums2)
        inter=list(inter)
        inter.sort()
        if(inter==[]):
            return -1
        return inter[0]