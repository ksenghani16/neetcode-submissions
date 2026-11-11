class Solution:
    def totalNQueens(self, n: int) -> int:
        row=0
        col=0
        board=['.' *n for _ in range(n)]
        count=0
        leftRow=[0]*n
        lower_diagonal=[0]*(2*n-1)
        upper_diagonal=[0]*(2*n-1)
        count=self.solve(n,count,board,row,col,leftRow,lower_diagonal,upper_diagonal)
        return count
    def solve(self,n,count,board,row,col,leftRow,lower_diagonal,upper_diagonal):
        if col==n:
            count+=1
            return count
        for row in range(n):
            if (leftRow[row]==0 and lower_diagonal[row+col]==0 and upper_diagonal[n-1+col-row]==0):
                leftRow[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[n-1+col-row]=1
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                count=self.solve(n,count,board,row,col+1,leftRow,lower_diagonal,upper_diagonal)  
                board[row]=board[row][:col]+"."+board[row][col+1:] 
                leftRow[row]=0
                lower_diagonal[row+col]=0
                upper_diagonal[n-1+col-row]=0
        return count



        