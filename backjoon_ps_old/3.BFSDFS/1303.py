import sys
from collections import deque
input = sys.stdin.readline
dx,dy = (-1,1,0,0),(0,0,-1,1)
N, M = map(int, input().split())

soldier_map = [[i for i in input().strip()] for _ in range(M)]

def bfs(field, row, col):
    queue = deque([(row,col)])
    count = 0
    while queue :
        row,col = queue.popleft()
        color = field[row][col]
        if color == ' ':
            continue
        field[row][col] = ' '
        count += 1
        for i in range(4):
            new_x,new_y = col+dx[i],row+dy[i]
            if new_y >= 0 and new_y < M and new_x >= 0 and new_x < N:
                if field[new_y][new_x] == color :
                    queue.append((new_y,new_x))
    return count ** 2
w_count, b_count = 0, 0
for i in range(M):
    for j in range(N):
        color = soldier_map[i][j]
        if color == 'B':
            b_count += bfs(soldier_map,i,j)
        elif color == 'W':
            w_count += bfs(soldier_map,i,j)
print(w_count,b_count)

"""
best short coding  https://www.acmicpc.net/source/22628203

m,n=map(int,input().split())
g=[[*input()] for i in[0]*n]
def f(i,j,x):
    q=[(i,j)];c=1;g[i][j]=0
    while q:
        i,j=q.pop()
        for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if n>i>-1<j<m and g[i][j]==x:q+=[[i,j]];g[i][j]=0;c+=1
    return c*c
l=[0,0]
r=range
for i in r(n):
    for j in r(m):
        if(a:=g[i][j]):l[a=='B']+=f(i,j,a)
print(*l)
"""