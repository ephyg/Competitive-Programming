class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=defaultdict(int)
        for i in nums1:
            x[i]+=1
        ans=[]
        for i in nums2:
            if x[i]>0:
                ans.append(i)
                x[i]-=1
                
                
        return ans