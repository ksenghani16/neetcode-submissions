class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows=len(grid)
        columns=len(grid[0]) 
        visited=[[0 for _ in range(columns+1)]for _ in range(rows+1)]
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1" and visited[i][j]==0:
                    count+=1
                    self.bfs(i,j,visited,grid)
        return count
    def bfs(self,i,j,visited,grid):
        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        queue.append((i,j))
        visited[i][j]=1
        while len(queue)!=0:
            x,y=queue.popleft()
            for xx,yy in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_x,new_y=x+xx,y+yy
                if new_x<0 or new_y<0 or new_x>=rows or new_y>=columns:
                    continue
                if grid[new_x][new_y] == "0" or visited[new_x][new_y]==1:
                    continue
                visited[new_x][new_y]=1
                queue.append((new_x,new_y))

            
            

        