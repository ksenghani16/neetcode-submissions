class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        fresh=0
        minutes=0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1 
        while queue and fresh>0:
            for _ in range(len(queue)):
                x,y=queue.popleft()
                for xx,yy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_x=x+xx
                    new_y=y+yy
                    if new_x<0 or new_y<0 or new_x>=rows or new_y>=columns:
                        continue
                    if grid[new_x][new_y]!=1:
                        continue
                    grid[new_x][new_y]=2
                    fresh-=1
                    queue.append((new_x,new_y))
            minutes+=1
        if fresh>0:
            return -1
        return minutes

        