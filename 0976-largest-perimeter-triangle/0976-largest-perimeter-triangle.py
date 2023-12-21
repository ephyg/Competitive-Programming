class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        large=0
        nums.sort()
        for i in range(len(nums)-2):
            if(nums[i]+nums[i+1]>nums[i+2]):
                large=max(sum(nums[i:i+3]),large)
        return large
            