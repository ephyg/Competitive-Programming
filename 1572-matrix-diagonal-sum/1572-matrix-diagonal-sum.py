class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        for i in range(len(mat)):
            total+=mat[i][i]
            total+=mat[i][len(mat)-i-1]
        if(len(mat)%2)==0:
            return total
        else:
            center=len(mat)//2
            return total-mat[center][center]