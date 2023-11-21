class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp=ans=sum(nums[0:k])
        for i in range(k,len(nums)):
            temp+=nums[i]
            temp-=nums[i-k]
            ans=max(temp,ans)
        return ans/k