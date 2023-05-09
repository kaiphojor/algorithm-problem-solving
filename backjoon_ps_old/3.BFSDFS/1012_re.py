from collections import deque
import sys
# recursion 제한 증가
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx,dy = [-1,1,0,0],[0,0,-1,1]
# def bfs(f,x,y,x_lim,y_lim):
#     queue = deque([(x,y)])
#     while queue:
#         i, j = queue.popleft()
#         for n in range(4):
#             nx,ny = i + dx[n], j + dy[n]
#             if 0 <= nx < x_lim and 0 <= ny < y_lim:
#                 if f[nx][ny] :
#                     queue.append((nx,ny))
#         f[i][j] = False
def dfs(f,x,y,x_lim,y_lim):
    stack = [(x,y)]
    while stack:
        i, j = stack.pop()
        for n in range(4):
            nx,ny = i + dx[n], j + dy[n]
            if 0 <= nx < x_lim and 0 <= ny < y_lim:
                if f[nx][ny] :
                    stack.append((nx,ny))
        f[i][j] = False

for _ in range(int(input().strip())):
    M, N, K = map(int, input().split())
    field = [[False for _ in range(N)] for __ in range(M)]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = True
    for i in range(M):
        for j in range(N):
            if field[i][j]:
                dfs(field,i,j,M,N)
                count += 1
    print(count)
