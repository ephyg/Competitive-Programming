class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        visited=set()
        nums=[int(i) for i in range(1,n+1)]
        i=0
        counter=1
        while not len(visited)==(n-1):
            i=i%(n)
            if not nums[i] in visited:
                if counter==k:
                    visited.add(nums[i])
                    counter=0
                counter+=1
            i+=1
        for i in range(1,n+1):
            if(i not in visited):
                return i
        