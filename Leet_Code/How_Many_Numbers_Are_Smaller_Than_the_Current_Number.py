from typing import List

from matplotlib.cbook import index_of
from numpy import append


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    count+=1
            ans.append(count)
        return ans