class Solution:
    def uniquePaths(self,m:int,n:int) -> int:
        twoD_list = []

        for i in range (0,m):
            temp = []
            for j in range (0,n):
                temp.append(1)
            twoD_list.append(temp)

        for i in range (1,m):
            for j in range( 1,n):
                twoD_list[i][j]=twoD_list[i-1][j] + twoD_list[i][j-1]

        return twoD_list[m-1][n-1]
