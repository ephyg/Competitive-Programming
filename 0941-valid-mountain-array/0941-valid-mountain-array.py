class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        pick=0
        inc=0
        dec=0
        if(len(arr)>=3):
            for i in range(len(arr)-1):
                if arr[i+1]>arr[i] and dec==0:
                    inc+=1
                elif arr[i+1]<arr[i] and inc>0:
                    dec+=1
                else:
                    return False
            if(inc!=0 and dec!=0):
                return True
            else:
                return False
        else:
            return False
                    
        
            