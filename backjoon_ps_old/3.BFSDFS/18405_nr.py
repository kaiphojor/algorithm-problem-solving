import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int,input().split())
examiner = []
V = []
for i in range(N):
    examiner.append(list(map(int,input().split())))
    for j in range(N):
        if examiner[i][j] != 0:
            V.append((examiner[i][j],i,j))
S, X, Y = map(int,input().split())

def bfs(S,X,Y,V):
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    queue = deque(V)
    count = 0

    while queue and count < S:        
        for _ in range(len(queue)):
            v,x,y = queue.popleft()
            for D in range(4):
                nx,ny = x+dx[D], y+dy[D]
                if 0 <= nx < N and 0 <= ny < N:
                    if examiner[nx][ny] == 0:
                        examiner[nx][ny] = examiner[x][y]
                        queue.append((examiner[nx][ny],nx,ny))
        count += 1
    return examiner[X-1][Y-1]
V.sort()
print(bfs(S,X,Y,V))


