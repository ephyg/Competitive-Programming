class Solution:
    def romanToInt(self, s: str) -> int:
        RomNumber=[]
        for i in range(len(s)):
            if (s[i]=='M'):
                RomNumber.append(1000)
            elif(s[i]=='D'):
                RomNumber.append(500)
            elif(s[i]=='C'):
                RomNumber.append(100)
            elif(s[i]=='L'):
                RomNumber.append(50)
            elif(s[i]=='X'):
                RomNumber.append(10)
            elif(s[i]=='V'):
                RomNumber.append(5)
            else:
                RomNumber.append(1)
        nums=RomNumber[-1]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if (RomNumber[i]>=RomNumber[j]):
                    nums+=RomNumber[i]
                    break
                else:
                    nums-=RomNumber[i]
                    break            
        return nums
