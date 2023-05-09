import sys
input = sys.stdin.readline
N, S, M = map(int, input().split())
V = list(map(int,input().split()))

dp = [[False for __ in range(M+1)] for _ in range(N+1)]
for i,v in enumerate(dp):
    if i == 0:
        dp[0][S] = True
        continue
    for j,p in enumerate(dp[i-1]):
        if p:
            down = j - V[i-1]
            up = j + V[i-1]
            if down >= 0:
                dp[i][down] = True
            if up <= M:
                dp[i][up] = True
result = -1 
for i in range(M+1):
    if dp[N][i]:
        result = i
print(result)