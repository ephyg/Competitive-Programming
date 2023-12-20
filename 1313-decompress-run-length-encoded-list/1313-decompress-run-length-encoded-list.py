class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        j=1
        i=0
        while j<len(nums):
            ls=[nums[j]]*nums[i]
            ans+=ls
            i+=2
            j+=2
        return ans