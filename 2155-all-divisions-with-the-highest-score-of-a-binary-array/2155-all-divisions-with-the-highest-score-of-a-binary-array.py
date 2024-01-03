class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros=0
        ones=sum(nums)
        answer=[ones]
        for i in range(len(nums)):
            if(nums[i]==0):
                zeros+=1
            else:
                ones-=1
            answer.append(zeros+ones)
        mx=max(answer)
        res=[]
        for i in range(len(answer)):
            if(answer[i]==mx):
                res.append(i)
        return res
        
        
        
