class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        ans=[]
        max_len=0
        s=s.split()
        for i in range(len(s)):
            max_len=max(len(s[i]),max_len)
        for i in range(max_len):
            temp=""
            for j in range(len(s)):
                # print(s[i],)
                if(len(s[j])>i):
                    temp+=s[j][i]
                else:
                    temp+=" "
            
            ans.append(temp.rstrip())
            
        return ans
                    