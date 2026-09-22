class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==0:
                    queue.append((i,j))
        while len(queue)!=0:
            x,y=queue.popleft()
            for xx,yy in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_x=x+xx
                new_y=y+yy
                if new_x<0 or new_y<0 or new_x>=rows or new_y>=columns:
                    continue
                if grid[new_x][new_y]!=2147483647:
                    continue
                grid[new_x][new_y]=grid[x][y]+1
                queue.append((new_x,new_y))


        