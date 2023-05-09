"""
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ list(map(int,input().strip())) for _ in range(N)]
result = 0
visited = []
def bfs(b, i,j):
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        for n in range(4):
            nx, ny = x+dx[n], y+dy[n]
            if 0 <= nx < N and 0 <= ny < M :
                if b[nx][ny] == 0:
                    queue.append((nx,ny))
        b[x][y] = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            result += 1 
            bfs(board,i,j)
print(result)
