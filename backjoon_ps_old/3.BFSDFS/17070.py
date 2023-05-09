from collections import deque
N = int(input())
h = [ list(map(int,input().split())) for _ in range(N)]
dx,dy = [0,1,1],[1,1,0]
new_step = {0:[0,1],1:[0,1,2],2:[1,2]}
total = 0

def dfs(x,y,d):
    global total
    if x == N-1 and y == N-1:
        total += 1
        return
    # 가로
    if d == 0 or d == 1:
        ny = y + 1
        if ny < N and h[x][ny] == 0:
            dfs(x,ny,0)
    # 세로
    if d == 1 or d == 2:
        nx = x + 1
        if nx < N and h[nx][y] == 0:
            dfs(nx,y,2)
    # 대각선 
    nx,ny = x+1,y+1
    if nx < N and ny < N and h[nx][ny] == 0 and h[nx][y] == 0 and h[x][ny] == 0:
        dfs(nx,ny,1)
        
if h[N-1][N-1] == 1:
    print(0)
else:
    dfs(0,1,0)
    print(total)