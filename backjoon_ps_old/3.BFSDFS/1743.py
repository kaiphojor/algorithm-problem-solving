"""
첫번째 - 재귀를 무조건 피하려 했다는 점
두번째 - 반복에서 재귀로 변환할 때 잘못된 것을 가리켰다는 점
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K = map(int, input().split())

mat = [[False for __ in range(M)] for _ in range(N)]
max_junk_count = 1
visited = []
dx, dy = [-1,1,0,0],[0,0,-1,1]

def dfs(m, i, j):

    global visited
    visited.append([i, j])
    junk_count = 1

    for n in range(4):
        nx,ny = i+dx[n], j+dy[n]

        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] and [nx,ny] not in visited:
                junk_count += dfs(m,nx,ny)
    
    return junk_count

for _ in range(K):
    x,y = map(int, input().split())
    mat[x-1][y-1] = True

for i in range(N):
    for j in range(M):
        if mat[i][j] and [i,j] not in visited:
            max_junk_count = max(max_junk_count,dfs(mat,i,j))

print(max_junk_count)