class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        columns=len(board[0])
        queue=deque()
        for i in range(rows):
            if board[i][columns-1]=='O':
                board[i][columns-1]='S'
                queue.append((i,columns-1))
            if board[i][0]=='O':
                board[i][0]='S'
                queue.append((i,0))  
        for j in range(columns):
                if board[0][j]=='O':
                    board[0][j]='S'
                    queue.append((0,j))
                if board[rows-1][j]=='O':
                    board[rows-1][j]='S'
                    queue.append((rows-1,j))
        while len(queue)!=0:
            x,y=queue.popleft()
            for xx,yy in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_x=x+xx
                new_y=y+yy
                if new_x<0 or new_y<0 or new_x>=rows or new_y>=columns:
                    continue
                if board[new_x][new_y]!='O':
                    continue
                board[new_x][new_y]='S'
                queue.append((new_x,new_y))
        for i in range(rows):
            for j in range(columns):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='S':
                    board[i][j]='O'
                    



        