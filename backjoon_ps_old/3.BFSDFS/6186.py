"""

"""
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
m = list( list(input().strip()) for _ in range(R))
clump_count = 0
visited = []
dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(i,j):
    global clump_count
    if [i,j] in visited:
        return
    queue = deque([[i,j]])
    
    while queue:
        x,y = queue.popleft()
        visited.append([x,y])

        for n in range(4):
            nx,ny = x + dx[n], y + dy[n]
            if 0 <= nx < R and 0 <= ny < C:
                if [nx,ny] not in visited:
                    if m[nx][ny] == '#':
                        queue.append([nx,ny])        
    clump_count += 1

for i in range(R):
    for j in range(C):
        if m[i][j] == '#':
            bfs(i,j)
            
print(clump_count)

