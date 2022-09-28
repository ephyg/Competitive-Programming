class Solution:
    def romanToInt(self, s: str) -> int:
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000
        nums=0
        romNumber=[I,V,X,L,C,D,M]
        RomNumber=[]
        for i in range(len(s)):
            if (s[i]=='M'):
                RomNumber.append(M)
            elif(s[i]=='D'):
                RomNumber.append(D)
            elif(s[i]=='C'):
                RomNumber.append(C)
            elif(s[i]=='L'):
                RomNumber.append(L)
            elif(s[i]=='X'):
                RomNumber.append(X)
            elif(s[i]=='V'):
                RomNumber.append(V)
            else:
                RomNumber.append(I)
    
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if (RomNumber[i]>=RomNumber[j]):
                    nums+=RomNumber[i]
                    print(RomNumber[i],i,j)
                    break
                else:
                    nums+=(RomNumber[j]-RomNumber[i])
                    i+=2
                    j+=2
                    break
               
        
        print (RomNumber)      
        return nums
sol=Solution()
print(sol.romanToInt( "MCDLXVI"))
