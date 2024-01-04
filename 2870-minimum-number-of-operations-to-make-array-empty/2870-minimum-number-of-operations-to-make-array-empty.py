class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dict=Counter(nums)
        ans=0
        freq=[]
        for i in dict:
            freq.append(dict[i])
        for i in range(len(freq)):
            while freq[i]>0:
                r=freq[i]%3
                if(r==0):
                    break
                if(r!=0 and freq[i]>1):
                    freq[i]=freq[i]-2
                    ans+=1
                if(freq[i]==1):
                    return -1
            ans+=(freq[i]//3)
        return ans