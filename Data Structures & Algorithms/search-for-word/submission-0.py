class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        path=set()
        for r in range(row):
            for c in range(col):
                if self.dfs(r,c,0,word,row,col,board,path):
                    return True
        return False
    def dfs(self,r,c,i,word,row,col,board,path):
        if i==len(word):
            return True
        if (r<0 or c<0 or r>=row or c>=col or (r,c) in path or word[i]!=board[r][c]):
            return False
        path.add((r,c))
        res = (self.dfs(r,c+1,i+1,word,row,col,board,path) or self.dfs(r,c-1,i+1,word,row,col,board,path) or self.dfs(r+1,c,i+1,word,row,col,board,path) or self.dfs(r-1,c,i+1,word,row,col,board,path) )
        path.remove((r,c))
        return res
                
        