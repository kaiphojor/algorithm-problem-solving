import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
dx,dy = [-1,1,0,0],[0,0,-1,1]
area = [list(map(int,input().split())) for _ in range(N)]
s, e = min(map(min,area)),max(map(max,area))
result = 1

#dfs 완전탐색
def dfs(i, j, n):
    global visited
    if visited[i][j]:
        return
    visited[i][j] = True
    for d in range(4):
        nx, ny = i+dx[d],j+dy[d]
        if 0<= nx < n and 0<= ny < n:
            dfs(nx,ny,n)

# 잠기기 시작하는 높이 부터 다 잠기는 높이까지
for threshold in range(s,e):    
    area_count = 0
    visited= [[False] * N for _ in range(N)]
    # 잠긴 곳 초기화
    for p in range(N):
        for q in range(N):
            if area[p][q] <= threshold:
                visited[p][q] = True
    # dfs 완전탐색
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:    
                dfs( i, j, N)
                area_count += 1
    result = max(result, area_count)
    
print(result)
