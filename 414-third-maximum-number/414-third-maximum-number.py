class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x=set(nums)
        nums=list(x)
        if(len(nums)>=3):
            nums.sort()
            return nums[-3]
        else:
            return max(nums)