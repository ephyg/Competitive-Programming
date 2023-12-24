class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        right=[i for i in nums if(i>pivot)]
        left=[i for i in nums if (i<pivot)]
        middle=[pivot for i in range(len(nums)-len(right)-len(left))]
        return left+middle+right