import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def bfs(b,n):
    dx,dy = [0,1],[1,0]
    queue = deque([[0,0]])
    available_path = 0
    while queue:
        loc = queue.popleft()
        x,y = loc[0],loc[1]
        for i in range(2):
            multiple = b[loc[0]][loc[1]]
            nx,ny = loc[0] + dx[i] * multiple, loc[1] + dy[i] * multiple 
            if 0 <= nx < n and 0 <= ny < n:
                if nx == n-1 and ny == n-1:
                    available_path += 1
                else:
                    queue.append([nx,ny])
    return available_path
print(bfs(board,N))