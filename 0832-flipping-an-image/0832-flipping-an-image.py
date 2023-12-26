class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(image)):
            var=image[i][::-1]
            temp=[]
            for j in range(len(image[0])):
                if(var[j]==0):
                    temp.append(1)
                else:
                    temp.append(0)
            ans.append(temp)
        return ans
                