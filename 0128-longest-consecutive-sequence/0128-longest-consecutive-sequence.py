class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if(not nums):
            return 0
        counter=1
        mx=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                counter+=1
            else:
                counter=1
            mx=max(counter,mx)
            
        return mx
            