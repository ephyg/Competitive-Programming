class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=""
        i=0
        while i<len(s):
            if(s[-1-i]=="#"):
                x=chr(96+int(s[-3-i:-1-i]))
                ans+=x
                i+=2
            else:
                x=chr(96+int(s[-1-i]))
                ans+=x
            i+=1
                
               
        return ans[::-1]
                
                
        
                
            
    