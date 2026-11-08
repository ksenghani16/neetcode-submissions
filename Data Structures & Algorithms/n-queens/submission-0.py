class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row=0
        col=0
        ans=[]
        board=["." * n for _ in range(n)]
        leftrow=[0]*n
        lower_diagonal=[0]*(2*n-1)
        upper_diagonal=[0]*(2*n-1)
        self.solve(ans,board,row,col,leftrow,lower_diagonal,upper_diagonal,n)
        return ans
    def solve(self,ans,board,row,col,leftrow,lower_diagonal,upper_diagonal,n):
        if n==col:
            ans.append(board[:])
            return ans
        for row in range(n):
            if (leftrow[row]==0 and lower_diagonal[row+col]==0 and upper_diagonal[n-1+col-row]==0):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]  
                leftrow[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[n-1+col-row]=1
                self.solve(ans,board,row,col+1,leftrow,lower_diagonal,upper_diagonal,n)
                board[row]=board[row][:col]+'.'+board[row][col+1:]
                leftrow[row]=0
                lower_diagonal[row+col]=0
                upper_diagonal[n-1+col-row]=0
        

        