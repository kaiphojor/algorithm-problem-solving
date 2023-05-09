# 09:13 ->09:33
import sys
input = sys.stdin.readline

n = int(input())
n_pyramid = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,-1],[-1,0]
max_pyramid = list( [0] * (i+1) for i in range(n)) 
max_pyramid[0][0] = n_pyramid[0][0]
for i in range(1,n):
    for j in range(l := len(n_pyramid[i])):
        for k in range(2):
            if 0 <= j + dy[k] < l-1:
                max_pyramid[i][j] = max(max_pyramid[i][j],max_pyramid[i+dx[k]][j+dy[k]] + n_pyramid[i][j])

print(max(max_pyramid[n-1]))
