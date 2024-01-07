class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp=sum(nums[0:k])
        ans=temp
        for i in range(len(nums)-k):
            temp+=nums[i+k]
            temp-=nums[i]
            ans=max(temp,ans)
        return ans/k