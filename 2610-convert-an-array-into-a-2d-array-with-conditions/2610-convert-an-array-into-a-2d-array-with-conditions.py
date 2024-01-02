class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict=Counter(nums)
        mx=max(list(dict.values()))
        answer=[]
        for i in range(mx):
            temp=[]
            for j in dict:
                if(dict[j]!=0 and  (j not in temp)):
                    temp.append(j)
                    dict[j]-=1
            answer.append(temp)
            temp=[]
        return answer
        