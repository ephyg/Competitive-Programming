class Solution:
    def minOperations(self, s: str) -> int:
        string1=['0']
        string2=['1']
        cnt1=0
        cnt2=0
        for i in range(0,len(s)-1):
            if(string1[i]=='0'):
                string1.append('1')
                string2.append('0')
            else:
                string1.append('0')
                string2.append('1')
        for i in range(len(s)):
            if(string1[i]!=s[i]):
                cnt1+=1
            if(string2[i]!=s[i]):
                cnt2+=1
        
        return min(cnt1,cnt2)