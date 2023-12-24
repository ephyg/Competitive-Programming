class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[i for i in nums if(i>0)]
        negative=[i for i in nums if(i<0)]
        ans=[]
        for i in range(len(nums)//2):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans
            