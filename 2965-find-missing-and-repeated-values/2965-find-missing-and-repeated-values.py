class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        other=[]
        for i in range(len(grid)):
            other+=grid[i]
        x=Counter(other)
        ans=[]
        print(other)
        for i in range(len(other)):
            if(x[other[i]]>1):
                ans.append(other[i])
                break
        for i in range(1,len(x)+2):
            if i not in x:
                ans.append(i)
                break
        return ans
            