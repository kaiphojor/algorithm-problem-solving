import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())
lattice = list( list(i for i in map(int,input().strip())) for _ in range(R) )
dx,dy = [-1,1,0,0],[0,0,-1,1]

def dfs(x,y):
    lattice[x][y] = -1

    for n in range(4):
        nx,ny = x + dx[n], y + dy[n]

        if 0 <= nx < R and 0 <= ny < C:
            if lattice[nx][ny] == 0:
                dfs(nx,ny)

for i in range(C):
    if lattice[0][i] == 0:
        dfs(0,i)

if -1 in lattice[R-1]:
    print('YES')
else:
    print('NO')
